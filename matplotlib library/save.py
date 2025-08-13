import matplotlib.pyplot as plt

fig, ax= plt.subplots(1,2, figsize=(10,5))

x =[1,2,3,4]
y =[10,20,30,40]

ax[0].plot(x,y,label="data", color="green")
ax[0].set_title("line chart")


ax[1].bar(x,y,label="data",color="orange")
ax[1].set_title("bar chart")
fig.suptitle("compare of line and bar chart")
plt.legend()
plt.tight_layout()

# saving the file
plt.savefig("student data.png",dpi=300,bbox_inches="tight")

plt.show()

