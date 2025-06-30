import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
data = pd.read_csv("/content/coffee_shop_revenue.csv")

# Memilih kolom numerik
numeric_columns = data.select_dtypes(include=['number']).columns

# Membuat histogram untuk setiap kolom numerik
for col in numeric_columns:
    plt.figure(figsize=(8, 5))

    mean_val = np.mean(data[col])
    median_val = np.median(data[col])

    sns.histplot(data[col], bins=10, kde=True, color='lightblue', edgecolor='black', stat='count', alpha=0.6)

    plt.axvline(mean_val, color='green', linestyle='dotted', linewidth=2, label=f'Mean = {mean_val:.2f}')
    plt.axvline(median_val, color='red', linestyle='dashed', linewidth=2, label=f'Median = {median_val:.2f}')

    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()