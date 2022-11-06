#include <stdio.h>
#include <locale>
#include <omp.h>

int main()
{
	int n;

#pragma omp parallel private(n)
	{
		n = 1;
#pragma omp master
		{
			n = 2;
		}
		printf("Первое значение n потока %d: %d\n", omp_get_thread_num(),n);

#pragma omp barrier
#pragma omp master
		{
			n = 3;
		}
		printf("Второе значение n потока %d: %d\n", omp_get_thread_num(),  n);
	}
	return 0;
}