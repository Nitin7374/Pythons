import matplotlib.pyplot as plt
 
hours =[1,2,3,4,5,6,7,8]
scores=[45,72,81,61,94,35,58,65]

plt.scatter(hours, scores, color="green", marker="o",label="student data")
plt.xlabel("hours")
plt.ylabel("scores")
plt.title("ranking of students ")
plt.legend()
plt.grid()
plt.show()