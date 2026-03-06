# Data Dictionary

## fact_financials

| Column         | Description                              |
| -------------- | ---------------------------------------- |
| Financial_ID   | Unique transaction identifier            |
| Date_Key       | Foreign key linking to dim_date          |
| Department_Key | Foreign key linking to dim_department    |
| Product_Key    | Foreign key linking to dim_product       |
| Revenue        | Sales revenue generated                  |
| Cost           | Operational cost associated with revenue |
| Units_Sold     | Number of units sold                     |

---

## dim_date

| Column     | Description            |
| ---------- | ---------------------- |
| Date_Key   | Unique date identifier |
| Date       | Calendar date          |
| Month      | Numeric month value    |
| Month_Name | Name of the month      |
| Quarter    | Fiscal quarter         |
| Year       | Calendar year          |

---

## dim_department

| Column          | Description                           |
| --------------- | ------------------------------------- |
| Department_Key  | Unique department identifier          |
| Department_Name | Department name                       |
| Cost_Type       | Fixed or variable cost classification |

---

## dim_product

| Column        | Description                 |
| ------------- | --------------------------- |
| Product_Key   | Unique product identifier   |
| Product_Name  | Product name                |
| Category      | Product category            |
| Price_Segment | Pricing tier classification |
