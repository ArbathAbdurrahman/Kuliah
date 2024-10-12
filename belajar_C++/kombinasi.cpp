#include <iostream>
#include <string>
using namespace std;

int main() {
    string tanaman[3] = {"Mawar", "Melati", "Kamboja"};
    string hewan[3] = {"Kucing", "Lele", "Burung"};
    string kendaraan[3] = {"Kapal", "Pesawat", "Becak"};

    string kombinasi[9];
    for (int i = 0; i < 3; i++) {
        kombinasi[i] = tanaman[i];
        kombinasi[i + 3] = hewan[i];
        kombinasi[i + 6] = kendaraan[i];
    }

    cout << "Array kombinasi: " << endl;
    for (int i = 0; i < 9; i++) {
        cout << kombinasi[i] << endl;
    }
    return 0;
}
