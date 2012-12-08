import numpy as np
import pycuda.autoinit
import pycuda.compiler as nvcc
import pycuda.gpuarray as gpu


class DataHandler: 

	def __init__(self, data):

		#push data to the gpu
		data = np.float64(data)
		self.data_d = gpu.to_gpu(data)

	def shape():
		return self.data_d.shape

	def purity():
		purity_kernel_source =\
		"""
		__global__ void purity_kernel(float *data, int h, int w){

			int iy = blockDim.y * blockIdx.y + threadIdx.y;
			int ix = blockDim.x * blockIdx.x + threadIdx.x;
			int idx = iy * w + ix;

		}
		"""

		#pull data from gpu


	def split(predicate):
		split_kernel_source = \
		"""
		__global__ void split_kernel(float *data, int h, int w){

			int iy = blockDim.y * blockIdx.y + threadIdx.y;
			int ix = blockDim.x * blockIdx.x + threadIdx.x;
			int idx = iy * w + ix;

		}
		"""

		split_kernel = cuda_compile(split_kernel_source, "split_kernel")

		# x,y = 32,32
		# blocksize = (x,y,1)
		# gridsize  = (int(np.ceil(float(w)/x)), int(np.ceil(float(h)/y)))
		# energy_kernel(energy_d, im_d, size, h, w, block=blocksize, grid=gridsize)


	def cuda_compile(source_string, function_name):
		# Compile the CUDA Kernel at runtime
		source_module = nvcc.SourceModule(source_string)
		# Return a handle to the compiled CUDA kernel
		return source_module.get_function(function_name)