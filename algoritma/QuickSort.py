import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def quick_sort(arr, start, end, steps, color_steps):
    if start < end:
        pivot_index = partition(arr, start, end, steps, color_steps)
        quick_sort(arr, start, pivot_index - 1, steps, color_steps)
        quick_sort(arr, pivot_index + 1, end, steps, color_steps)

def partition(arr, start, end, steps, color_steps):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        colors = ["blue"] * len(arr)
        colors[j] = "green"      # Elemen yang sedang dibandingkan diberi warna hijau
        colors[end] = "red"      # Pivot ditandai dengan warna merah
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        steps.append(arr.copy())
        color_steps.append(colors)
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    steps.append(arr.copy())
    color_steps.append(["blue"] * len(arr))  # Reset warna setelah langkah selesai
    return i + 1

# Data acak unik dari 1 hingga 100
data = np.arange(1, 101)
np.random.shuffle(data)
steps = []
color_steps = []
quick_sort(data, 0, len(data) - 1, steps, color_steps)

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

# Interval 50 ms untuk animasi yang lebih cepat
anim = animation.FuncAnimation(fig, func=update_plot, fargs=(bar_rects, steps, color_steps),
                               frames=len(steps), interval=50, repeat=False)

plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Quick Sort Visualization with Highlighted Partitions")
plt.show()

