#include <stdio.h>
#include <omp.h>
#include <locale>

int main()
{
	setlocale(LC_ALL, "Russian");

	int n = 32;
	
	printf("n в последовательной области (начало): %d\n", n);

#pragma omp parallel private(n) num_threads(10)
	{
		printf("Значение n в потоке (на входе): %d\n", n);
	
		n = omp_get_thread_num(); // Присваеваем n номер текущего потока (нити)
		printf("Значение n в потоке (на выходе): %d\n", n);

	}
	n = 3;
	printf("n в последовательной области (конец): %d\n", n);
	return 0;
}