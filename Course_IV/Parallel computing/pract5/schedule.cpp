#include <iostream>
#include <stdio.h>
#include <omp.h>
#include <locale>
#include <thread>
#include <chrono>

unsigned int microseconds;

using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");
	int i;
	double time = omp_get_wtime();

#pragma omp parallel private(i) num_threads(4)
	{

    //#pragma omp for schedule (static, 6) //54.1926

    //#pragma omp for schedule (dynamic, 6) //54.1742

    //#pragma omp for schedule (guided, 6) //51.1629

    #pragma omp for schedule (auto) //50.1715

            for (i = 0; i<200; i++)

            {

                printf("Поток %d выполнила итерацию %d\n", omp_get_thread_num(), i);
                
                this_thread::sleep_for (chrono::seconds(1));  

            }

	}

	cout << "Time = " << (omp_get_wtime() - time) << endl;

}