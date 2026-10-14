
from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

db_path = BASE_DIR / "data" / "marketing.db"
sql_path = BASE_DIR / "sql" / "campaign_analysis.sql"
output_dir = BASE_DIR / "reports"

output_dir.mkdir(exist_ok=True)

sql_script = sql_path.read_text(encoding="utf-8")

queries = [
    q.strip()
    for q in sql_script.split(";")
    if q.strip()
]

names = [
    "overall_performance",
    "campaign_performance",
    "age_performance",
    "gender_performance",
    "interest_performance"
]

with sqlite3.connect(db_path) as conn:
    for name, query in zip(names, queries):
        result = pd.read_sql_query(query, conn)

        print(f"\n{'=' * 50}")
        print(name.upper())
        print(f"{'=' * 50}")
        print(result.to_string(index=False))

        result.to_csv(
            output_dir / f"{name}.csv",
            index=False
        )

print("\nAll SQL analyses completed successfully!")
