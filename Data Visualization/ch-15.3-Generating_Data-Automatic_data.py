# Calculating Data Automatically

import matplotlib.pyplot as plt

# using loop to plot squares of numbers from 1 to 1000

x_val = range(1, 21)
y_val = [(x**2) for x in x_val]     # syntax:: for x in x_val: return x**2

ax = plt.subplot()

plt.plot(x_val, y_val, color = 'red')
plt.scatter(x_val, y_val, color='blue',)         
# to colour the plot, pass 'color' argument with colour name in quotation
# to pass custom rgb color- color=(r_val, g_val, b_val)


# Set the range for each axis.
ax.axis([0, 20, 0, 400])        #=> ax.axis(min_x_val, max_x_val, min_y_val, max_y_val)

ax.ticklabel_format(style='plain')      # tick-label styling function

# plt.show()


## Using a Colormap: A colormap is a sequence of colors in a gradient that moves from a starting to an ending color. 
# light colour indicates low value and darker value indicates higher value 

ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Blues)
# c argument is used to assign sequence of colors with sequence mapping
# then we pass colormap to use with the cmap argument

plt.show()



## Saving Your Plots Automatically: directly save plots instead of displaying

plt.savefig('squares_plot.png')
# plt.savefig('folderName/fileName.extension', 'arg to trim extra white space')

