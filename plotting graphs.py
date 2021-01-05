# Importing the relevant modules
import matplotlib.pyplot as plt



#
# # Graphs in python
#
# x =[1, 3, 5, 10]
# # plt.plot(x)
# #plt.show() # This will show the plot we are plotting
# # plotting x and y against each other
#
# y = [7, 12, 21, 22]
# plt.plot(x,y)
# #plt.show()
#
# # lets plot a nice looking plot

x = [3, 9, 14]
y = [2, 7, 11]
#Plotting x and y
plt.plot(x, y, c="red", linewidth=2, label="Line1")


#Line 2 - points
x2 = [1, 15, 18]
y2 = [0, 3, 12]
plt.plot(x2,  y2, c="green", linewidth=2, label="Line 2", linestyle="dashed", marker='o', markerfacecolor="black"  )

#Label the axes
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two lines")

#Show the legend
plt.legend()

#Get python to show the plot
plt.show()
