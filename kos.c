// Nama : Arbath Abdurrahman
// NIM  : 23106050012
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main() {
    char kamar1[20] = "Tukiman";
    char kamar2[20] = "Joko";
    char kamar3[20] = "Surip";
    char kamar4[20] = "Parjo";

    while (1) {
        printf("kamar1: %s, Alamat: %p\n", kamar1, (void*)&kamar1);
        printf("kamar2: %s, Alamat: %p\n", kamar2, (void*)&kamar2);
        printf("kamar3: %s, Alamat: %p\n", kamar3, (void*)&kamar3);
        printf("kamar4: %s, Alamat: %p\n\n", kamar4, (void*)&kamar4);
        // Mengganti nilai kamar
        char temp[20];
        strcpy(temp, kamar4);
        strcpy(kamar4, kamar3);
        strcpy(kamar3, kamar2);
        strcpy(kamar2, kamar1);
        strcpy(kamar1, temp);
        sleep(2);
    }
    return 0;
}
