#include <stdio.h>
#include <time.h>

void perform_task(int task_num, int iterations) {
    for (int i = 1; i <= iterations; i++) {
        printf("Task %d - Loop iteration: %d\n", task_num, i);
    }
    printf("Task %d completed\n", task_num);
}

int main() {
    clock_t start = clock(); // Mulai pengukuran waktu

    // Eksekusi tasks secara berurutan
    perform_task(1, 1000);
    perform_task(2, 1000);
    perform_task(3, 1000);
    perform_task(4, 1000);
    perform_task(5, 1000);

    printf("All serial tasks completed.\n");

    clock_t end = clock(); // Akhiri pengukuran waktu
    double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Execution time: %.2f ms\n", cpu_time_used * 1000);

    return 0;
}