
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = BASE_DIR / "data" / "raw" / "conversion_data.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "marketing_cleaned.csv"

# Load dataset
df = pd.read_csv(RAW_FILE)

print("DATASET SHAPE")
print(df.shape)

print("\nFIRST FIVE RECORDS")
print(df.head())

print("\nCOLUMN INFORMATION")
df.info()

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nSUMMARY STATISTICS")
print(df.describe(include="all"))

# Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Remove exact duplicates
df = df.drop_duplicates().copy()

# Convert metric columns to numeric
numeric_cols = [
    "impressions",
    "clicks",
    "spent",
    "total_conversion",
    "approved_conversion",
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Inspect missing numeric values
print("\nMISSING NUMERIC VALUES")
print(df[numeric_cols].isna().sum())

# Remove records missing essential metrics
df = df.dropna(subset=numeric_cols).copy()

# Flag inconsistent metrics
invalid = (
    (df[numeric_cols] < 0).any(axis=1)
    | (df["clicks"] > df["impressions"])
    | (df["approved_conversion"] > df["total_conversion"])
)

print("\nPOTENTIALLY INVALID ROWS:", invalid.sum())

# Exclude invalid rows, preserving raw data
df = df.loc[~invalid].copy()

# Calculate marketing KPIs
df["ctr"] = (
    df["clicks"] / df["impressions"].replace(0, float("nan"))
) * 100

df["cpc"] = (
    df["spent"] / df["clicks"].replace(0, float("nan"))
)

df["lead_conversion_rate"] = (
    df["total_conversion"]
    / df["clicks"].replace(0, float("nan"))
) * 100

df["cost_per_purchase"] = (
    df["spent"]
    / df["approved_conversion"].replace(0, float("nan"))
)

# Ad-level classification target
df["has_approved_conversion"] = (
    df["approved_conversion"] > 0
).astype(int)

# Save cleaned data
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print("\nCLEANED DATASET SHAPE:", df.shape)
print("\nTARGET DISTRIBUTION")
print(df["has_approved_conversion"].value_counts())

print("\nCLEANED DATA SAVED TO:", OUTPUT_FILE)
