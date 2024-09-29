#include <iostream>
using namespace std;

int main() {
    string Nama;
    int Tg1, Tg2, Tg3, Tg4, Tg5;

    // Meminta input User
    cout << "Masukkan Nama Mahasiswa : ";
    cin >> Nama;
    cout << "Nilai Tugas 1 : ";
    cin >> Tg1;
    cout << "Nilai Tugas 2 : ";
    cin >> Tg2;
    cout << "Nilai Tugas 3 : ";
    cin >> Tg3;
    cout << "Nilai Tugas 4 : ";
    cin >> Tg4;
    cout << "Nilai Tugas 5 : ";
    cin >> Tg5;

    // Mencari nilai rata-rata
    int rata_rata = (Tg1 + Tg2 + Tg3 + Tg4 + Tg5) / 5;
    cout << "Rata-rata = " << rata_rata << endl;

    // Mencari nilai tertinggi
    if (Tg1 >= Tg2 && Tg1 >= Tg3 && Tg1 >= Tg4 && Tg1 >= Tg5) {
        cout << "Nilai Tertinggi = " << Tg1 << endl;
    } else if (Tg2 >= Tg1 && Tg2 >= Tg3 && Tg2 >= Tg4 && Tg2 >= Tg5) {
        cout << "Nilai Tertinggi = " << Tg2 << endl;
    } else if (Tg3 >= Tg1 && Tg3 >= Tg2 && Tg3 >= Tg4 && Tg3 >= Tg5) {
        cout << "Nilai Tertinggi = " << Tg3 << endl;
    } else if (Tg4 >= Tg1 && Tg4 >= Tg2 && Tg4 >= Tg3 && Tg4 >= Tg5) {
        cout << "Nilai Tertinggi = " << Tg4 << endl;
    } else if (Tg5 >= Tg1 && Tg5 >= Tg2 && Tg5 >= Tg3 && Tg5 >= Tg4) {
        cout << "Nilai Tertinggi = " << Tg5 << endl;
    }

    // Mencari nilai terkecil
    if (Tg1 <= Tg2 && Tg1 <= Tg3 && Tg1 <= Tg4 && Tg1 <= Tg5) {
        cout << "Nilai Terkecil = " << Tg1 << endl;
    } else if (Tg2 <= Tg1 && Tg2 <= Tg3 && Tg2 <= Tg4 && Tg2 <= Tg5) {
        cout << "Nilai Terkecil = " << Tg2 << endl;
    } else if (Tg3 <= Tg1 && Tg3 <= Tg2 && Tg3 <= Tg4 && Tg3 <= Tg5) {
        cout << "Nilai Terkecil = " << Tg3 << endl;
    } else if (Tg4 <= Tg1 && Tg4 <= Tg2 && Tg4 <= Tg3 && Tg4 <= Tg5) {
        cout << "Nilai Terkecil = " << Tg4 << endl;
    } else if (Tg5 <= Tg1 && Tg5 <= Tg2 && Tg5 <= Tg3 && Tg5 <= Tg4) {
        cout << "Nilai Terkecil = " << Tg5 << endl;
    }

    return 0;
}
