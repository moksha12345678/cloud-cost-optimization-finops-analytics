# Cloud Cost Optimization & FinOps Analytics

## Overview
A portfolio project demonstrating cloud-spend analysis using **synthetic, illustrative data**. It examines cost by department and service, monthly spend trends, low-utilization resources, idle/stopped resources, and missing owner tags.

**Data honesty:** This repository uses generated sample data, not real company or cloud-provider records. Flagged resources are candidates for review, not proof of waste. No verified savings percentage is claimed.

## Tools
Python (pandas, NumPy, Matplotlib), SQL, CSV; outputs can be imported into Power BI or Tableau.

## Files
- `data/cloud_billing_raw_synthetic.csv` — raw sample data with intentional missing values
- `data/cloud_billing_cleaned_synthetic.csv` — cleaned dataset
- `analysis_queries.sql` — example SQL queries
- `run_analysis.py` — reproducible analysis script
- `outputs/` — summaries and resources flagged for review
- `charts/` — cost charts
- `outputs/executive_summary.md` — concise findings and next steps

## Run
Install dependencies: `pip install pandas numpy matplotlib`
Then run: `python run_analysis.py`

## Questions
1. Which departments/services have the highest synthetic spend?
2. How does spend change by month?
3. Which resources need review based on low utilization, status, or missing ownership tags?
4. What should be validated before recommending cost reductions?

## Recommendations
Validate flagged resources with service owners, improve owner tagging, investigate unusual monthly changes, and estimate savings only after validating pricing and remediation assumptions.
