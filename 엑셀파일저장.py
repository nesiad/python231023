import openpyxl
import random

# Create a new workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Create the header row
header = ["ID", "Name", "Quantity", "Price"]
sheet.append(header)

# Generate 100 rows of sales data
for _ in range(100):
    product_id = random.randint(1000, 9999)
    product_name = f"Product {product_id}"
    quantity = random.randint(1, 10)
    price = round(random.uniform(10, 1000), 2)

    row_data = [product_id, product_name, quantity, price]
    sheet.append(row_data)

# Save the workbook to the specified location
workbook.save(r'C:\work\sales.xlsx')

print("Sales list generated and saved to C:\work\sales.xlsx")
