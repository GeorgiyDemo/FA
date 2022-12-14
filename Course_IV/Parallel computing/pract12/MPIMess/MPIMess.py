from mpi4py import MPI
from numpy import empty , array , int32 , float64 , dot

# определяем коммуникатор comm – группу процессов, которые участвуют в вычислениях
comm = MPI. COMM_WORLD
# rank применяется для указания номера процесса
rank = comm.Get_rank()


numprocs = comm.Get_size()

#Если номер процесса 0
if rank == 0:
  f1 = open('in.dat', 'r')
  N = array(int32(f1. readline ()))
  M = array(int32(f1. readline ()))
  f1.close ()

#Если не 0
else:
  N = array (0, dtype=int32)
  M = array (0, dtype=int32)

if rank == 0:
  comm.send (M, dest =1, tag =0)

else:
  N = comm.recv (source =0, tag =0)

print (f'Variable N on process {rank} is: {N}')