import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np
from abc import ABC, abstractmethod

class SortingVisualizer(ABC):
    def __init__(self, array_size=30, algorithm_name="Sorting Algorithm"):
        self.array_size = array_size
        self.algorithm_name = algorithm_name
        self.setup_data()
        self.setup_plot()
    
    def setup_data(self):
        np.random.seed(42)
        self.data = np.random.randint(1, 100, size=self.array_size)
        self.steps = []
        self.color_steps = []
        self.steps.append(self.data.copy())
        self.color_steps.append(["lightblue"] * len(self.data))
        self.sort_algorithm()
        
    @abstractmethod
    def sort_algorithm(self):
        pass
    
    def setup_plot(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.bar_rects = self.ax.bar(range(len(self.data)), self.steps[0],
                                    color=self.color_steps[0], align="edge")
        
        self.ax.set_xlim(0, len(self.data))
        self.ax.set_ylim(0, int(1.1 * max(self.data)))
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Value")
        self.ax.set_title(f"{self.algorithm_name} Visualization")
        
        self.text = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)
        self.add_legend()
    
    def add_legend(self):
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='lightblue', label='Unsorted'),
            Patch(facecolor='red', label='Current Element'),
            Patch(facecolor='green', label='Comparing/Swapping'),
            Patch(facecolor='purple', label='Sorted')
        ]
        self.ax.legend(handles=legend_elements, loc='upper right')
    
    def update(self, frame):
        for rect, val, color in zip(self.bar_rects, self.steps[frame], self.color_steps[frame]):
            rect.set_height(val)
            rect.set_color(color)
        self.text.set_text(f'Step: {frame}/{len(self.steps)-1}')
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

class BubbleSortVisualizer(SortingVisualizer):
    def __init__(self, array_size=30):
        super().__init__(array_size, "Bubble Sort")
    
    def sort_algorithm(self):
        arr = self.data.copy()
        n = len(arr)
        
        for i in range(n):
            for j in range(0, n-i-1):
                colors = ["lightblue"] * n
                # Mark sorted portion
                for k in range(n-i, n):
                    colors[k] = "purple"
                # Mark comparing elements
                colors[j] = "green"
                colors[j + 1] = "green"
                
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    colors[j] = "red"
                    colors[j + 1] = "red"
                
                self.steps.append(arr.copy())
                self.color_steps.append(colors.copy())

def visualize_bubble_sort(array_size=30):
    try:
        visualizer = BubbleSortVisualizer(array_size)
        visualizer.run_animation()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        plt.close('all')

if __name__ == "__main__":
    visualize_bubble_sort(30)