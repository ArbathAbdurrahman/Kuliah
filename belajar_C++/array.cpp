#include <iostream>
using namespace std;

int main() {
    int angka[5] = {1,2,3,4,5};
    for (int i = 0; i<5;i++) {
        cout << "Elemen ke-"<< i << angka[i] << endl;
    }
    return 0;
}