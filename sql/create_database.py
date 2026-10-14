
from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

csv_path = BASE_DIR / "data" / "processed" / "marketing_cleaned.csv"
db_path = BASE_DIR / "data" / "marketing.db"

df = pd.read_csv(csv_path)

with sqlite3.connect(db_path) as conn:
    df.to_sql(
        "marketing_campaigns",
        conn,
        if_exists="replace",
        index=False
    )

    result = pd.read_sql_query(
        "SELECT COUNT(*) AS total_records FROM marketing_campaigns",
        conn
    )

print("Database created successfully!")
print(result)
print(f"Database location: {db_path}")
