import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from abc import ABC, abstractmethod

# Import the base class from BubbleSort.py
from BubbleSort import SortingVisualizer

class SelectionSortVisualizer(SortingVisualizer):
    def __init__(self, array_size=30):
        super().__init__(array_size, "Selection Sort")
    
    def sort_algorithm(self):
        arr = self.data.copy()
        n = len(arr)
        
        for i in range(n):
            min_idx = i
            colors = ["lightblue"] * n
            # Mark sorted portion
            for k in range(i):
                colors[k] = "purple"
                
            for j in range(i + 1, n):
                colors[min_idx] = "red"
                colors[j] = "green"
                self.steps.append(arr.copy())
                self.color_steps.append(colors.copy())
                
                if arr[j] < arr[min_idx]:
                    colors[min_idx] = "lightblue"
                    min_idx = j
                    colors[min_idx] = "red"
                    self.steps.append(arr.copy())
                    self.color_steps.append(colors.copy())
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            colors = ["lightblue"] * n
            for k in range(i + 1):
                colors[k] = "purple"
            self.steps.append(arr.copy())
            self.color_steps.append(colors.copy())

def visualize_selection_sort(array_size=30):
    try:
        visualizer = SelectionSortVisualizer(array_size)
        visualizer.run_animation()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        plt.close('all')

if __name__ == "__main__":
    visualize_selection_sort(30)