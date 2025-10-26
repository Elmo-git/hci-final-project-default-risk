
import pandas as pd

def quick_overview(df: pd.DataFrame, target: str | None = None) -> pd.DataFrame:
    meta = []
    for c in df.columns:
        s = df[c]
        meta.append({
            "column": c,
            "dtype": str(s.dtype),
            "n_unique": s.nunique(dropna=True),
            "n_missing": int(s.isna().sum()),
            "pct_missing": float(s.isna().mean()*100),
        })
    m = pd.DataFrame(meta).sort_values("pct_missing", ascending=False)
    if target and target in m["column"].values:
        m.loc[m["column"]==target,"column"] = m.loc[m["column"]==target,"column"] + "  <TARGET>"
    return m
