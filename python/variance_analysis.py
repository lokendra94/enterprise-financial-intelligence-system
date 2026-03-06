import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/fact_financials.csv")

print("Dataset Loaded")

# Keep only revenue rows
revenue_df = df[df["Line_Item"] == "Revenue"]

# Separate Actual and Budget
actual = revenue_df[revenue_df["Scenario"] == "Actual"]
budget = revenue_df[revenue_df["Scenario"] == "Budget"]

# Aggregate revenue by department
actual_summary = actual.groupby("Department_Key")["Amount"].sum().reset_index()
budget_summary = budget.groupby("Department_Key")["Amount"].sum().reset_index()

# Rename columns
actual_summary.rename(columns={"Amount": "Actual_Revenue"}, inplace=True)
budget_summary.rename(columns={"Amount": "Budget_Revenue"}, inplace=True)

# Merge datasets
variance = pd.merge(actual_summary, budget_summary, on="Department_Key")

# Calculate variance
variance["Variance"] = variance["Actual_Revenue"] - variance["Budget_Revenue"]
variance["Variance_%"] = (variance["Variance"] / variance["Budget_Revenue"]) * 100

print(variance)

# Save report
variance.to_csv("../data/processed/variance_report.csv", index=False)

print("Variance report saved.")