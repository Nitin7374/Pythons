import seaborn as sns
import matplotlib.pyplot as plt

x =[1,2,3,4,5,6]
y=[2,3,4,7,5,8]

data =sns.load_dataset("penguins")
data
sns.lineplot(x ="x",y ="y", data = data)
plt.show()