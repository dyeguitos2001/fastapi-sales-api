from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "sales_summary_gold.csv"

def load_sales_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_FILE)
    return df

def get_all_sales(category: str | None = None) -> list[dict]:
    df = load_sales_data()

    if category:
        df = df[df["category"].str.lower() == category.lower()]

    return df.to_dict(orient="records")

def get_sales_by_region(region: str) -> list[dict]:
    df = load_sales_data()
    filtered = df[df["region"].str.lower() == region.lower()]
    return filtered.to_dict(orient="records")

def get_sales_summary() -> dict:
    df = load_sales_data()
    return {
        "total_revenue": float(df["revenue"].sum()),
        "total_orders": int(df["total_orders"].sum()),
        "total_quantity": float(df["total_quantity"].sum()),
        "total_completed_orders": int(df["completed_orders"].sum()),
    }
