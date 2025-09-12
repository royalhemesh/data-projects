📊 Customer & Sales Data Analysis using SQL
📖 Overview

This project demonstrates end-to-end data analysis using SQL. The dataset was ingested into a PostgreSQL database, cleaned, and analyzed using SQL queries to extract valuable business insights.
The project highlights how structured data can be transformed into actionable insights through query optimization, aggregation, and reporting techniques.

The analysis is complemented by a Jupyter Notebook that explains the query logic, insights, and visualizations for better storytelling.

✨ Key Features

Database Design & Setup

Imported raw .csv data into PostgreSQL using .sql schema and DDL scripts.

Normalized data into relational tables for efficient querying.

SQL Data Cleaning

Handled duplicates, missing values, and inconsistent entries using SQL statements.

Enforced constraints like NOT NULL, PRIMARY KEY, and CHECK for data integrity.

Exploratory Data Analysis (EDA) with SQL

Used GROUP BY, JOIN, CTEs, and Window Functions for business insights.

Key KPIs: Top-selling products, revenue by region, customer churn patterns, etc.

Advanced SQL Queries

Ranking queries using ROW_NUMBER() and RANK().

Rolling averages and cumulative sales with WINDOW FUNCTIONS.

Subqueries and nested SELECT statements for deeper insights.

Visualization

Jupyter Notebook with matplotlib & seaborn to visualize results of SQL queries.

Plots include revenue trends, top customers, and sales distribution.

🛠️ Technology Stack

Database: PostgreSQL 13+

Query Language: SQL (DDL, DML, Aggregations, Window Functions)

Notebook: Jupyter Notebook (for explanation + visualization)

Python Libraries:

psycopg2 / SQLAlchemy (for DB connection)

pandas, numpy (data manipulation)

matplotlib, seaborn (visualization)

🚀 Getting Started
Prerequisites

Install PostgreSQL and pgAdmin (or any SQL client).

Python 3.9+ with Jupyter Notebook.

Setup

Clone this repository:

git clone https://github.com/royalhemesh/sql-analysis-project.git
cd sql-analysis-project


Import the SQL schema & dataset into PostgreSQL:

\i data_setup.sql;


Open Jupyter Notebook for step-by-step EDA:

jupyter notebook analysis.ipynb

📁 Project Structure
.
├── data_setup.sql        # SQL script for schema & dataset creation
├── analysis.ipynb        # Jupyter Notebook with queries & visualizations
├── requirements.txt      # Python dependencies for visualization
└── README.md             # Project documentation

📊 Example Insights

Top 5 Countries by Sales

SELECT country, SUM(sales) AS total_sales
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY country
ORDER BY total_sales DESC
LIMIT 5;


Customer Retention (Churn Analysis)
Using WINDOW FUNCTIONS to calculate repeat purchases.

Revenue Growth Trend
Month-wise revenue calculated with DATE_TRUNC() and visualized in Python.

🤝 Contributing

Contributions, suggestions, and optimizations for queries are welcome! Open an issue or submit a pull request.

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
