#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <cstdlib>

using namespace std;
// fungsi menghitung total
double total(const vector<double>& subtotals) {
    double total = 0;
    for (double item : subtotals) {
        total += item;
    }
    return total;
}
// fungsi menghitung diskon
double diskon(double harga, int disc) {
    return harga * (disc / 100.0);
}
// fungsi menghitung sub total
double subtotal(double harga, double discount, int qty) {
    return (harga - discount) * qty;
}
// kode utama
int main() {
    // pemetaan
    vector<vector<string>> data;
    vector<double> subtotals;
    // kode akan terus berjalan
    while (true) {
        cout << string(40, '=') << endl;
        cout << setw(20) << setfill(' ') << "Input Data" << endl;
        cout << string(40, '=') << endl;
        // input
        string nama, satuan, ed;
        int qty, disc;
        double harga;
        
        cout << "Nama Barang\t : ";
        getline(cin, nama);
        
        cout << "QTY\t\t : ";
        cin >> qty;
        cin.ignore();
        
        cout << "Satuan\t\t : ";
        getline(cin, satuan);
        
        cout << "ED\t\t : ";
        getline(cin, ed);
        
        cout << "Harga\t\t : ";
        cin >> harga;
        
        cout << "Diskon %\t : ";
        cin >> disc;
        cin.ignore();
        
        system("cls");
        
        double discount = diskon(harga, disc);
        double subtotall = subtotal(harga, discount, qty);
        
        vector<string> masukan = {
            nama,
            to_string(qty),
            satuan,
            ed,
            to_string(harga),
            to_string(disc),
            to_string(subtotall)
        };
        data.push_back(masukan);
        subtotals.push_back(subtotall);
        // output
        cout << string(98, '=') << endl;
        cout << setw(50) << setfill(' ') << "Rincian" << endl;
        cout << string(98, '=') << endl;
        cout << "No | " << setw(20) << "Nama Barang" << " | " 
             << setw(5) << "QTY" << " | " 
             << setw(10) << "Satuan" << " | "
             << setw(10) << "ED" << " | "
             << setw(10) << "Harga" << " | "
             << setw(7) << "Disc %" << " | "
             << setw(10) << "Subtotal" << endl;
        cout << string(98, '-') << endl;
        // pemanggilan data
        for (size_t i = 0; i < data.size(); ++i) {
            cout << setw(2) << right << i+1 << " | "
                 << setw(20) << data[i][0] << " | "
                 << setw(5) << data[i][1] << " | "
                 << setw(10) << data[i][2] << " | "
                 << setw(10) << data[i][3] << " | "
                 << setw(10) << fixed << setprecision(2) << stod(data[i][4]) << " | "
                 << setw(7) << data[i][5] << " | "
                 << setw(10) << fixed << setprecision(2) << stod(data[i][6]) << endl;
        }
        cout << string(98, '-') << endl;
        
        double totall = total(subtotals);
        cout << setw(83) << right << "Total Harga: " << fixed << setprecision(2) << totall << endl;
        cout << string(98, '=') << endl;
        // kodisi
        string lanjut;
        cout << "Apakah Anda ingin memasukkan data lagi? (y/n): ";
        getline(cin, lanjut);
        
        if (lanjut == "n" || lanjut == "N") {
            break;
        }
    }
    
    return 0;
}