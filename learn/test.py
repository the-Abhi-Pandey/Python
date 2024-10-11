# import pandas as pd

# file_path = r'"C:\Users\2186236\OneDrive - Cognizant\Desktop\Target Entity Trend Details 070123 - 063024.xlsx"'
# df1 = pd.read_excel(file_path, sheet_name='DEV')
# df2 = pd.read_excel(file_path, sheet_name='PROD')

# diff_df = df1.compare(df2)
# print(diff_df)



import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate random dates
def random_date(start, end):
    return start + timedelta(days=np.random.randint(0, (end - start).days))

# Parameters
num_rows = 30000
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
order_numbers = [f"SO{70000 + i}" for i in range(num_rows // 10)]
product_keys = np.random.randint(200, 600, size=num_rows)
customer_keys = np.random.randint(10000, 30000, size=num_rows)
territory_keys = np.random.randint(1, 10, size=num_rows)
order_line_items = np.random.randint(1, 5, size=num_rows)
order_quantities = np.random.randint(1, 4, size=num_rows)

# Generate DataFrame
data = {
    "OrderDate": [random_date(start_date, end_date) for _ in range(num_rows)],
    "StockDate": [random_date(start_date - timedelta(days=365), start_date) for _ in range(num_rows)],
    "OrderNumber": np.random.choice(order_numbers, num_rows),
    "ProductKey": product_keys,
    "CustomerKey": customer_keys,
    "TerritoryKey": territory_keys,
    "OrderLineItem": order_line_items,
    "OrderQuantity": order_quantities
}

df = pd.DataFrame(data)
df.to_csv("generated_data_2024.csv", index=False)
print("Data generation complete. File saved as .")

