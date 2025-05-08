import sqlite3
import pandas as pd 

with sqlite3.connect("../db/lesson.db") as conn:
    print("Database connected successfully.")
    
    query = """
    SELECT 
        line_items.line_item_id,
        line_items.quantity,
        line_items.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    """
    
    df = pd.read_sql_query(query, conn)

print(df.head())
df['total'] = df['quantity'] * df['price']
print(df.head())

grouped_df = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
})


grouped_df.rename(columns={
    'line_item_id': 'order_count',
    'total': 'total_sales'
}, inplace=True)


print(grouped_df.head())

grouped_df = grouped_df.sort_values(by='product_name')


grouped_df.to_csv("order_summary.csv")

print("CSV file 'order_summary.csv' has been written to the assignment7 directory.")
print(grouped_df.head())