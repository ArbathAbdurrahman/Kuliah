#include <iostream>
using namespace std;

void tambahNilai(int arr[], int ukuran , int nilaiTambah) {
    for (int i = 0; i<ukuran;i++) {
        arr[i] += nilaiTambah;
    }
}

int main() {
    int angka[5] = {10,20,30,40,50};

    cout << "Sebelum modifikasi: ";
    for (int i = 0; i<5;i++) {
        cout << angka[i]<< " ";
    }
    cout << endl;

    tambahNilai(angka, 5, 10);
    cout << "Setelah modifikasi: ";
    for (int i = 0; i <5; i++) {
    cout << angka[i] << " "; 
    }
    cout << endl;
    return 0;
}