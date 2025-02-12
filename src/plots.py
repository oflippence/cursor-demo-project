import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("../data/raw/sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Create a bar chart
plt.figure(figsize=(12, 6))
colors = {
    "North": "#7FB7D6",  # deeper pastel blue
    "South": "#92D88C",  # deeper pastel green
    "East": "#E69B9B",  # deeper pastel pink/coral
    "West": "#FFCB8C",  # deeper pastel orange
}

# Plot bars for each region
for region in df["Region"].unique():
    mask = df["Region"] == region
    plt.bar(df[mask]["Date"], df[mask]["Revenue"], label=region, color=colors[region])

# Customize the plot
plt.title("Revenue by Date and Region", fontsize=12)
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.legend(title="Region")
plt.grid(True, alpha=0.3)

# Adjust layout to prevent label cutoff
plt.tight_layout()
plt.show()

# Save the plot
plt.savefig("../data/raw/revenue_by_date_region.png")
plt.close()

print("Plot saved to ../data/raw/revenue_by_date_region.png")
