import matplotlib.pyplot as plt

x =["mon","tues","wed",'thur',"friday","sat"]
y=[10,5,41,16,54,38]

plt.plot(x,y)
plt.title("bakery sales over a week")

plt.xlabel("days of a week")
plt.ylabel("sales per day")

plt.show()