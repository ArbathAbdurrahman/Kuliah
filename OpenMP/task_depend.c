#include <stdio.h>
#include <omp.h>

int main() {
    double start_time = omp_get_wtime(); // Mulai pengukuran waktu

    #pragma omp parallel
    {
        #pragma omp single
        {
            int dep1 = 0, dep2 = 0, dep3 = 0, dep4 = 0, dep5 = 0; //dependensi berurutan

            #pragma omp task depend(out: dep1)
            {
                for (int i = 1; i <= 10; i++) {
                    printf("Task 1 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
                }
                printf("Task 1 completed by thread %d\n", omp_get_thread_num());
            }

            #pragma omp task depend(in: dep1) depend(out: dep2)
            {
                for (int i = 1; i <= 10; i++) {
                    printf("Task 2 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
                }
                printf("Task 2 completed by thread %d\n", omp_get_thread_num());
            }

            #pragma omp task depend(in: dep2) depend(out: dep3)
            {
                for (int i = 1; i <= 10; i++) {
                    printf("Task 3 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
                }
                printf("Task 3 completed by thread %d\n", omp_get_thread_num());
            }

            #pragma omp task depend(in: dep3) depend(out: dep4)
            {
                for (int i = 1; i <= 10; i++) {
                    printf("Task 4 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
                }
                printf("Task 4 completed by thread %d\n", omp_get_thread_num());
            }

            #pragma omp task depend(in: dep4) depend(out: dep5)
            {
                for (int i = 1; i <= 10; i++) {
                    printf("Task 5 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
                }
                printf("Task 5 completed by thread %d\n", omp_get_thread_num());
            }

            #pragma omp taskwait
            printf("All parallel but serial tasks completed.\n");
        }
    }

    double end_time = omp_get_wtime(); // Akhiri pengukuran waktu
    printf("Execution time: %.2f ms\n", (end_time - start_time) * 1000); // Cetak waktu eksekusi dalam ms
    return 0;
}
