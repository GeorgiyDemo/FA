from mpi4py import MPI
from numpy import empty , array , int32 , float64 , dot

comm = MPI. COMM_WORLD
rank = comm. Get_rank ()
size = comm. Get_size ()


numprocs = comm. Get_size ()

if rank == 0: 
    array_share = [ 0 ]
    for i in range(1,size): 
        array_share.append( i )

else: 
    array_share = None


# Отсылка по элементу из массива всем процессам, в т.ч. и себе
recvbuf = comm.scatter(array_share, root=0)

# вычисляем по значению в каждом процессе
calcVal = recvbuf * 2

# собираем результат обратно в вектор
recv_arr = comm.gather(calcVal, root=5)

if rank == 5: 
  for i in range(0,size): 
       # выводим поэлементно полученный вектор
       print(" process %s receiving %s from process %s"  %(rank , recv_arr[i] , i))
