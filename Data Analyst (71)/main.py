import pandas as pd

df = pd.read_csv('592 salaries-by-college-major.csv')
print(df.head())


df.shape
df.isna()
clean_df = df.dropna()

a = clean_df['Starting Median Salary'].idxmax()
b = clean_df['Undergraduate Major'].loc[43]

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk.sort_values(by="Mid-Career 90th Percentile Salary", ascending=False).head()

# to change the visualization of the number, better format, like rounding better
pd.options.display.float_format = '{:,.2f}'.format