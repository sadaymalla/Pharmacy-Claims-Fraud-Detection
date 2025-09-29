Pharmacy Claims Fraud Detection

This project provides a pipeline for detecting anomalies (e.g., potential fraud) in pharmacy claims data using machine learning techniques and visualizing the results with an interactive dashboard.

📂 Project Structure

etl_pipeline.py → Handles data loading, preprocessing, and feature engineering.

anamoly_detect.py → Runs anomaly detection using Isolation Forest and Local Outlier Factor (LOF).

dashboard.py → Streamlit dashboard for visualizing anomalies.

main.py → Entry point for running the ETL pipeline, anomaly detection, and/or dashboard.

⚙️ Installation

Clone the repository and install dependencies:

git clone <your-repo-url>
cd <your-repo>
pip install -r requirements.txt

Required Python Packages

pandas

numpy

scikit-learn

scipy

streamlit

plotly

🚀 Usage
1. Run ETL + Anomaly Detection

Run preprocessing and anomaly detection on claims CSV:

python main.py -- --etl --csv ./data/<name>.csv


This will:

Load claims data

Build derived features (e.g., average cost per claim, refill rate)

Detect anomalies using ensemble methods

Save results to anomaly_results.csv

2. Run Dashboard

After generating anomaly results:

python main.py --dashboard


This will launch a web dashboard where you can:

View summary metrics

Explore flagged anomalies

Visualize claims data in interactive scatter plots

📊 Features
ETL (etl_pipeline.py)

Cleans and typecasts claim columns

Generates features such as:

avg_cost_per_claim

avg_cost_per_30day_fill

avg_days_supply_per_claim

refill_rate

Anomaly Detection (anamoly_detect.py)

Uses Isolation Forest and Local Outlier Factor (LOF)

Combines model scores into a unified anomaly score

Flags anomalous providers

Dashboard (dashboard.py)

Interactive Streamlit dashboard

Metrics: total records, flagged anomalies

Data table: top suspicious providers

Visualization: anomaly scatter plots (sampled for performance)

📁 Output

anomaly_results.csv → CSV file with enriched features, anomaly scores, and flags.

Columns include:

Original claims data (PRSCRBR_NPI, Prscrbr_Last_Org_Name, etc.)

Engineered features (avg_cost_per_claim, refill_rate, etc.)

Model outputs (combined_score)

anomaly_flag (boolean indicator)

🔮 Next Steps

Fine-tune contamination rates and model hyperparameters.

Enhance visualization with time-based trends.

Extend support for larger datasets with scalable storage/processing.