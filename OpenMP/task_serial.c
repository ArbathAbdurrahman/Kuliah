#include <stdio.h>
#include <time.h>

int main() {
    clock_t start = clock(); // Mulai pengukuran waktu

    // Eksekusi tugas secara berurutan
    for (int i = 1; i <= 1000; i++) {
        printf("Task 1 - Loop iteration: %d by main thread\n", i);
    }
    printf("Task 1 completed by main thread\n");

    for (int i = 1; i <= 1000; i++) {
        printf("Task 2 - Loop iteration: %d by main thread\n", i);
    }
    printf("Task 2 completed by main thread\n");

    for (int i = 1; i <= 1000; i++) {
        printf("Task 3 - Loop iteration: %d by main thread\n", i);
    }
    printf("Task 3 completed by main thread\n");

    for (int i = 1; i <= 1000; i++) {
        printf("Task 4 - Loop iteration: %d by main thread\n", i);
    }
    printf("Task 4 completed by main thread\n");

    for (int i = 1; i <= 1000; i++) {
        printf("Task 5 - Loop iteration: %d by main thread\n", i);
    }
    printf("Task 5 completed by main thread\n");

    printf("All serial tasks completed.\n");

    clock_t end = clock(); // Akhiri pengukuran waktu
    double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Execution time: %.2f ms\n", cpu_time_used * 1000);

    return 0;
}