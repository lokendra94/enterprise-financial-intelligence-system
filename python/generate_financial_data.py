import pandas as pd
import numpy as np

np.random.seed(42)

# ==========================================
# 1️⃣ DATE DIMENSION
# ==========================================

dates = pd.date_range(start="2022-01-01", end="2024-12-01", freq="MS")

dim_date = pd.DataFrame({"Date": dates})
dim_date["Date_Key"] = dim_date["Date"].dt.year * 100 + dim_date["Date"].dt.month
dim_date["Year"] = dim_date["Date"].dt.year
dim_date["Month"] = dim_date["Date"].dt.month
dim_date["Month_Name"] = dim_date["Date"].dt.strftime("%B")
dim_date["Quarter"] = "Q" + dim_date["Date"].dt.quarter.astype(str)
dim_date["Is_Fiscal_Period"] = 1  # Simplified assumption

# ==========================================
# 2️⃣ PRODUCT DIMENSION
# ==========================================

products = {
    101: {"name": "Smart Home Device", "base_units": 800, "price": 5000, "cogs": 3000, "category": "Smart Home", "segment": "Premium"},
    102: {"name": "Wearables", "base_units": 1200, "price": 3000, "cogs": 1700, "category": "Wearable Tech", "segment": "Mid"},
    103: {"name": "Accessories", "base_units": 2000, "price": 1000, "cogs": 400, "category": "Accessories", "segment": "Economy"},
    104: {"name": "Enterprise IoT", "base_units": 400, "price": 9000, "cogs": 5500, "category": "IoT Solutions", "segment": "Premium"},
}

dim_product = pd.DataFrame([
    [pid, p["name"], p["category"], p["segment"]]
    for pid, p in products.items()
], columns=["Product_Key", "Product_Name", "Category", "Price_Segment"])

# ==========================================
# 3️⃣ DEPARTMENT DIMENSION
# ==========================================

departments = [
    (1, "Sales", "Variable"),
    (2, "Marketing", "Variable"),
    (3, "Manufacturing", "Variable"),
    (4, "Supply Chain", "Variable"),
    (5, "R&D", "Fixed"),
    (6, "Customer Support", "Fixed"),
    (7, "Finance & Admin", "Fixed"),
    (8, "IT", "Fixed"),
]

dim_department = pd.DataFrame(departments,
                              columns=["Department_Key", "Department_Name", "Cost_Type"])

# ==========================================
# 4️⃣ UNIFIED FACT TABLE
# ==========================================

seasonality = {
    1: 0.90, 2: 0.95, 3: 1.00,
    4: 1.05, 5: 1.10, 6: 1.15,
    7: 1.05, 8: 1.00, 9: 0.95,
    10: 1.10, 11: 1.25, 12: 1.40
}

rows = []
financial_id = 1

for date in dates:
    date_key = date.year * 100 + date.month
    year_growth = (date.year - 2022) * 0.08
    season_factor = seasonality[date.month]

    for pid, details in products.items():

        # ----- Generate Units -----
        units = (
            details["base_units"]
            * (1 + year_growth)
            * season_factor
            * np.random.uniform(0.95, 1.05)
        )

        revenue = units * details["price"]
        cogs = units * details["cogs"] * np.random.uniform(0.97, 1.03)

        # ===== ACTUAL =====
        rows.append([financial_id, date_key, 1, pid, "Actual", "Revenue", round(revenue, 2), round(units)])
        financial_id += 1

        rows.append([financial_id, date_key, 3, pid, "Actual", "COGS", round(cogs, 2), None])
        financial_id += 1

        # ===== BUDGET =====
        rows.append([financial_id, date_key, 1, pid, "Budget", "Revenue", round(revenue * 1.05, 2), round(units * 1.07)])
        financial_id += 1

        rows.append([financial_id, date_key, 3, pid, "Budget", "COGS", round(cogs * 0.97, 2), None])
        financial_id += 1

        # ===== FORECAST (Rolling style proxy) =====
        forecast_revenue = revenue * np.random.uniform(0.98, 1.06)

        rows.append([financial_id, date_key, 1, pid, "Forecast", "Revenue", round(forecast_revenue, 2), None])
        financial_id += 1

    # ----- Operating Expense (Department-level, no product link) -----
    base_opex = 2_000_000 * (1 + (date.year - 2022) * 0.05)

    for dept in dim_department["Department_Key"]:
        fluctuation = np.random.uniform(0.9, 1.1)
        expense = base_opex * fluctuation / len(dim_department)

        # Actual OPEX
        rows.append([financial_id, date_key, dept, None, "Actual", "Operating_Expense", round(expense, 2), None])
        financial_id += 1

        # Budget OPEX
        rows.append([financial_id, date_key, dept, None, "Budget", "Operating_Expense", round(expense * 0.95, 2), None])
        financial_id += 1

        # Forecast OPEX
        rows.append([financial_id, date_key, dept, None, "Forecast", "Operating_Expense", round(expense * np.random.uniform(0.95,1.05), 2), None])
        financial_id += 1


fact_financials = pd.DataFrame(rows, columns=[
    "Financial_ID",
    "Date_Key",
    "Department_Key",
    "Product_Key",
    "Scenario",
    "Line_Item",
    "Amount",
    "Units_Sold"
])

# ==========================================
# 5️⃣ SAVE FILES
# ==========================================

dim_date.to_csv("../data_raw/dim_date.csv", index=False)
dim_product.to_csv("../data_raw/dim_product.csv", index=False)
dim_department.to_csv("../data_raw/dim_department.csv", index=False)
fact_financials.to_csv("../data_raw/fact_financials.csv", index=False)

print("Unified Enterprise Financial Dataset Generated Successfully.")