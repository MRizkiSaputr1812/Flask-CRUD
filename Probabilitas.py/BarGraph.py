import pandas as pd # Import the pandas library and assign it the alias 'pd'
import matplotlib.pyplot as plt

df = pd.read_csv('/content/Forbes Richest Atheletes.csv')

df.head(20)

# Mengonversi kolom earnings menjadi numerik (jika belum)
df['earnings ($ million)'] = pd.to_numeric(df['earnings ($ million)'], errors='coerce')

# Mengelompokkan data berdasarkan tahun dan menjumlahkan pendapatan
earnings_per_year = df.groupby('Year')['earnings ($ million)'].sum().reset_index()

# Plot bar graph
plt.figure(figsize=(10, 6))
plt.bar(earnings_per_year['Year'], earnings_per_year['earnings ($ million)'], color='skyblue')
plt.xlabel('Year')
plt.ylabel('Total Earnings ($ million)')
plt.title('Total Earnings of Forbes Richest Athletes (1990-2020)')
plt.xticks(rotation=45)
plt.show()