-- Synthetic FinOps sample data; import cleaned CSV as cloud_billing.
SELECT department, ROUND(SUM(monthly_cost_usd),2) AS total_cost_usd
FROM cloud_billing GROUP BY department ORDER BY total_cost_usd DESC;

SELECT service, ROUND(SUM(monthly_cost_usd),2) AS total_cost_usd,
       ROUND(AVG(utilization_pct),1) AS avg_utilization_pct
FROM cloud_billing GROUP BY service ORDER BY total_cost_usd DESC;

SELECT resource_id, department, service, region, monthly_cost_usd,
       utilization_pct, resource_status, owner_tag_present
FROM cloud_billing
WHERE utilization_pct < 20 OR resource_status IN ('Idle','Stopped')
   OR owner_tag_present = 'No'
ORDER BY monthly_cost_usd DESC;

SELECT strftime('%Y-%m', billing_month) AS billing_month,
       ROUND(SUM(monthly_cost_usd),2) AS total_cost_usd
FROM cloud_billing GROUP BY strftime('%Y-%m', billing_month)
ORDER BY billing_month;
