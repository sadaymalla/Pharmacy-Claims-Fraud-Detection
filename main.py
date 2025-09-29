import argparse
from etl_pipeline import load_data, build_features
from anamoly_detect import detect_anomalies
from dashboard import run_dashboard

def run_etl(csv_path):
    print("Loading data...")
    df = load_data(csv_path)
    print("Building features...")
    df_feat = build_features(df)
    print("Detecting anomalies...")
    df_out = detect_anomalies(df=df_feat)
    df_out.to_csv("anomaly_results.csv", index=False)
    print("Saved -> anomaly_results.csv")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=str, help="Path to claims CSV")
    parser.add_argument("--etl", action="store_true")
    parser.add_argument("--dashboard", action="store_true")
    args = parser.parse_args()

    if args.etl:
        run_etl(args.csv)
    if args.dashboard:
        run_dashboard("anomaly_results.csv")