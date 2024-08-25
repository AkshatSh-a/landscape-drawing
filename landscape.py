import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()

from matplotlib.colors import LinearSegmentedColormap

colors = ["#FF4500", "#FFA07A", "#87CEEB"]
cmap = LinearSegmentedColormap.from_list("sunset", colors)

for i in range(100):
    ax.fill_between([0,12], i*0.07, (i+1)*0.07, color=cmap(i/100))

mountain1 = np.array([[0,0], [2,5], [4,0]])
mountain2 = np.array([[3, 0], [5, 4], [7, 0]])
mountain3 = np.array([[6, 0], [9, 6], [12, 0]])

ax.fill(mountain1[:,0], mountain1[:,1], 'darkgreen', edgecolor='black', linewidth=2)
ax.fill(mountain2[:,0], mountain2[:,1], 'green', edgecolor='black', linewidth=2)
ax.fill(mountain3[:,0], mountain3[:,1], 'forestgreen', edgecolor='black', linewidth=2)

snow_cap1 = np.array([[1.7, 5], [2, 5.3], [2.3, 5]])
snow_cap2 = np.array([[4.4, 4], [5, 4.4], [5.6, 4]])
snow_cap3 = np.array([[8.3, 6], [9, 6.4], [9.7, 6]])

ax.fill(snow_cap1[:,0], snow_cap1[:,1], "white", edgecolor="black", linewidth=1)
ax.fill(snow_cap2[:,0], snow_cap2[:,1], "white", edgecolor="black", linewidth=1)
ax.fill(snow_cap3[:,0], snow_cap3[:,1], "white", edgecolor="black", linewidth=1)

sun = plt.Circle((6, 3.5), 0.8, color="#FFD700", alpha=0.8)
ax.add_patch(sun)

def draw_tree(x,y, size):
    trunk_width = size * 0.2
    trunk_height = size * 0.3
    tree_top = np.array([[x,y],[x-size/2,y - size], [x+size/2, y-size]])
    ax.fill(tree_top[:,0], tree_top[:,1], 'darkgreen',edgecolor='black')
    ax.add_patch(plt.Rectangle((x-trunk_width/2, y-size-trunk_height), trunk_width,trunk_height, color='saddlebrown'))


draw_tree(1.5,1,0.8)
draw_tree(3,1.2,1.0)
draw_tree(6,1.0,0.7)
draw_tree(0.5,1.3,0.9)
draw_tree(10,1,0.6)

def draw_cloud(x,y, size_x, size_y):
    cloud = plt.Circle((x,y), size_x, color= 'white', alpha=0.8)
    ax.add_patch(cloud)
    ax.add_patch(plt.Circle((x-size_x*0.7, y), size_y*0.8, color="white", alpha=0.8))
    ax.add_patch(plt.Circle((x + size_x * 0.7, y), size_y * 0.8, color="white", alpha=0.8))
    ax.add_patch(plt.Circle((x, y - size_y * 0.7), size_y * 0.8, color="white", alpha=0.8))


draw_cloud(3,5.5,0.8,0.5)
draw_cloud(7,6.2,1.0,0.6)
draw_cloud(10.5,5.8,0.9,0.5)

ax.set_xticks([])
ax.set_yticks([])

ax.set_xlim([0,12])
ax.set_ylim([0, 7])

plt.show()
