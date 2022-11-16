import pyopencl as cl
import numpy as np

N = 32
a = np.random.rand(N,N,4).astype(np.float32)
res = np.empty((N,N,1)).astype(np.float32).flatten()

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
a_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a.flatten())
dest_buf = cl.Buffer(ctx, mf.WRITE_ONLY, res.nbytes)

prg = cl.Program(ctx, """
    __kernel void sq(__global float4 *a,
    __global float *c)
    {
      int gid = get_global_id(0);
      float4 pix = a[gid];
      c[gid] = .299f * pix.x + .587f * pix.y + .114f * pix.z;
    }
    """).build()

n_workers = (N*N,)
prg.sq(queue, n_workers, None, a_buf, dest_buf)

cl.enqueue_copy(queue, res, dest_buf)

ref = .299*a[:,:,0] + .587*a[:,:,1] + .114*a[:,:,2]
print(np.allclose(res, ref.flatten()))