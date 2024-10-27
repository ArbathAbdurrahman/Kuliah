import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def selection_sort(arr):
    steps = []
    color_steps = []  # Menyimpan warna setiap batang di setiap langkah
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Simpan data langkah dan warna batang
        steps.append(arr.copy())
        colors = ["blue"] * len(arr)  # Semua batang berwarna biru secara default
        colors[i] = "red"           # Batang yang sedang berpindah diberi warna hijau
        colors[min_index] = "green"    # Batang yang ditukar juga diberi warna hijau
        color_steps.append(colors)
    return steps, color_steps

# Data acak unik dari 1 hingga 100
data = np.arange(1, 101)  # Buat array [1, 2, ..., 100]
np.random.shuffle(data)    # Acak urutan angka dalam array
steps, color_steps = selection_sort(data)

fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(data)), steps[0], color=color_steps[0], align="edge")

ax.set_xlim(0, len(data))
ax.set_ylim(0, int(1.1 * max(data)))

def update_plot(frame, rects, steps, color_steps):
    array = steps[frame]         # Mendapatkan array pada langkah saat ini
    colors = color_steps[frame]   # Mendapatkan warna untuk langkah saat ini
    for rect, val, color in zip(rects, array, colors):
        rect.set_height(val)      # Memperbarui tinggi batang
        rect.set_color(color)     # Memperbarui warna batang

# Interval 50 ms untuk animasi yang lebih cepat
anim = animation.FuncAnimation(fig, func=update_plot, fargs=(bar_rects, steps, color_steps),
                               frames=len(steps), interval=100, repeat=False)

plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Selection Sort Visualization with Highlighted Swaps")
plt.show()
