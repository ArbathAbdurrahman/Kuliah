#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    
    // Lakukan n-1 iterasi untuk memastikan seluruh array terurut
    for (int i = 0; i < n; i++) {
        // Setiap iterasi, lakukan penyortiran dari awal hingga elemen ke-n-i
        for (int j = 0; j < n - i - 1; j++) {
            // Tukar jika elemen saat ini lebih besar dari elemen berikutnya
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    vector<int> arr = {10, 7, 8, 9, 1, 5};
    
    cout << "Array sebelum diurutkan: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    bubbleSort(arr);

    cout << "Array setelah diurutkan: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}