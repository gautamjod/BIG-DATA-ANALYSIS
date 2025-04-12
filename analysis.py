import dask.dataframe as dd

df=dd.read_csv('Cleaned.csv')

print("\nTotal Sales:",round(df['Amount'].sum().compute(),2))
print("\nAverage Rating:",round(df['Review'].mean().compute(),2))
print("\nTotal Orders:",df['CustomerID'].count().compute())

print("\nTop 5 Purchased Item By Quantity",df["Item"].value_counts().head(5))

print("\nTop 5 Purchased Item By Amount")
print(df.groupby("Item")["Amount"].sum().compute().nlargest(5))


print("\nTotal Sales by Month:")
print(df.groupby("Month")['Amount'].sum().compute().sort_values(ascending=False))

print("\nTop 5 CustomerID by Spend")
print(df.groupby("CustomerID")["Amount"].sum().compute().nlargest(5))

print("\nAverage Review By Item")
print(df.groupby("Item")['Review'].mean().compute().sort_values(ascending=False).nlargest(5))

print("\nTop 5 consistence Spender")
print(df.groupby("CustomerID")["Amount"].std().compute().nlargest(5))


combined = df[['CustomerID', 'Amount', 'Review']].dropna().compute()
low_review_high_spend = combined.groupby('CustomerID').agg({'Amount': 'sum', 'Review': 'mean'})
sensitive_cust=low_review_high_spend[(low_review_high_spend['Amount']>df["Amount"].mean()) & (low_review_high_spend['Review']<df["Review"].mean())]
print("\nSensitive Customers")

repeatcust=df["CustomerID"].value_counts().compute().nlargest(5)
print("Top 5 Repeat Customers\n",repeatcust)
