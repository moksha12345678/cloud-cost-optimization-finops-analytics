from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parent
df=pd.read_csv(ROOT/'data/cloud_billing_cleaned_synthetic.csv',parse_dates=['billing_month'])
out=ROOT/'outputs'; out.mkdir(exist_ok=True)
df.groupby('department',as_index=False).agg(records=('record_id','count'),total_cost_usd=('monthly_cost_usd','sum'),avg_utilization_pct=('utilization_pct','mean')).to_csv(out/'cost_by_department.csv',index=False)
df.groupby('service',as_index=False).agg(records=('record_id','count'),total_cost_usd=('monthly_cost_usd','sum'),avg_utilization_pct=('utilization_pct','mean')).to_csv(out/'cost_by_service.csv',index=False)
df.groupby(df.billing_month.dt.to_period('M').astype(str),as_index=False).agg(total_cost_usd=('monthly_cost_usd','sum'),records=('record_id','count')).to_csv(out/'monthly_cost_trend.csv',index=False)
flags=df[(df.utilization_pct<20)|(df.resource_status.isin(['Idle','Stopped']))|(df.owner_tag_present=='No')]
flags.to_csv(out/'resources_for_review.csv',index=False)
print(f'{len(df):,} synthetic records analyzed; {len(flags):,} records flagged for human review.')
print('Flags are not confirmed waste or realized savings.')
