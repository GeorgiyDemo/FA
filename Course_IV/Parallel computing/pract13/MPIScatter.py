from mpi4py import MPI
from numpy import empty , array , int32 , float64 , dot

comm = MPI. COMM_WORLD
rank = comm. Get_rank ()

numprocs = comm. Get_size ()

if rank == 0: 
    array_to_share = [1, 2, 3, 4 ,5 ,6 ,7, 8]
else: 
    array_to_share = None


# Отсылка по элементу из массива всем процессам, в т.ч. и себе
recvbuf = comm.scatter(array_to_share, root=0)

print("process = %d" %rank + " recvbuf = %d " %recvbuf)