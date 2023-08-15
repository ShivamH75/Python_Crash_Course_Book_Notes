import matplotlib.pyplot as plt

# Using Built-in Styles.
# styles contain a variety of default settings for background colors, gridlines, line widths, fonts, font sizes, and more. 
print(plt.style.available)              # to check list of available styles


values = [1,2,3,4,5]
squares = [1,4,9,16,25]
cubes = [1,8,27,64,125]

plt.style.use('seaborn')            # mention the stylename here
ax = plt.subplot()
# mention style name should always declare before subplot function

# ax.plot(x_values, y_values)           -> will plot line graph
# ax.scatter(x_values, y_values)        -> will plot scatter points graph

# plt.show()


## Plotting and Styling Individual Points with scatter()

# ax.scatter(2, 4, s=200)        #mention the x,y co-ordinates of point 
# s argument to set the size of the dots used to draw the graph 
# plt.show()


## Plotting a Series of Points with scatter()
# ax.scatter(x_values, y_values) 
ax.scatter(values, squares) 
plt.show()