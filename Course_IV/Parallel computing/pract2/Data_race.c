#include <iostream>
#include "omp.h"
#include <string>

using namespace std;

int main()
{
	int x = 0;
#pragma omp parallel shared(x) num_threads(30)
	{
		x += 1;
	}
	cout << "x = " << x << endl;
	return 0;
}