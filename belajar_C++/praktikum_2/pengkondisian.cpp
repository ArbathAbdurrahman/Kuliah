#include <iostream>
using namespace std;

int main() {
    int angka;

    cout << "Massukan angka : ";
    cin >> angka;

    if (angka %2 == 0) {
        cout << "Angka Genap." << endl;
    }else {
        cout << "Angka Ganjil." << endl;
    }

    return 0;
}