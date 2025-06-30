import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load dataset
file_path = "/content/coffee_shop_revenue_cleaned.xlsx"
data = pd.read_excel(file_path, sheet_name="Sheet1")

# Define variable pairs with strong correlation
variable_pairs = [
    ("Number Of Customers Per Day", "Daily Revenue"),
    ("Average Order Value", "Daily Revenue"),
    ("Marketing Spend Per Day", "Daily Revenue")
]

# Define colors for plots
colors = ["blue", "green", "orange"]

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

for i, (x_var, y_var) in enumerate(variable_pairs):
    ax = axes[i]
    sns.regplot(x=data[x_var], y=data[y_var], ax=ax,
                scatter_kws={"alpha": 0.5, "color": colors[i]},
                line_kws={"color": "red"})

    # Calculate correlation
    corr, _ = pearsonr(data[x_var], data[y_var])
    ax.text(0.05, 0.95, f"Correlation: {corr:.2f}", transform=ax.transAxes, fontsize=12, verticalalignment='top')

    # Set labels and title
    ax.set_xlabel(x_var)
    ax.set_ylabel(y_var)
    ax.set_title(f"{x_var} vs {y_var}")

# Overall title
plt.suptitle("Scatter Plot of Highly Correlated Variables", fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()