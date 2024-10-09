#include <stdio.h>
#include <time.h>

int main() {
    int loop = 10; // Jumlah Loop
    clock_t start_time = clock(); // Mulai pengukuran waktu

    // Task 1
    for (int i = 1; i <= loop; i++) {
        printf("Task 1 - Loop iteration: %d\n", i);
    }
    printf("Task 1 completed\n");

    // Task 2
    for (int i = 1; i <= loop; i++) {
        printf("Task 2 - Loop iteration: %d\n", i);
    }
    printf("Task 2 completed\n");

    // Task 3
    for (int i = 1; i <= loop; i++) {
        printf("Task 3 - Loop iteration: %d\n", i);
    }
    printf("Task 3 completed\n");

    // Task 4
    for (int i = 1; i <= loop; i++) {
        printf("Task 4 - Loop iteration: %d\n", i);
    }
    printf("Task 4 completed\n");

    // Task 5
    for (int i = 1; i <= loop; i++) {
        printf("Task 5 - Loop iteration: %d\n", i);
    }
    printf("Task 5 completed\n");

    printf("All tasks completed.\n");

    clock_t end_time = clock(); // Akhiri pengukuran waktu
    double execution_time = (double)(end_time - start_time) / CLOCKS_PER_SEC * 1000.0;
    printf("Execution time: %.2f ms\n", execution_time);

    return 0;
}