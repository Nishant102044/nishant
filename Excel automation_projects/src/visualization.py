import matplotlib.pyplot as plt

def category_sales_chart(df):

    summary = df.groupby("Product_Category")["Sales_Amount"].sum()

    summary.plot(kind="bar")

    plt.title("Category Wise Sales")

    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig("Reports/category_sales.png")

    plt.show()