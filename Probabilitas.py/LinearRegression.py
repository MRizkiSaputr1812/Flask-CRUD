import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# Membaca file Excel
df = pd.read_excel("/content/coffee_shop_revenue_cleaned.xlsx")

# Fungsi untuk membuat scatter plot dengan regresi linear
def plot_regression(x_col, y_col, xlabel, title):
    X = df[[x_col]].values
    y = df[y_col].values

    # Membuat model regresi linear
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Menyimpan koefisien dan intercept
    b1 = model.coef_[0]
    b0 = model.intercept_
    regression_equation = f'y = {b1:.2f}x + {b0:.2f}'

    # Menentukan prediksi min dan max
    x_min = X.min()  # Or min(X.flatten())
    x_max = X.max()  # Or max(X.flatten())
    y_min_pred = model.predict([[x_min]])
    y_max_pred = model.predict([[x_max]])

    # Plot scatter plot dan garis regresi
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=X.flatten(), y=y, label='Actual Data', color='blue')
    plt.plot(X.flatten(), y_pred, color='red', label='Regression Line')

    # Menambahkan garis error (green lines)
    for i in range(len(X)):
        plt.plot([X[i], X[i]], [y[i], y_pred[i]], color='green', linestyle='--', alpha=0.6)

    # Menambahkan teks persamaan regresi pada grafik
    plt.text(min(X), max(y), regression_equation, fontsize=12, color='red',
             bbox=dict(facecolor='white', alpha=0.5))

    # Menambahkan label dan judul
    plt.xlabel(xlabel)
    plt.ylabel('Daily Revenue')
    plt.title(title)
    plt.legend()
    plt.show()

    # Menampilkan koefisien, intercept, dan prediksi min/max
    print(f'Persamaan regresi untuk {xlabel}: {regression_equation}')
    print(f'Koefisien regresi (b1): {b1:.2f}')
    print(f'Intercept (b0): {b0:.2f}')
    print(f'Prediksi nilai minimum: {y_min_pred[0]:.2f}')
    print(f'Prediksi nilai maksimum: {y_max_pred[0]:.2f}')


# Plot regresi untuk "Number Of Customers Per Day" vs "Daily Revenue"
plot_regression('Number Of Customers Per Day', 'Daily Revenue', 'Number Of Customers Per Day', 'Linear Regression: Customers vs Revenue with Error Lines')

# Plot regresi untuk "Average Order Value" vs "Daily Revenue"
plot_regression('Average Order Value', 'Daily Revenue', 'Average Order Value', 'Linear Regression: Average Order Value vs Revenue with Error Lines')

# Plot regresi untuk "Marketing Spend Per Day" vs "Daily Revenue"
plot_regression('Marketing Spend Per Day', 'Daily Revenue', 'Marketing Spend Per Day', 'Linear Regression: Marketing Spend vs Revenue with Error Lines')
