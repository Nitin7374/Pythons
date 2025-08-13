import matplotlib.pyplot as plt
 
plt.scatter([1,2,3], [40,50,60], color="orange", label="class A")
plt.scatter([1,2,3], [48,68,70], color="green", label="class B")


plt.xlabel("hours")
plt.ylabel("scores")
plt.title("ranking of students ")
plt.legend()
plt.grid()
plt.show()