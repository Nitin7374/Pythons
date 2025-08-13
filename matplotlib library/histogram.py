import matplotlib.pyplot as plt

scores=[15,45,12,78,62,38,82,49,12,19,67,92]

plt.hist(scores,bins=5, color="purple", edgecolor="black")
plt.xlabel("score range")
plt.ylabel("no. of student")
plt.title("score contribution of students")
plt.show()
