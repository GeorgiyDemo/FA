import pyopencl as cl
import numpy as np
import Image as im

def show_single_buffer(queue, n_pix, buffer):
	temp = np.empty(n_pix).astype(np.uint8)
	cl.enqueue_copy(queue, temp, buffer)
	test = im.new('L', cat.size)
	test.putdata(temp)
	test.show()

cat = im.open('data/cat.jpg').convert('RGBA')
pix = np.array(list(cat.getdata())).astype(np.uint8)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

prg = cl.Program(ctx, """
    __kernel void sep_channels(__global uchar4 *a,
            __global uchar *r,
            __global uchar *g,
            __global uchar *b)
    {
      int gid = get_global_id(0);
      r[gid] = a[gid].x;
      g[gid] = a[gid].y;
      b[gid] = a[gid].z;
    }
    __kernel void mer_channels(__global uchar4 *a,
            __global uchar *r,
            __global uchar *g,
            __global uchar *b)
    {
      int gid = get_global_id(0);
      a[gid].x = r[gid];
      a[gid].y = g[gid];
      a[gid].z = b[gid];
      a[gid].w = 255;
    }
    __kernel void blur_channel(__global uchar *c,
            __global uchar *res,
            uint w, uint h)
    {
      uint xp = get_global_id(0);
      uint yp = get_global_id(1);
      uint left = clamp(xp-1, (uint)0, w);
      uint right = clamp(xp+1, (uint)0, w);
      uint top = clamp(yp-1, (uint)0, h);
      uint bot = clamp(yp+1, (uint)0, h);
      uchar blr = 0.2*c[xp+w*top] +
                  0.2*c[left+w*yp] +
                  0.2*c[xp+w*yp] +
                  0.2*c[right+w*yp] +
                  0.2*c[xp+w*bot];
      res[xp+w*yp] = blr;
    }
    """).build()

n_pix = cat.size[0]*cat.size[1]
result = np.empty_like(pix)
mf = cl.mem_flags
pix_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=pix)
r_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
g_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
b_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
rb_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
gb_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
bb_buf = cl.Buffer(ctx, mf.READ_WRITE, size=n_pix)
pixb_buf = cl.Buffer(ctx, mf.WRITE_ONLY | mf.COPY_HOST_PTR, hostbuf=result)

n_workers = (cat.size[0]*cat.size[1],)
prg.sep_channels(queue, n_workers, None, pix_buf, r_buf, g_buf, b_buf)

n_workers = (cat.size[0], cat.size[1])
prg.blur_channel(queue, n_workers, None, r_buf, rb_buf, np.uint32(cat.size[0]), np.uint32(cat.size[1]))
prg.blur_channel(queue, n_workers, None, g_buf, gb_buf, np.uint32(cat.size[0]), np.uint32(cat.size[1]))
prg.blur_channel(queue, n_workers, None, b_buf, bb_buf, np.uint32(cat.size[0]), np.uint32(cat.size[1]))

#show_single_buffer(queue, n_pix, r_buf)
#show_single_buffer(queue, n_pix, rb_buf)

n_workers = (cat.size[0]*cat.size[1],)
prg.mer_channels(queue, n_workers, None, pixb_buf, rb_buf, gb_buf, bb_buf)

cl.enqueue_copy(queue, result, pixb_buf)

im_data = [ (p[0], p[1], p[2], p[3]) for p in result ]
cat.putdata(im_data)
cat.show()