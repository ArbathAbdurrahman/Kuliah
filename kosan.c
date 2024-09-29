#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LENGTH 50
#define NUM_ROOMS 5

// Penghuni
typedef struct {
    char name[MAX_NAME_LENGTH];
} Tenant;

// Kamar
typedef struct {
    Tenant *tenant;
    int roomNumber;
} Room;

// Fungsi untuk mengganti penghuni kamar
void changeTenant(Room *room, const char *newTenantName) {
    if (room->tenant == NULL) {
        room->tenant = (Tenant *)malloc(sizeof(Tenant));
    }
    strncpy(room->tenant->name, newTenantName, MAX_NAME_LENGTH);
    room->tenant->name[MAX_NAME_LENGTH - 1] = '\0'; 
}
// Tampilkan informasi kos-kosan
void displayRooms(Room rooms[], int numRooms) {
    for (int i = 0; i < numRooms; i++) {
        printf("Kamar %d (Alamat: %p)\n", rooms[i].roomNumber, (void *)&rooms[i]);
        if (rooms[i].tenant != NULL) {
            printf("  Penghuni: %s\n", rooms[i].tenant->name);
        } else {
            printf("  Penghuni: Kosong\n");
        }
    }
}

int main() {

    Room rooms[NUM_ROOMS];
    for (int i = 0; i < NUM_ROOMS; i++) {
        rooms[i].roomNumber = i + 1;
        rooms[i].tenant = NULL;
    }

    // Ganti penghuni beberapa kamar
    changeTenant(&rooms[0], "Budi");
    changeTenant(&rooms[2], "Siti");
    changeTenant(&rooms[4], "Andi");

    // Tampilkan informasi kos-kosan
    displayRooms(rooms, NUM_ROOMS);

    // Ganti penghuni kamar yang sudah ada
    changeTenant(&rooms[0], "Dewi");

    printf("\nSetelah pergantian penghuni:\n");
    displayRooms(rooms, NUM_ROOMS);

    // Bebaskan memori yang digunakan oleh tenant
    for (int i = 0; i < NUM_ROOMS; i++) {
        if (rooms[i].tenant != NULL) {
            free(rooms[i].tenant);
        }
    }

    return 0;
}
