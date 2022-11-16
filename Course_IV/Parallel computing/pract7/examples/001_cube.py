import pyopencl as cl
import numpy as np

a = np.arange(32).astype(np.float32)
res = np.empty_like(a)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
a_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
dest_buf = cl.Buffer(ctx, mf.WRITE_ONLY, res.nbytes)

prg = cl.Program(ctx, """
    __kernel void sq(__global const float *a,
    __global float *c)
    {
      int gid = get_global_id(0);
      c[gid] = a[gid] * a[gid];
    }
    """).build()

prg.sq(queue, a.shape, None, a_buf, dest_buf)

cl.enqueue_copy(queue, res, dest_buf)

print(a, res)