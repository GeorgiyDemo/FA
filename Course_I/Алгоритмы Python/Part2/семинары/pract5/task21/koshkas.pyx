#python3 setup.py build_ext --inplace

import numpy

cdef int carr[2001]
cdef int [:] carr_view = carr

cpdef int[:] generator():
    cdef int [:] arr = carr_view
    for i in range(arr.shape[0]):
        arr[i] = numpy.random.randint(-5,4)
    return arr


cpdef tuple summ():
    cdef int [:] arr = generator()

    cdef size_t i
    cdef int zeros = 0
    cdef int negative = 0
    cdef int positive = 0

    l = arr.shape[0]
    for i in range(l):
        if arr[i] > 0:
            positive += 1
    
    for i in range(l):
        if arr[i] < 0:
            negative += 1
    
    for i in range(l):
        if arr[i] == 0:
            zeros += 1

    return positive, negative, zeros


cpdef tuple DEMKACython():
    return summ()

