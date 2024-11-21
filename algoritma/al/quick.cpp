#include <iostream>
#include <vector>
using namespace std;

vector<int> quicksort(vector<int>& arr) {
    // Jika array hanya memiliki 1 elemen atau kosong, kembalikan array
    if (arr.size() <= 1) {
        return arr;
    }
    
    // Pilih pivot (misalnya, elemen terakhir)
    int pivot = arr.back();
    arr.pop_back();
    
    // Pisahkan elemen yang lebih kecil dari pivot dan yang lebih besar atau sama dengan pivot
    vector<int> left, right;
    for (int x : arr) {
        if (x <= pivot) {
            left.push_back(x);
        } else {
            right.push_back(x);
        }
    }
    
    // Rekursif untuk mengurutkan bagian kiri dan kanan, lalu gabungkan
    vector<int> sortedLeft = quicksort(left);
    vector<int> sortedRight = quicksort(right);
    
    vector<int> result = sortedLeft;
    result.push_back(pivot);
    result.insert(result.end(), sortedRight.begin(), sortedRight.end());
    
    return result;
}

int main() {
    vector<int> arr = {10, 7, 8, 9, 1, 5};
    
    cout << "Array sebelum diurutkan: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    arr = quicksort(arr);

    cout << "Array setelah diurutkan: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}