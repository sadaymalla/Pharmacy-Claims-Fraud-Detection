import streamlit as st, pandas as pd, plotly.express as px

def run_dashboard(results_csv="anomaly_results.csv"):
    df = pd.read_csv(results_csv)

    st.title("Pharmacy Claim Fraud Detection Dashboard")

    # Summary
    total = len(df)
    anomalies = df["anomaly_flag"].sum()
    st.metric("Total Records", total)
    st.metric("Flagged Anomalies", anomalies)

    # Show only top anomalies
    top = 100
    st.subheader(f"Top {top} Suspicious Providers")
    top_anomalies = df[df["anomaly_flag"] == True].sort_values("combined_score", ascending=False).head(top)
    st.dataframe(top_anomalies)

    # Use sampling for scatter plot
    st.subheader("Anomaly Visualization")
    sample_df = df.sample(min(10000, len(df)), random_state=42)  # sample 10k rows
    fig = px.scatter(
        sample_df,
        x="refill_rate",
        y="avg_cost_per_claim",
        color="anomaly_flag",
        hover_data=["PRSCRBR_NPI", "Prscrbr_Last_Org_Name", "avg_days_supply_per_claim","combined_score"],
        title="Refill Rate vs Cost (Sampled Anomalies)"
    )
    st.plotly_chart(fig, use_container_width=True)