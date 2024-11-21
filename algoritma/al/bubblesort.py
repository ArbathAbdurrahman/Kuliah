def bubble_sort(arr):
    n = len(arr)
    
    # Lakukan n-1 iterasi untuk memastikan seluruh array terurut
    for i in range(n):
        # Setiap iterasi, lakukan penyortiran dari awal hingga elemen ke-n-i
        for j in range(0, n-i-1):
            # Tukar jika elemen saat ini lebih besar dari elemen berikutnya
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Contoh penggunaan
arr = [10, 7, 8, 9, 1, 5]
print("Array sebelum diurutkan:", arr)

# Memanggil fungsi bubble_sort
bubble_sort(arr)
print("Array setelah diurutkan:", arr)
