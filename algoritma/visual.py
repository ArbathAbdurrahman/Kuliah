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
        # Generate random data
        np.random.seed(42)
        self.data = np.random.randint(1, 100, size=self.array_size)
        self.steps = []
        self.color_steps = []
        self.comparisons = 0
        self.swaps = 0
        
        # Initial state
        self.steps.append(self.data.copy())
        self.color_steps.append(["#3498db"] * len(self.data))  # Light blue
        self.sort_algorithm()
        
    @abstractmethod
    def sort_algorithm(self):
        pass
    
    def setup_plot(self):
        # Create figure with two subplots
        self.fig, (self.ax, self.stats_ax) = plt.subplots(2, 1, figsize=(12, 8), 
                                                         height_ratios=[3, 1])
        
        # Main sorting visualization
        self.bar_rects = self.ax.bar(range(len(self.data)), self.steps[0],
                                    color=self.color_steps[0], align="edge",
                                    alpha=0.7, width=0.8)
        
        # Configure main plot
        self.ax.set_xlim(-1, len(self.data))
        self.ax.set_ylim(0, int(1.1 * max(self.data)))
        self.ax.set_xlabel("Index", fontsize=10)
        self.ax.set_ylabel("Value", fontsize=10)
        self.ax.set_title(f"{self.algorithm_name}", pad=20, fontsize=12)
        self.ax.grid(True, linestyle='--', alpha=0.7)
        
        # Configure stats plot
        self.stats_ax.set_axis_off()
        self.stats_text = self.stats_ax.text(0.02, 0.5, "", transform=self.stats_ax.transAxes,
                                           fontsize=10, verticalalignment='center')
        
        self.add_legend()
        plt.tight_layout()
    
    def add_legend(self):
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#3498db', label='Unsorted', alpha=0.7),
            Patch(facecolor='#e74c3c', label='Current Element', alpha=0.7),
            Patch(facecolor='#2ecc71', label='Comparing', alpha=0.7),
            Patch(facecolor='#9b59b6', label='Sorted', alpha=0.7)
        ]
        self.ax.legend(handles=legend_elements, loc='upper right', fontsize=8)
    
    def update(self, frame):
        # Update bars
        for rect, val, color in zip(self.bar_rects, self.steps[frame], self.color_steps[frame]):
            rect.set_height(val)
            rect.set_color(color)
        
        # Update statistics
        stats_text = (
            f"Progress: {frame + 1}/{len(self.steps)}\n"
            f"Comparisons: {self.comparisons}\n"
            f"Swaps: {self.swaps}\n"
            f"Array size: {self.array_size}"
        )
        self.stats_text.set_text(stats_text)
        
        return tuple(list(self.bar_rects) + [self.stats_text])
    
    def run_animation(self):
        anim = animation.FuncAnimation(
            self.fig,
            self.update,
            frames=range(len(self.steps)),
            interval=100,  # Slower for better visualization
            repeat=False,
            blit=True
        )
        plt.show()

class BubbleSortVisualizer(SortingVisualizer):
    def __init__(self, array_size=30):
        super().__init__(array_size, "Bubble Sort")
    
    def sort_algorithm(self):
        arr = self.data.copy()
        n = len(arr)
        
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                self.comparisons += 1
                colors = ["#3498db"] * n  # Default color
                
                # Mark sorted portion
                for k in range(n-i, n):
                    colors[k] = "#9b59b6"  # Purple for sorted
                
                # Mark comparing elements
                colors[j] = "#2ecc71"      # Green for comparing
                colors[j + 1] = "#2ecc71"
                
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    colors[j] = "#e74c3c"   # Red for swapping
                    colors[j + 1] = "#e74c3c"
                    swapped = True
                    self.swaps += 1
                
                self.steps.append(arr.copy())
                self.color_steps.append(colors.copy())
            
            if not swapped:
                # Mark all remaining elements as sorted
                colors = ["#9b59b6"] * n
                self.steps.append(arr.copy())
                self.color_steps.append(colors)
                break

class QuickSortVisualizer(SortingVisualizer):
    def __init__(self, array_size=30):
        super().__init__(array_size, "Quick Sort")
    
    def sort_algorithm(self):
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                self.comparisons += 1
                colors = ["#3498db"] * len(arr)
                colors[high] = "#e74c3c"  # Pivot in red
                colors[j] = "#2ecc71"     # Current element in green
                
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    self.swaps += 1
                    colors[i] = "#2ecc71"
                
                # Mark sorted portions
                for k in range(low):
                    colors[k] = "#9b59b6"
                for k in range(high + 1, len(arr)):
                    colors[k] = "#9b59b6"
                
                self.steps.append(arr.copy())
                self.color_steps.append(colors.copy())
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            self.swaps += 1
            
            colors = ["#3498db"] * len(arr)
            colors[i + 1] = "#9b59b6"
            for k in range(low):
                colors[k] = "#9b59b6"
            for k in range(high + 1, len(arr)):
                colors[k] = "#9b59b6"
                
            self.steps.append(arr.copy())
            self.color_steps.append(colors.copy())
            
            return i + 1
        
        def quicksort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quicksort(arr, low, pi - 1)
                quicksort(arr, pi + 1, high)
        
        arr = self.data.copy()
        quicksort(arr, 0, len(arr) - 1)
        
        # Final sorted state
        self.steps.append(arr.copy())
        self.color_steps.append(["#9b59b6"] * len(arr))

class SelectionSortVisualizer(SortingVisualizer):
    def __init__(self, array_size=30):
        super().__init__(array_size, "Selection Sort")
    
    def sort_algorithm(self):
        arr = self.data.copy()
        n = len(arr)
        
        for i in range(n):
            min_idx = i
            
            for j in range(i + 1, n):
                self.comparisons += 1
                colors = ["#3498db"] * n
                
                # Mark sorted portion
                for k in range(i):
                    colors[k] = "#9b59b6"
                
                colors[min_idx] = "#e74c3c"  # Current minimum
                colors[j] = "#2ecc71"        # Comparing element
                
                self.steps.append(arr.copy())
                self.color_steps.append(colors.copy())
                
                if arr[j] < arr[min_idx]:
                    colors[min_idx] = "#3498db"
                    min_idx = j
                    colors[min_idx] = "#e74c3c"
                    
                    self.steps.append(arr.copy())
                    self.color_steps.append(colors.copy())
            
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                self.swaps += 1
            
            # Update colors to show sorted portion
            colors = ["#3498db"] * n
            for k in range(i + 1):
                colors[k] = "#9b59b6"
            self.steps.append(arr.copy())
            self.color_steps.append(colors.copy())

def visualize_sorting_algorithm(algorithm, array_size=30):
    try:
        visualizer = algorithm(array_size)
        visualizer.run_animation()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        plt.close('all')

if __name__ == "__main__":
    print("\nVisualisasi Algoritma Pengurutan dari Terkecil ke Terbesar")
    print("=" * 50)
    
    algorithms = [
        ("Bubble Sort", BubbleSortVisualizer),
        ("Quick Sort", QuickSortVisualizer),
        ("Selection Sort", SelectionSortVisualizer)
    ]
    
    for name, algorithm in algorithms:
        print(f"\nMemvisualisasikan {name}...")
        visualize_sorting_algorithm(algorithm, array_size=30)