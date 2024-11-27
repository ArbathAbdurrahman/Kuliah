#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

int main() {
    int sum = 0; // Shared variable for reduction and critical directive
    int array[100];
    omp_lock_t lock;

    // Initialize array with random values
    for (int i = 0; i < 100; i++) {
        array[i] = rand() % 10;
    }

    // Initialize OpenMP lock
    omp_init_lock(&lock);

    #pragma omp parallel
    {
        // Tree structure for computing partial sums
        #pragma omp for reduction(+:sum)
        for (int i = 0; i < 100; i++) {
            sum += array[i];
        }

        // Using critical to print by one thread at a time
        #pragma omp critical
        {
            printf("Partial sum by thread %d: %d\n", omp_get_thread_num(), sum);
        }

        // Lock for controlled access to shared data
        #pragma omp single
        {
            omp_set_lock(&lock);
            printf("Thread %d acquired lock\n", omp_get_thread_num());
            omp_unset_lock(&lock);
        }
    }

    // Destroy lock
    omp_destroy_lock(&lock);

    printf("Total sum: %d\n", sum);

    return 0;
}
