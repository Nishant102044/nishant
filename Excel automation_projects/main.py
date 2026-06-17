<<<<<<< HEAD
from src.clean_data import clean_data
from src.generate_report import generate_report
from src.visualization import category_sales_chart

file_path = "data/Sales_data.xlsx"

# Clean Data
df = clean_data(file_path)

# Generate Report
report = generate_report(df)

# Create Chart
category_sales_chart(df)

print(report)

=======
from src.clean_data import clean_data
from src.generate_report import generate_report
from src.visualization import category_sales_chart

file_path = "data/Sales_data.xlsx"

# Clean Data
df = clean_data(file_path)

# Generate Report
report = generate_report(df)

# Create Chart
category_sales_chart(df)

print(report)

>>>>>>> 6442826c615e90312781ce7636378122ee1c4d54
print("Project Completed Successfully")