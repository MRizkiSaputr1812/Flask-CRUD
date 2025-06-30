import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
file_path = '/content/Forbes Richest Atheletes.csv'
df = pd.read_csv(file_path)

# Filter data untuk tahun 2010-2020
df = df[(df['Year'] >= 2010) & (df['Year'] <= 2020)]

# Mengatur ukuran plot
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

# Boxplot pendapatan atlet per tahun
boxplot = sns.boxplot(x='Year', y='earnings ($ million)', data=df)
plt.title('Box Plot Distribusi Pendapatan Atlet per Tahun (2010-2020)')
plt.xticks(rotation=45)

# Menambahkan deviasi dan kuartil
for year in df['Year'].unique():
    data = df[df['Year'] == year]['earnings ($ million)']
    q1 = data.quantile(0.25)
    q2 = data.median()
    q3 = data.quantile(0.75)
    std = data.std()
    plt.text(year-2010, q1, f'Q1: {q1:.2f}', horizontalalignment='center', size='small', color='blue')
    plt.text(year-2010, q2, f'Q2: {q2:.2f}', horizontalalignment='center', size='small', color='green')
    plt.text(year-2010, q3, f'Q3: {q3:.2f}', horizontalalignment='center', size='small', color='orange')
    plt.text(year-2010, q3 + std, f'STD: {std:.2f}', horizontalalignment='center', size='small', color='red')

# Menampilkan plot
plt.tight_layout()
plt.show()