import pandas as pd

data = {
    'Product': ['A', 'B', 'C'],
    'Price': [10.99, 23.50, 7.95],
    'Quantity': [100, 60, 150]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print DataFrame
print("DataFrame:")
print(df)

# Add a new column for Total Sales
df['Total'] = df['Price'] * df['Quantity']

# Print the updated DataFrame
print("\nWith Total Sales:")
print(df)
