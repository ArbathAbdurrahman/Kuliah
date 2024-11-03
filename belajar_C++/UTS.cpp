#include <iostream>
using namespace std;

const float Pi = 3.14;

// Fungsi untuk menghitung luas lingkaran
float hitungLuas(float jariJari) {
    return Pi * jariJari * jariJari;
}

// Fungsi untuk menghitung keliling lingkaran
float hitungKeliling(float jariJari) {
    return 2 * Pi * jariJari;
}

int main() {
    float jariJari;
    int pilihan;
    char ulang;

    while (true) {
        // Pilihan menu
        cout << "Menghitung Luas dan Keliling Lingkaran" << endl;
        cout << "1. Hitung Luas" << endl;
        cout << "2. Hitung Keliling" << endl;
        cout << "Masukkan pilihan: ";
        cin >> pilihan;

        // Memasukkan nilai jari-jari dengan validasi
        cout << "Masukkan jari-jari lingkaran: ";
        cin >> jariJari;

        if (jariJari < 0) {
            cout << "Nilai jari-jari tidak boleh kurang dari 0. Silakan coba lagi.\n";
            continue;  // Kembali ke awal loop jika input tidak valid
        }

        if (pilihan == 1) {
            cout << "Luas lingkaran: " << hitungLuas(jariJari) << endl;
        } else if (pilihan == 2) {
            cout << "Keliling lingkaran: " << hitungKeliling(jariJari) << endl;
        } else {
            cout << "Pilihan tidak valid. Silakan coba lagi.\n";
        }

        cout << "Apakah ingin mengulang? (y/n): ";
        cin >> ulang;
        if (ulang != 'y' && ulang != 'Y') {
            break;
        }
    }

    return 0;
}
