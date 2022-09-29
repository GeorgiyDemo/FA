#include <iostream>
#include <omp.h>
#include <string>

using namespace std;

int main()
{
    string hw = "Hello World!\n";
#pragma omp parallel shared(hw)
     {
      cout << hw;
     }
    return 0;
}