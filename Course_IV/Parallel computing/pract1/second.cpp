#include <omp.h>
#include <iostream>

static const int N = 16;
int main(){
    int is_cpu = true;
    int *data = static_cast<int*>(malloc(N * sizeof(int)));
    for(int i=0; i<N; i++) data[i] = i;

    #pragma omp target map(from:is_cpu) map(tofrom:data[0:N])
    {
        is_cpu=omp_is_initial_device();
        #pragma omp parallel for
        for (int i=0; i<N; i++)
            data[i] *= 2;
    }

    printf ("Running on %s\n", (is_cpu?"CPU":"GPU"));
    for(int i=0; i<N; i++) std::cout << data[i] << std::endl;

    free(data);
    return 0;
}
