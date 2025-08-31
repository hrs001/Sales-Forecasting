# Coffee Shop Revenue & Customer Clustering

This project analyzes **coffee shop daily customer footfall** and uses **KMeans clustering** to identify sales categories:  
- **Low Business Day**  
- **Regular Day**  
- **Peak Day** (holidays/marketing campaigns)

It also estimates **daily revenue** based on pricing and predicts the **average sachet usage** per day.

## Project Workflow
1. Load dataset (`coffee_shop_revenue.csv`).
2. Add **Date column** starting from `2023-01-01`.
3. Convert dates into **day numbers** for clustering.
4. Apply **KMeans clustering** on daily customer count.
5. Label clusters into **Occasions** (Low, Regular, Peak).
6. Plot **cluster visualization**.
7. Calculate **average revenue & sachet usage** for each category.


