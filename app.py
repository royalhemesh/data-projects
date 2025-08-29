import streamlit as st
import plotly.express as px
import pandas as pd
from data_processing import load_and_prepare_data

# --- Page Configuration ---
st.set_page_config(
    page_title="Olist Customer Satisfaction Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- Data Loading ---
# Use a cache to avoid reloading data on every interaction
@st.cache_data
def load_data():
    df = load_and_prepare_data()
    # Ensure the timestamp column is timezone-naive for slider compatibility
    df['order_purchase_timestamp'] = df['order_purchase_timestamp'].dt.tz_localize(None)
    return df

df = load_data()

if df is None:
    st.error("Failed to load data. Please check the data files and path.")
    st.stop()

# --- Dashboard Title ---
st.title("📊 Olist Customer Satisfaction & Delivery Performance")
st.markdown("This dashboard analyzes customer satisfaction based on delivery timeliness.")

# --- Sidebar Filters ---
st.sidebar.header("Filters")

# Date Range Slider
min_date = df['order_purchase_timestamp'].min().to_pydatetime()
max_date = df['order_purchase_timestamp'].max().to_pydatetime()

start_date, end_date = st.sidebar.slider(
    "Select Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="YYYY-MM-DD"
)

# Product Category Dropdown
all_categories = df['product_category_name'].unique()
selected_categories = st.sidebar.multiselect(
    "Select Product Category",
    options=all_categories,
    default=all_categories
)

# --- Filtering Data ---
filtered_df = df[
    (df['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
    (df['order_purchase_timestamp'] <= pd.to_datetime(end_date)) &
    (df['product_category_name'].isin(selected_categories))
]

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# --- KPI Metrics ---
total_orders = filtered_df.shape[0]
avg_review_score = filtered_df['Review Score'].mean()
late_deliveries = filtered_df[filtered_df['Delivery Status'] == 'Late'].shape[0]
late_delivery_rate = (late_deliveries / total_orders) if total_orders > 0 else 0
total_revenue = filtered_df['price'].sum() + filtered_df['freight_value'].sum()

st.header("Executive KPI Summary")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Orders", value=f"{total_orders:,}")

with col2:
    st.metric(label="Avg. Review Score", value=f"{avg_review_score:.2f}")

with col3:
    st.metric(label="Late Delivery Rate", value=f"{late_delivery_rate:.2%}")

with col4:
    st.metric(label="Total Revenue", value=f"R${total_revenue:,.2f}")

st.markdown("---")

# --- Visualizations ---
st.header("Detailed Analysis")
left_col, right_col = st.columns(2)

# Visual 1: Average Review Score by Delivery Status
with left_col:
    st.subheader("Average Review Score by Delivery Status")
    avg_score_by_status = filtered_df.groupby('Delivery Status')['Review Score'].mean().reset_index()
    fig1 = px.bar(
        avg_score_by_status,
        x='Delivery Status',
        y='Review Score',
        color='Delivery Status',
        color_discrete_map={'Late': '#FF6347', 'On-Time/Early': '#4682B4'},
        text_auto='.2f',
        height=400
    )
    st.plotly_chart(fig1, use_container_width=True)

# Visual 2: Late Delivery Rate by State (Using a bar chart for simplicity as maps can be slow)
with left_col:
    st.subheader("Late Delivery Rate by State")
    state_df = filtered_df.groupby('customer_state').agg(
        total_orders=('order_id', 'count'),
        late_orders=('Delivery Status', lambda x: (x == 'Late').sum())
    ).reset_index()
    state_df['late_rate'] = state_df['late_orders'] / state_df['total_orders']
    state_df = state_df.sort_values('late_rate', ascending=False).head(15) # Top 15
    fig2 = px.bar(
        state_df,
        x='late_rate',
        y='customer_state',
        orientation='h',
        labels={'late_rate': 'Late Delivery Rate', 'customer_state': 'State'},
        text='late_rate',
        height=400
    )
    fig2.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    st.plotly_chart(fig2, use_container_width=True)

# Visual 3: Revenue vs. Satisfaction by Product Category
with right_col:
    st.subheader("Revenue vs. Satisfaction by Product Category")
    category_df = filtered_df.groupby('product_category_name').agg(
        Total_Revenue=('price', 'sum'),
        Avg_Review_Score=('Review Score', 'mean'),
        Total_Orders=('order_id', 'count')
    ).reset_index()
    fig3 = px.scatter(
        category_df,
        x='Avg_Review_Score',
        y='Total_Revenue',
        size='Total_Orders',
        color='product_category_name',
        hover_name='product_category_name',
        size_max=60,
        height=400,
        labels={'Avg_Review_Score': 'Average Review Score', 'Total_Revenue': 'Total Revenue'}
    )
    fig3.update_layout(showlegend=False)
    st.plotly_chart(fig3, use_container_width=True)

# Visual 4: Monthly Orders & Late Delivery Trend
with right_col:
    st.subheader("Monthly Orders & Late Delivery Trend")
    monthly_df = filtered_df.copy()
    monthly_df['Month'] = monthly_df['order_purchase_timestamp'].dt.to_period('M').astype(str)
    monthly_trend = monthly_df.groupby('Month').agg(
        Total_Orders=('order_id', 'count'),
        Late_Orders=('Delivery Status', lambda x: (x == 'Late').sum())
    ).reset_index()
    monthly_trend['Late_Rate'] = monthly_trend['Late_Orders'] / monthly_trend['Total_Orders']

    # Create a dual-axis chart is tricky in Plotly Express, but we can overlay
    from plotly.subplots import make_subplots
    fig4 = make_subplots(specs=[[{"secondary_y": True}]])

    # Add bars for Total Orders
    fig4.add_trace(
        px.bar(monthly_trend, x='Month', y='Total_Orders').data[0],
        secondary_y=False,
    )
    fig4.update_traces(marker_color='#4682B4', name='Total Orders')

    # Add line for Late Delivery Rate
    fig4.add_trace(
        px.line(monthly_trend, x='Month', y='Late_Rate').data[0],
        secondary_y=True,
    )
    fig4.update_traces(marker_color='#FF6347', name='Late Delivery Rate')

    fig4.update_layout(height=400, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    fig4.update_yaxes(title_text="Total Orders", secondary_y=False)
    fig4.update_yaxes(title_text="Late Delivery Rate", secondary_y=True, tickformat=".0%")

    st.plotly_chart(fig4, use_container_width=True)