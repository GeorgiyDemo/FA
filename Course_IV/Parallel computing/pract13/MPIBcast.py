from mpi4py import MPI
from numpy import empty , array , int32 , float64 , dot

comm = MPI. COMM_WORLD
rank = comm. Get_rank ()

numprocs = comm. Get_size ()

if rank == 0: 
    variable_to_share = 100      
else: 
    variable_to_share = None

# Отсылка значения всем, в т.ч. и себе
variable_to_share = comm.bcast(variable_to_share, root=0) 

print("process = %d" %rank + " variable shared  = %d " %variable_to_share)
