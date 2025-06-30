import matplotlib.pyplot as plt

data = [1,2,2,3,3,3,4,4,4,4,5,5,6,7,8]

plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.title("Contoh Histogram")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
plt.show()