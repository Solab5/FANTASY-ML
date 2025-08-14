from pathlib import Path
import pandas as pd, json, datetime as dt

DATA = Path("data")
RAW = DATA/"raw"; PROC = DATA/"processed"
RAW.mkdir(parents=True, exist_ok=True); PROC.mkdir(parents=True, exist_ok=True)

def save_json(obj, name:str):
    p = RAW/f"{name}.json"
    with open(p, "w") as f: json.dump(obj, f)
    return p

def save_parquet(df:pd.DataFrame, name:str):
    p = PROC/f"{name}.parquet"
    df.to_parquet(p, index=False); return p

def dated_tag(prefix:str):
    ts = dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    return f"{prefix}_{ts}"
