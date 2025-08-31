# Coffee Stall Revenue & Footfall Analysis

## Project Overview
This project analyzes the daily sales and customer footfall data of a coffee stall to identify business patterns, categorize sales days (low, regular, peak), and estimate revenue.  
The analysis uses **clustering (KMeans)**, visualization, and revenue calculations to extract useful business insights.

---

## Dataset
- **File:** `coffee_shop_revenue.csv`
- **Columns included:**
  - `Number_of_Customers_Per_Day`
  - `Average_Order_Value`
  - `Operating_Hours_Per_Day`
  - `Number_of_Employees`
  - `Marketing_Spend_Per_Day`
  - `Location_Foot_Traffic`
  - `Daily_Revenue`

> Quantity of items sold is not provided → we assumed each customer corresponds to **1 order**.  
> Price of a chocolaty cold coffee is fixed at **INR 65 (regular day)** and **INR 60 (peak day discounts/marketing).**

---

## Methodology
1. **Date Assignment**  
   - Starting from `2023-01-01`, each row was assigned a sequential date.

2. **Occasion Categorization**  
   - We created a new column `Occasion` based on clustering (`KMeans`) of daily customer footfall.
   - Clusters mapped into:
     - **Low Business Day**
     - **Regular Day**
     - **Peak Day** (holidays/marketing boosts)

3. **Visualization**  
   - Cluster scatterplot created with:
     - X-axis: Day Number
     - Y-axis: Customers per Day
     - Color-coded clusters with labels

4. **Revenue & Consumption**  
   - Estimated average revenue/day by multiplying customers × average price.  
   - Estimated sachet consumption/day (1 sachet per customer).

---


## Output (Aggregated Results)
- Average customers/day for each occasion
- Estimated revenue/day
- Estimated sachets used/day

---

## Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn (KMeans)

---

## Next Steps
- Add forecasting (ARIMA/Prophet) for future sales prediction
- Evaluate effect of marketing spend vs. footfall
- Explore dynamic pricing models
