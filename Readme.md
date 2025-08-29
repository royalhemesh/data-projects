# Olist Customer Satisfaction Analysis: A Deep Dive into E-Commerce Reviews

This repository contains an end-to-end data analysis project that identifies the primary driver of negative customer reviews on the Olist e-commerce platform. The analysis proceeds from raw data cleaning to a final set of actionable business recommendations.

## 🎯 Business Problem

Customer satisfaction is a critical metric for the success and growth of any e-commerce platform. Negative reviews can deter potential customers and highlight operational inefficiencies. Therefore, the central question for this project is:

> **What are the primary drivers of low customer review scores (1-2 stars), and how can Olist use this information to improve customer satisfaction?**

---

## 💡 Key Insights & Actionable Recommendations

For recruiters and hiring managers, here are the key takeaways from the analysis:

#### Insights
1.  **Delivery Timeliness is the #1 Predictor of Satisfaction:** The analysis proves with statistical significance that a late delivery is the single most powerful predictor of a negative (1 or 2-star) review.
2.  **Late Deliveries Overshadow All Other Factors:** The negative impact of a late delivery is so strong that it consistently overshadows other factors like product category, price, or freight value.

#### Recommendations
1.  **Optimize the Logistics Pipeline:** Olist should focus operational improvements on its shipping and delivery network. By analyzing carrier performance and setting more accurate delivery estimates, the company can directly address the primary cause of customer dissatisfaction.
2.  **Implement Proactive Customer Communication:** For orders projected to be late, Olist should automatically notify the customer of the delay. This transparency, coupled with a small gesture like a future discount, can mitigate the negative experience and improve customer retention.

---

## 📊 Key Visualizations

The most impactful finding is visualized in the box plot below, which shows a dramatic drop in review scores for orders that were delivered late compared to those delivered on time or early.


*This chart clearly illustrates that while on-time deliveries cluster around 4 and 5-star reviews, late deliveries are centered around 1 and 2 stars.*

---

## 🛠️ Tech Stack

* **Language:** `Python`
* **Libraries:** `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `SciPy`
* **Environment:** `Jupyter Notebook`

---

## 🔬 Analysis Workflow

The project followed a structured data analysis workflow:

1.  **Data Cleaning & Aggregation:** Loaded 5 raw datasets, handled missing values, converted data types, and joined them into a single master table for analysis.
2.  **Feature Engineering:** Created new features to aid the analysis, including `delivery_time` and `estimated_vs_actual_delivery`, which was crucial for the final insight.
3.  **Exploratory Data Analysis (EDA):** Performed univariate, bivariate, and multivariate analysis to uncover initial patterns, with a focus on how different variables impacted the `review_score`.
4.  **Hypothesis Testing:** Formalized the key observation from the EDA with a statistical test. An independent two-sample t-test was conducted, which confirmed that late deliveries result in a statistically significant decrease in average review scores (**p < 0.001**).

---

## 🚀 How to Replicate

To replicate this analysis on your own machine:

1.  Clone this repository:
    ```bash
    git clone [https://github.com/your-username/Olist-Analysis.git](https://github.com/your-username/Olist-Analysis.git)
    ```
2.  Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
3.  Launch the Jupyter Notebook:
    ```bash
    jupyter notebook Olist_Analysis.ipynb
    ```

## 📂 Data Source

The dataset used is the "Brazilian E-Commerce Public Dataset by Olist," which is publicly available on **[Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)**.