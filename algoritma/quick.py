import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from abc import ABC, abstractmethod

# Import the base class from BubbleSort.py
from BubbleSort import SortingVisualizer

class QuickSortVisualizer(SortingVisualizer):
    def __init__(self, array_size=30):
        super().__init__(array_size, "Quick Sort")
    
    def sort_algorithm(self):
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                colors = ["lightblue"] * len(arr)
                colors[high] = "red"  # pivot
                colors[j] = "green"   # current element
                
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    colors[i] = "green"
                
                self.steps.append(arr.copy())
                self.color_steps.append(colors.copy())
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            colors = ["lightblue"] * len(arr)
            colors[i + 1] = "purple"
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

def visualize_quick_sort(array_size=30):
    try:
        visualizer = QuickSortVisualizer(array_size)
        visualizer.run_animation()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        plt.close('all')

if __name__ == "__main__":
    visualize_quick_sort(30)