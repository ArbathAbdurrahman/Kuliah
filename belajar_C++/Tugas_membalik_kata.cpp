#include <iostream>
#include <string>
using namespace std;

string balikString(string str) {
    int n = str.length();
    for (int i = 0; i < n / 2; i++) {
        swap(str[i], str[n - i - 1]);
    }
    return str;
}

int main() {
    string input;
    
    cout << "Masukkan string (misalnya: nama, NIM, umur, asal daerah): ";
    getline(cin, input);
    
    string balik = balikString(input);
    
    cout << "Hasil string yang dibalik: " << balik << endl;
    
    return 0;
}
