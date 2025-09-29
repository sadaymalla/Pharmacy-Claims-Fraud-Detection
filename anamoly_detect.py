import numpy as np, pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler
from scipy.stats import rankdata

def detect_anomalies(df, contamination=0.01):
    features = ['avg_cost_per_claim','avg_cost_per_30day_fill',
                'avg_days_supply_per_claim','refill_rate','Tot_Clms']
    print(features)
    X = df[features].fillna(0).values
    Xs = StandardScaler().fit_transform(X)

    iso = IsolationForest(n_estimators=200, contamination=contamination, random_state=42)
    iso_preds = iso.fit_predict(Xs); iso_scores = -iso.decision_function(Xs)

    lof = LocalOutlierFactor(n_neighbors=35, contamination=contamination)
    lof_preds = lof.fit_predict(Xs); lof_scores = -lof.negative_outlier_factor_

    iso_rank, lof_rank = rankdata(iso_scores), rankdata(lof_scores)
    combined = (iso_rank + lof_rank)/2.0; combined /= np.max(combined)

    df = df.copy().reset_index(drop=True)
    df['iso_score'], df['lof_score'], df['combined_score'] = iso_scores, lof_scores, combined
    df['anomaly_flag'] = (iso_preds==-1) | (lof_preds==-1)
    return df