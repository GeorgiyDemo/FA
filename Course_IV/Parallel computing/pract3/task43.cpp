#include <stdio.h>
#include <omp.h>
#include <locale>

int main()
{
	int n;
	omp_set_nested(1);
    //процедура включает или отключает вложенный параллелизм, устанавливая значение max-active-levels-var

#pragma omp parallel private(n)
	{
		n = omp_get_thread_num();
        #pragma omp parallel
		{
			printf("Часть 1, поток %d - %d\n", n, omp_get_thread_num());
		}
	}
	omp_set_nested(0);
    #pragma omp parallel private(n)
	{
		n = omp_get_thread_num();
        #pragma omp parallel
            {
                printf("Часть 2, поток %d - %d\n", n, omp_get_thread_num());
            }
    }
	return 0;
}