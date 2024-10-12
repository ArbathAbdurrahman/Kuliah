#include <iostream>
#include <string>
using namespace std;

// Fungsi untuk memecah kalimat menjadi kata-kata dan mengelompokkan berdasarkan panjang
void kelompokkanKataBerdasarkanPanjang(const string& kalimat) {
    const int MAX_PANJANG = 50;  // Asumsi panjang kata maksimal
    string kelompokKata[MAX_PANJANG][100];  // Array 2D untuk menyimpan kata-kata berdasarkan panjangnya
    int jumlahKata[MAX_PANJANG] = {0};  // Array untuk menghitung jumlah kata dalam setiap kelompok

    string kata;
    int kataIndex = 0;

    // Memecah kalimat menjadi kata-kata secara manual
    for (int i = 0; i <= kalimat.length(); i++) {
        if (kalimat[i] == ' ' || kalimat[i] == '\0') {
            if (!kata.empty()) {
                int panjang = kata.length();
                // Menyimpan kata di array kelompok sesuai panjangnya
                kelompokKata[panjang][jumlahKata[panjang]] = kata;
                jumlahKata[panjang]++;
                kata.clear();  // Reset kata untuk kata berikutnya
            }
        } else {
            kata += kalimat[i];  // Menambahkan karakter ke kata
        }
    }

    // Menampilkan hasil pengelompokan
    for (int i = 1; i < MAX_PANJANG; i++) {
        if (jumlahKata[i] > 0) {
            cout << "Panjang " << i << ": ";
            for (int j = 0; j < jumlahKata[i]; j++) {
                cout << kelompokKata[i][j] << " ";
            }
            cout << "(Total: " << jumlahKata[i] << " kata)" << endl;
        }
    }
}

int main() {
    string kalimat;

    // Input dari pengguna
    cout << "Masukkan sebuah kalimat: ";
    getline(cin, kalimat);

    // Memanggil fungsi untuk mengelompokkan kata-kata berdasarkan panjang
    kelompokkanKataBerdasarkanPanjang(kalimat);

    return 0;
}
