//g++ timeit.cpp cpp.cpp

#include <iostream>
#include "timeit.h"
using namespace std;

int i;
int n = 2001;
int a[2001];
int zeros, positive, negative;

//Генерация массива
void generator()
{   
    srand((unsigned) time(0));
    for (i=0;i<n;i++)
        a[i]=-10+rand()%20;
}

int main()
{
    Timer tmr;
    zeros = 0;
    positive = 0;
    negative = 0;
    generator();

    for (i=0;i<n;i++)
    {
        if (a[i] < 0)
            negative ++;
        else if (a[i] > 0)
            positive ++;
        else
            zeros ++;
    }

    printf("\nC++:\nПоложительных: %i\n",positive);
    printf("Отрицательных: %i\n",negative);
    printf("Кол-во нулей: %i\nВремя: ",zeros);
    double t = tmr.elapsed();
    cout << t << endl;
    return 0;
}