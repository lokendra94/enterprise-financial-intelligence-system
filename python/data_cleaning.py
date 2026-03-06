import pandas as pd

# Load raw financial dataset
df = pd.read_csv("../data/raw/fact_financials.csv")

print("Dataset Loaded")

# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Convert date column if needed
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])

# Save cleaned dataset
df.to_csv("../data/processed/cleaned_financials.csv", index=False)

print("Cleaned dataset saved in processed folder")