import matplotlib.pyplot as plt

product =["A","B","C","D"]
sales=[1000,500,4000,2000]

plt.bar(product,sales,color="skyblue",label="sales 2025")
plt.xlabel("product")
plt.ylabel("sales")
plt.title("product sales comparesion")
plt.legend()
plt.show()