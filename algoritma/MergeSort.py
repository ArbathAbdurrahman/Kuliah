import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def merge(arr, left, mid, right, steps, color_steps):
    temp_arr = arr.copy()
    colors = ["lightblue"] * len(arr)
    for i in range(left, right + 1):
        colors[i] = "yellow"
    steps.append(temp_arr.copy())
    color_steps.append(colors.copy())
    
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < n1 and j < n2:
        colors = ["lightblue"] * len(arr)
        for idx in range(left, right + 1):
            colors[idx] = "yellow"
            
        if L[i] <= R[j]:
            arr[k] = L[i]
            colors[k] = "green"
            i += 1
        else:
            arr[k] = R[j]
            colors[k] = "green"
            j += 1
        k += 1
        steps.append(arr.copy())
        color_steps.append(colors.copy())

    while i < n1:
        colors = ["lightblue"] * len(arr)
        for idx in range(left, right + 1):
            colors[idx] = "yellow"
        arr[k] = L[i]
        colors[k] = "green"
        i += 1
        k += 1
        steps.append(arr.copy())
        color_steps.append(colors.copy())

    while j < n2:
        colors = ["lightblue"] * len(arr)
        for idx in range(left, right + 1):
            colors[idx] = "yellow"
        arr[k] = R[j]
        colors[k] = "green"
        j += 1
        k += 1
        steps.append(arr.copy())
        color_steps.append(colors.copy())
    
    colors = ["lightblue"] * len(arr)
    for i in range(left, right + 1):
        colors[i] = "purple"
    steps.append(arr.copy())
    color_steps.append(colors.copy())

def merge_sort(arr, left, right, steps, color_steps):
    if left < right:
        colors = ["lightblue"] * len(arr)
        for i in range(left, right + 1):
            colors[i] = "red"
        steps.append(arr.copy())
        color_steps.append(colors.copy())
        
        mid = (left + right) // 2
        merge_sort(arr, left, mid, steps, color_steps)
        merge_sort(arr, mid + 1, right, steps, color_steps)
        merge(arr, left, mid, right, steps, color_steps)

class MergeSortVisualizer:
    def __init__(self, array_size=30):
        self.array_size = array_size
        self.setup_data()
        self.setup_plot()
        
    def setup_data(self):
        np.random.seed(42)
        self.data = np.random.randint(1, 100, size=self.array_size)
        self.steps = []
        self.color_steps = []
        self.steps.append(self.data.copy())
        self.color_steps.append(["lightblue"] * len(self.data))
        merge_sort(self.data.copy(), 0, len(self.data) - 1, self.steps, self.color_steps)
        
    def setup_plot(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.bar_rects = self.ax.bar(range(len(self.data)), self.steps[0],
                                    color=self.color_steps[0], align="edge")
        
        self.ax.set_xlim(0, len(self.data))
        self.ax.set_ylim(0, int(1.1 * max(self.data)))
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Value")
        self.ax.set_title("Merge Sort Visualization")
        
        self.text = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)
        
        # Add legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='lightblue', label='Unsorted'),
            Patch(facecolor='red', label='Current Subarray'),
            Patch(facecolor='yellow', label='Merging'),
            Patch(facecolor='green', label='Current Element'),
            Patch(facecolor='purple', label='Sorted Subarray')
        ]
        self.ax.legend(handles=legend_elements, loc='upper right')
        
    def update(self, frame):
        # Update bar heights and colors
        for rect, val, color in zip(self.bar_rects, self.steps[frame], self.color_steps[frame]):
            rect.set_height(val)
            rect.set_color(color)
        self.text.set_text(f'Step: {frame}/{len(self.steps)-1}')
        # Convert list to tuple for matplotlib 3.9.0
        return tuple(list(self.bar_rects) + [self.text])
    
    def run_animation(self):
        anim = animation.FuncAnimation(
            self.fig,
            self.update,
            frames=range(len(self.steps)),
            interval=100,
            repeat=False
        )
        plt.tight_layout()
        try:
            plt.show()
        except Exception as e:
            print(f"Error during animation: {e}")
        finally:
            plt.close()

def visualize_merge_sort(array_size=30):
    try:
        visualizer = MergeSortVisualizer(array_size)
        visualizer.run_animation()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        plt.close('all')

if __name__ == "__main__":
    visualize_merge_sort(30)