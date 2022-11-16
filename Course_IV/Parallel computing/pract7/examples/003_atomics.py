import pyopencl as cl
import numpy as np

n_threads = 100000
N = 10
a = np.zeros(10).astype(np.int32)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx, properties=cl.command_queue_properties.PROFILING_ENABLE)

mf = cl.mem_flags
a_buf = cl.Buffer(ctx, mf.COPY_HOST_PTR, hostbuf=a)

prg = cl.Program(ctx, """
    __kernel void naive(__global int *a,
    int N)
    {
      int gid = get_global_id(0);
      int pos = gid % N;
      a[pos] = a[pos] + 1;
    }
    __kernel void atomics(__global int *a,
    int N)
    {
      int gid = get_global_id(0);
      int pos = gid % N;
      atomic_inc(a+pos);
    }
    """).build()

n_workers = (n_threads,)

naive_res = np.empty_like(a)
evt = prg.naive(queue, n_workers, None, a_buf, np.int32(N))
evt.wait()
print(evt.profile.end - evt.profile.start)
cl.enqueue_copy(queue, naive_res, a_buf)
print(naive_res)

a_buf = cl.Buffer(ctx, mf.COPY_HOST_PTR, hostbuf=a)
atomics_res = np.empty_like(a)
evt = prg.atomics(queue, n_workers, None, a_buf, np.int32(N))
evt.wait()
print(evt.profile.end - evt.profile.start)
cl.enqueue_copy(queue, atomics_res, a_buf)
print(atomics_res)