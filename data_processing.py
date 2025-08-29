import pandas as pd

def load_and_prepare_data(data_path='olsit data/'):
    """
    Loads, merges, and cleans the Olist e-commerce dataset.

    This function replicates the data preparation steps from the initial
    Jupyter Notebook analysis to create a master table.

    Args:
        data_path (str): The path to the directory containing the CSV files.

    Returns:
        pandas.DataFrame: A cleaned and merged DataFrame ready for analysis.
    """
    # --- 1. Data Loading ---
    try:
        orders = pd.read_csv(f'{data_path}olist_orders_dataset.csv')
        reviews = pd.read_csv(f'{data_path}olist_order_reviews_dataset.csv')
        items = pd.read_csv(f'{data_path}olist_order_items_dataset.csv')
        products = pd.read_csv(f'{data_path}olist_products_dataset.csv')
        customers = pd.read_csv(f'{data_path}olist_customers_dataset.csv')
    except FileNotFoundError as e:
        print(f"Error loading data files: {e}")
        print("Please ensure the Olist dataset CSV files are in the correct directory.")
        return None

    # --- 2. Initial Cleaning ---
    # Drop rows with null product category names
    products.dropna(subset=['product_category_name'], inplace=True)

    # Convert date columns to datetime objects, coercing errors
    date_cols = [
        'order_purchase_timestamp', 'order_approved_at',
        'order_delivered_carrier_date', 'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]
    for col in date_cols:
        orders[col] = pd.to_datetime(orders[col], errors='coerce')

    # Drop orders without a delivery date, as they are essential for our analysis
    orders.dropna(subset=['order_delivered_customer_date', 'order_estimated_delivery_date'], inplace=True)

    # --- 3. Feature Engineering ---
    # Calculate the difference between estimated and actual delivery
    # A negative value means the order was delivered AFTER the estimate (late)
    orders['Delivery Timeliness'] = (orders['order_estimated_delivery_date'] - orders['order_delivered_customer_date']).dt.days

    # Create a categorical 'Delivery Status' column
    # Note: In the notebook, this was `estimated_vs_actual_delivery`. Renaming for clarity.
    orders['Delivery Status'] = orders['Delivery Timeliness'].apply(lambda x: 'Late' if x < 0 else 'On-Time/Early')

    # --- 4. Data Merging ---
    master_df = pd.merge(orders, reviews, on='order_id')
    master_df = pd.merge(master_df, items, on='order_id')
    master_df = pd.merge(master_df, products, on='product_id')
    master_df = pd.merge(master_df, customers, on='customer_id')

    # --- 5. Data Aggregation ---
    # To handle orders with multiple items, we aggregate to the order level.
    # We sum price and freight, and take the first value for descriptive columns.
    agg_funcs = {
        'order_purchase_timestamp': 'first',
        'review_score': 'first',
        'Delivery Timeliness': 'first',
        'Delivery Status': 'first',
        'price': 'sum',
        'freight_value': 'sum',
        'product_category_name': 'first',
        'customer_state': 'first'
        # Add other columns if needed, using 'first' as the agg func
    }

    # We group by the unique order ID
    final_df = master_df.groupby('order_id').agg(agg_funcs).reset_index()

    # --- 6. Final Touches ---
    # Rename columns for clarity in the dashboard
    final_df.rename(columns={'review_score': 'Review Score'}, inplace=True)

    print("Data processing complete.")
    return final_df

if __name__ == '__main__':
    # For testing the script directly
    master_table = load_and_prepare_data()
    if master_table is not None:
        print("Master table created successfully:")
        print(master_table.head())
        print(f"\nShape: {master_table.shape}")
        print("\nInfo:")
        master_table.info()