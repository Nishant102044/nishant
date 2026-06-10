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

print("Project Completed Successfully")