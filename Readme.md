🧮 Customer & Sales Data Analysis with SQL / Python

## 📖 Overview  
This project showcases end-to-end data analytics using **SQL** and Python. The raw customer & sales dataset is ingested into PostgreSQL, cleaned via SQL, and analyzed with complex queries. Insights are then visualized with Python in a Jupyter notebook and presented via a simple web app. The goal is to demonstrate strong SQL querying, data cleaning, EDA, and storytelling.

Key capabilities include:
- Data cleansing (handling missing values, duplicates, enforcing constraints)
- Aggregations, window functions, joins, and time-based trend analysis
- Visualizing business metrics such as sales by region, top customers, spending distribution, revenue trends, and churn

---

## 🔧 Technology Stack

| Component         | Tools / Libraries                          |
|-------------------|---------------------------------------------|
| Database          | PostgreSQL                                  |
| Query Language    | SQL (DDL, DML, Aggregations, Window Functions) |
| Data Processing   | Python 3.9+, Pandas, NumPy                  |
| Visualization     | Matplotlib, Seaborn                        |
| Jupyter Notebooks | For documenting analysis & embedding SQL    |
| Web App           | Streamlit / Flask (for interactive dashboards) |

---

## 🛠 Project Structure

```text
data-projects/
├── olsit data/             ← Raw CSV data files  
├── requirements.txt        ← Python library dependencies  
├── data_processing.py      ← Scripts to prepare / clean the data (if needed)  
├── analysis.sql            ← Key SQL queries for insights and reporting  
├── hemesh.ipynb            ← Jupyter Notebook with analysis, visualizations & query explanations  
├── app.py                  ← Web application to share key metrics and dashboards  
└── README.md               ← Project documentation (this file)  
🚀 Getting Started
Follow these steps to run the project on your machine:

Clone the repository

bash
Copy code
git clone https://github.com/royalhemesh/data-projects.git
cd data-projects
Install prerequisites

Install PostgreSQL (or have access to a running instance)

Python 3.9+

Create & activate virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate      # macOS / Linux  
# or  
.\venv\Scripts\activate       # Windows
pip install -r requirements.txt
Set up the database

Create a database (e.g., olsit_db)

Import the schema & load raw data using SQL / scripts you have

Use analysis.sql or data_processing.py if any loading / cleaning needs

Perform analysis

Open hemesh.ipynb in Jupyter:

bash
Copy code
jupyter notebook
Run SQL queries for insights like: top 5 customers, revenue by product category, sales trend by month, churn analysis, etc.

View the dashboard / web app

If using Streamlit:

bash
Copy code
streamlit run app.py
If using Flask:

bash
Copy code
python app.py
Go to the web address shown in console (e.g., http://localhost:8501)

📊 Example Insights You’ll Find
Here are some of the specific business insights covered in this project:

Top-performing Regions: Which geographic regions contribute the most to sales

Customer Lifetime & Churn: Analyses of repeated vs one-time purchasers

Sales Trends Over Time: Month by month, seasonal variation in revenue

Product / Category Performance: Best-selling items, categories with low vs high returns

💡 Best Practices & Skills Demonstrated
Clean & normalized relational schema

Constraints: NOT NULL, PRIMARY KEY, CHECK used for maintaining data integrity

Use of window functions (e.g., for running totals, ranking)

Complex joins and aggregations

Visualization for storytelling: charts for trends, comparisons, distributions

✅ How to Contribute
Contributions are welcome! If you wish to improve queries, visualizations, or add new metrics:

Fork the repo

Create a new branch for your feature (e.g., feature/new-insight)

Submit a pull request with clear description & sample output

📄 License
This project is released under the MIT License. See the LICENSE file for more details.

📧 Contact
For any questions or feedback, feel free to reach out:
Hemesh — [your email or LinkedIn handle]
