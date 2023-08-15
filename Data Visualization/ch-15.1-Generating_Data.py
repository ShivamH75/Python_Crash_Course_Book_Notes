# Data analysis uses code to explore the patterns and connections in a dataset.

# matplotlib - mathematical plotting library

# Plotly package -  generates visualizations that automatically resize to fit a variety of display devices. 


# installing matplotlib - pip install matplotlib -U    #install latest version

# type of visualizations - https://matplotlib.org/stable/plot_types/index.html

## 1. Plotting a Simple Line Graph
import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
cubes = [1,8,27,64,125]


fig, ax = plt.subplots()
# The variable fig represents the entire figure, which is the collection of plots that are generated.
# subplot() function can generate one or multiple plots in same figure.
# ax.plot(squares)
# ax represents single plot

# plt.show()
# function plt.show() opens Matplotlib’s viewer and displays the plot

# customize plot
# 1. thickness of a line 
# ax.plot(squares, linewidth=3)

# 2. Set chart title and label axes.
ax.set_title("Squares Plot", fontsize=24)
ax.set_xlabel("Numbers")
ax.set_ylabel("Square of the numbers")

# 3. Set size of tick labels
ax.tick_params(labelsize=16)

# plt.show()

# important parameters
# linewidth
# fontsize
# labelsize

# NOTE: the plot starts from 0 on x-axis, so incorrect values are seen against y
# so we need to provide x-coordinates also 
values = [1,2,3,4,5]
ax.plot(values, squares, linewidth=2)
ax.plot(values, cubes, linewidth=2)

plt.show()

