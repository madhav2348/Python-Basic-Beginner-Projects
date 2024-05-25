import matplotlib.pyplot as plt


x= [2,2,4,9,2,7,1]
y= [2,3,6,4,9,1,1]

plt.bar(x,y)

plt.plot(x,y , label ='line1', color ='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue',markersize=12)
plt.ylim(1,8)
plt.ylim(1,8)


x1 = [1,2,3,4,5,6,7]
y1 = [9,8,7,6,5,4,3]
plt.plot(x1,y1, label = 'line 2')


plt.xlabel("x axis")
plt.ylabel("y axis")

plt.title("demo graph")

plt.legend()
plt.show()