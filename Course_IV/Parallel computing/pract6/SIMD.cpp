#include <iostream>
#include <chrono>
const int n = 20000;
using namespace std;

int main()
{
	int i, j;
	float* a = new float[n*n];

    chrono::steady_clock sc;   // create an object of `steady_clock` class
   auto start = sc.now();     // start timer


	for (int i = 0; i < n*n; i++)
		a[i] = 1.0f;
	for (int k = 0; k < 1; k++)
	{
		for (int i = 1; i < 3; i++)
			for (int j = 0; j < n; j++)
			{
				a[n*i + j] = a[n*i + j - (i + 1) - 1] / (a[n*i + j - (i + 1)] * a[n*i + j - (i + 1)]) + 1;
			}
		for (int i = 3; i < n; i++)
#pragma omp simd safelen(4)			
			for (int j = 0; j < n; j++)
			{
				a[n*i + j] = a[n*i + j - (i + 1) - 1] / (a[n*i + j - (i + 1)] * a[n*i + j - (i + 1)]) + 1;
			}
	}

    auto end = sc.now();       // end timer (starting & ending is done by measuring the time at the moment the process started & ended respectively)
   auto time_span = static_cast<chrono::duration< double > >(end - start);   // measure time span between start & end
   cout<<"Operation took: "<<time_span.count()<<" seconds !!!";

	/*
    cout << "example2_vec" << endl;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << a[i*n + j] << " ";
		}
		cout << endl;
	}
    */

   
   return 0;
}