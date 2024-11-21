def quicksort(arr):
    # Jika array hanya memiliki 1 elemen atau kosong, kembalikan array
    if len(arr) <= 1:
        return arr
    
    # Pilih pivot (misalnya, elemen terakhir)
    pivot = arr[len(arr) - 1]
    
    # Pisahkan elemen yang lebih kecil dari pivot dan yang lebih besar atau sama dengan pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Rekursif untuk mengurutkan bagian kiri dan kanan, lalu gabungkan
    return quicksort(left) + [pivot] + quicksort(right)

# Contoh penggunaan
arr = [10, 7, 8, 9, 1, 5]
print("Array sebelum diurutkan:", arr)

# Memanggil fungsi quicksort
sorted_arr = quicksort(arr)
print("Array setelah diurutkan:", sorted_arr)
