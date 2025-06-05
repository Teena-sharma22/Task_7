import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

a = sqlite3.connect('task7_sales_data.db')

## run only one time ---for create table 
# cursor = a.cursor()

# cursor.execute("""
# create table IF NOT EXISTS sales_dataa ( id Integer primary key autoincrement ,
#  Product text ,Quantity Integer,Price Real)
# """)
# cursor.executemany("""
# insert into sales_dataa (Product,Quantity,Price) values(?,?,?) """,[('Pen', 10, 5),
# ('Pencil', 20, 2),
# ('Notebook', 5, 20),
# ('Pen', 5, 5),
# ('Notebook', 3, 20),
# ('Pencil', 15, 2),
# ('Notebook', 7, 20),
# ('Pen', 12, 5),
# ('Eraser', 25, 1),
# ('Eraser', 10, 1)])
# a.commit()

query = """
SELECT product, SUM(quantity) AS total_quantity, SUM(quantity * price) AS revenue
FROM sales_dataa GROUP BY product
"""

df = pd.read_sql_query(query, a)

# Step 5: Print summary
print("Sales Summary:")
print(df)

query2 = """ 
select * from sales_dataa """
dff = pd.read_sql_query(query2,a)
print (dff)

# Step 6: Plot bar chart of revenue by product
df.plot(kind='bar', x='Product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Step 7: Close the connection
a.close()
