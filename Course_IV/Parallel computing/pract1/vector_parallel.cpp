#include <omp.h>
#include <iostream>
#include <stdio.h>
#include <locale>
#include <time.h>
using namespace std;
 
int main()
{
    setlocale(LC_ALL, "Russian");
    // int a[10000], b[10000], c[10000];
    std::size_t array_size = 1000000000;
    int* a = new int[array_size];
    int* b = new int[array_size];
    int* c = new int[array_size];
    clock_t start_t, end_t, total_t;
    start_t = clock();
    printf("Начало цикла инициализации векторов , start_t = %ld\n", start_t);
 
#pragma omp parallel for
    for (int i = 0; i < 1000000000; i++)
    {
        a[i] = i;
        b[i] = i;
    }
 
    end_t = clock();
    printf("Конец цикла инициализации векторов , end_t = %ld\n", end_t);
 
    total_t = end_t - start_t;
    cout << "Общее время работы процессора по инициализации векторов " << total_t / (CLOCKS_PER_SEC) << " seconds" << endl;
 
    start_t = clock();
    printf("Начало цикла сложения векторов , start_t = %ld\n", start_t);
 
#pragma omp parallel for
    for (int i = 0; i < 1000000000; i++)
        c[1] = a[i] + b[i];
    end_t = clock();
    printf("Конец цикла сложения векторов , end_t = %ld\n", end_t);
    total_t = end_t - start_t;
    cout << "Общее время работы процессора по сложению векторов " << total_t / (CLOCKS_PER_SEC) << " seconds" << 
endl;
 
    delete[] a;
    delete[] b;
    delete[] c;
    return(0);
}
