#include <iostream>
#include <stdio.h>
#include <omp.h>

int main()

{
	int num;
    printf("Вывод в main thread");
    

#pragma omp parallel num_threads(6) private(num) 
	{
		num = omp_get_thread_num(); //Номер текущего потока
		printf("Перед директивой single num=%d \n", num);

        #pragma omp barrier
        #pragma omp single copyprivate(num)
        {
            printf("Введите целое число : ");
            scanf("%d", &num);
        }

		printf("После директивы single num=%d \n", num);
	}
}