import matplotlib.pyplot as plt

region=["north","south","east","west"]
revenue=[2000,8000,1500,4000]

plt.pie(revenue,labels=region,autopct="%1.1f%%",colors=["green","red","yellow","orange"])
plt.title("revenue contibution by region")
plt.legend()
plt.show()