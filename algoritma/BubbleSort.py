import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def bubble_sort(arr):
    steps = []
    color_steps = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            colors = ["blue"] * n
            colors[j] = "green"    # Elemen yang dibandingkan diberi warna hijau
            colors[j + 1] = "green"
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            steps.append(arr.copy())
            color_steps.append(colors)
    return steps, color_steps

data = np.arange(1, 101)
np.random.shuffle(data)
steps, color_steps = bubble_sort(data)

fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(data)), steps[0], color=color_steps[0], align="edge")

ax.set_xlim(0, len(data))
ax.set_ylim(0, int(1.1 * max(data)))

def update_plot(frame, rects, steps, color_steps):
    array = steps[frame]
    colors = color_steps[frame]
    for rect, val, color in zip(rects, array, colors):
        rect.set_height(val)
        rect.set_color(color)

anim = animation.FuncAnimation(fig, func=update_plot, fargs=(bar_rects, steps, color_steps),
                               frames=len(steps), interval=1, repeat=False)

plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Bubble Sort Visualization with Highlighted Swaps")
plt.show()
