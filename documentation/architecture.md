# Data Architecture

## Overview

The project uses a **Star Schema data model**, a common architecture used in data warehouses and business intelligence systems.

This model separates data into:

• Fact tables (transactional data)
• Dimension tables (descriptive attributes)

This design improves query performance and simplifies analytical reporting.

---

## Fact Table

### fact_financials

The fact table stores measurable financial metrics.

Key metrics include:

• Revenue
• Cost
• Units Sold

Each record represents financial performance for a specific date, department, and product.

---

## Dimension Tables

### dim_date

Stores calendar information.

Attributes include:

• Date
• Month
• Quarter
• Year
• Fiscal Period Indicator

---

### dim_department

Contains department level information.

Attributes include:

• Department Name
• Cost Type (Fixed or Variable)

---

### dim_product

Contains product related information.

Attributes include:

• Product Name
• Product Category
• Price Segment

---

## Relationships

The model uses **one-to-many relationships**:

dim_date → fact_financials
dim_department → fact_financials
dim_product → fact_financials

Filtering flows from dimension tables to the fact table.

This ensures efficient aggregation and accurate calculations.

---

## Benefits of Star Schema

• Simplified queries
• Faster reporting performance
• Scalable architecture
• Reduced data redundancy
