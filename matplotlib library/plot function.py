import matplotlib.pyplot as plt

months =[1,2,3,4,5]
sales=[1000,500,2000,1500,100]

plt.plot(months,sales, color="green",linewidth="1",linestyle="--",marker="o",label="2025 sales data")
plt.xlabel("months")
plt.ylabel("sales per months")
plt.title("2025 sales data")
plt.legend()
plt.grid(color="red",linestyle=":")
plt.xticks([1,2,3,4,5],["m1","m2","m3","m4","m5"])

plt.show()
