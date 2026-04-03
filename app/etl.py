import json
from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/products_100.csv")
OUTPUT_PATH = Path("output/results.json")


def extract_data():
    df = pd.read_csv(DATA_PATH)
    return df


def transform_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    df = df.dropna(subset=["price", "quantity"])
    return df


def analyze_data(df):
    top_5_expensive = (
        df.sort_values(by="price", ascending=False)
        .head(5)[["id", "name", "price", "quantity", "category"]]
        .to_dict(orient="records")
    )

    category_counts = df["category"].value_counts().to_dict()

    stats = {
        "total_products": int(len(df)),
        "average_price": float(df["price"].mean()),
        "max_price": float(df["price"].max()),
        "min_price": float(df["price"].min()),
        "total_quantity": int(df["quantity"].sum()),
        "products_per_category": category_counts,
        "top_5_most_expensive": top_5_expensive,
    }

    return stats


def load_data(stats):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4, ensure_ascii=False)


def run_etl():
    df = extract_data()
    cleaned_df = transform_data(df)
    stats = analyze_data(cleaned_df)
    load_data(stats)
    return stats


if __name__ == "__main__":
    results = run_etl()
    print(json.dumps(results, indent=4, ensure_ascii=False))