# Load library
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt


# EDA questions for dataset- Correlation between reward points and total price
# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='SQLNikki272829',
    database='supermarket_sales'
)


query = "SELECT reward_points, total_price FROM supermarket_sales.sales;"
df = pd.read_sql(query, conn)

correlation = df['reward_points'].corr(df['total_price'])

# Print the result
print(f"Correlation between reward points and total price: {round(correlation, 1)}")

# Create a scatter plot for correlation
plt.figure(figsize=(8, 6))
plt.scatter(df['reward_points'], df['total_price'], alpha=0.5, color='blue')
plt.title('Scatter Plot: Reward Points vs Total Price')
plt.xlabel('Reward Points')
plt.ylabel('Total Price')
plt.grid(True)
plt.show()
