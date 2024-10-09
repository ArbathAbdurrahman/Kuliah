#include <stdio.h>
#include <omp.h>

int main() {
    omp_set_num_threads(1); // set thread
    int loop = 100; // Jumlah Loop
    double start_time = omp_get_wtime(); // Mulai pengukuran waktu

    #pragma omp parallel
    {
        #pragma omp single
        {
            #pragma omp task
            {
                for (int i = 1; i <= loop; i++) {
                    printf("Task 1 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
                }
                printf("Task 1 completed by thread %d\n", omp_get_thread_num());
            }

            #pragma omp task
            {
                for (int i = 1; i <= loop; i++) {
                    printf("Task 2 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
                }
                printf("Task 2 completed by thread %d\n", omp_get_thread_num());
            }

            #pragma omp task
            {
                for (int i = 1; i <= loop; i++) {
                    printf("Task 3 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
                }
                printf("Task 3 completed by thread %d\n", omp_get_thread_num());
            }

            #pragma omp task
            {
                for (int i = 1; i <= loop; i++) {
                    printf("Task 4 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
                }
                printf("Task 4 completed by thread %d\n", omp_get_thread_num());
            }
            #pragma omp task
            {
                for (int i = 1; i <= loop; i++) {
                    printf("Task 5 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
                }
                printf("Task 5 completed by thread %d\n", omp_get_thread_num());
            }
            // // Task 6
            // #pragma omp task
            // {
            //     for (int i = 1; i <= loop; i++) {
            //         printf("Task 6 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
            //     }
            //     printf("Task 6 completed by thread %d\n", omp_get_thread_num());
            // }

            // // Task 7
            // #pragma omp task
            // {
            //     for (int i = 1; i <= loop; i++) {
            //         printf("Task 7 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
            //     }
            //     printf("Task 7 completed by thread %d\n", omp_get_thread_num());
            // }

            // // Task 8
            // #pragma omp task
            // {
            //     for (int i = 1; i <= loop; i++) {
            //         printf("Task 8 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
            //     }
            //     printf("Task 8 completed by thread %d\n", omp_get_thread_num());
            // }

            // // Task 9
            // #pragma omp task
            // {
            //     for (int i = 1; i <= loop; i++) {
            //         printf("Task 9 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
            //     }
            //     printf("Task 9 completed by thread %d\n", omp_get_thread_num());
            // }

            // // Task 10
            // #pragma omp task
            // {
            //     for (int i = 1; i <= loop; i++) {
            //         printf("Task 10 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
            //     }
            //     printf("Task 10 completed by thread %d\n", omp_get_thread_num());
            // }

            // // Task 11
            // #pragma omp task
            // {
            //     for (int i = 1; i <= loop; i++) {
            //         printf("Task 11 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
            //     }
            //     printf("Task 11 completed by thread %d\n", omp_get_thread_num());
            // }

            // // Task 12
            // #pragma omp task
            // {
            //     for (int i = 1; i <= loop; i++) {
            //         printf("Task 12 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
            //     }
            //     printf("Task 12 completed by thread %d\n", omp_get_thread_num());
            // }
            // // Task 13
            // #pragma omp task
            // {
            //     for (int i = 1; i <= loop; i++) {
            //         printf("Task 13 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
            //     }
            //     printf("Task 13 completed by thread %d\n", omp_get_thread_num());
            // }
            // // Task 14
            // #pragma omp task
            // {
            //     for (int i = 1; i <= loop; i++) {
            //         printf("Task 14 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
            //     }
            //     printf("Task 14 completed by thread %d\n", omp_get_thread_num());
            // }
            // // Task 15
            // #pragma omp task
            // {
            //     for (int i = 1; i <= loop; i++) {
            //         printf("Task 15 - Loop iteration: %d by thread %d\n", i, omp_get_thread_num());
            //     }
            //     printf("Task 15 completed by thread %d\n", omp_get_thread_num());
            // }

            #pragma omp taskwait // Tunggu hingga semua task selesai
            printf("All serial tasks completed.\n");
        }
    }

    double end_time = omp_get_wtime(); // Akhiri pengukuran waktu
    printf("Execution time: %.2f ms\n", (end_time - start_time) * 1000); // Cetak waktu eksekusi dalam ms
    return 0;
}
