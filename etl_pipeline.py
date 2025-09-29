import pandas as pd, numpy as np

REQUIRED_COLS = [
        "PRSCRBR_NPI", "Prscrbr_Last_Org_Name",
        "Tot_Clms", "Tot_Drug_Cst", "Tot_30day_Fills", "Tot_Day_Suply"
    ]

def load_data(csv_path):
    return pd.read_csv(csv_path, usecols=REQUIRED_COLS, low_memory=False)

def build_features(df):
    df = df.copy()

    for c in ['Tot_Clms','Tot_Drug_Cst','Tot_30day_Fills','Tot_Day_Suply']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
            
    df = df[df["Tot_Clms"]>0]
    df["avg_cost_per_claim"] = df["Tot_Drug_Cst"]/df["Tot_Clms"]
    df['avg_cost_per_30day_fill'] = np.where(df['Tot_30day_Fills']>0,
                                             df['Tot_Drug_Cst']/df['Tot_30day_Fills'],0)
    df['avg_days_supply_per_claim'] = np.where(df['Tot_Clms']>0,
                                               df['Tot_Day_Suply']/df['Tot_Clms'], np.nan)
    df['refill_rate'] = np.where(df['Tot_Clms']>0,
                                 df['Tot_30day_Fills']/df['Tot_Clms'], 0)
    df['avg_days_supply_per_claim'] = df['avg_days_supply_per_claim'].fillna(
        df['avg_days_supply_per_claim'].median())
    return df
