import numpy as np
import pycuda.autoinit
import pycuda.compiler as nvcc
import pycuda.gpuarray as gpu

from ..datahandler_base import DataHandlerBase

class DataHandlerCUDA(DataHandlerBase): 

	def __init__(self, data):
		#push data to the gpu
		data = np.float64(data)
		self.data_d = gpu.to_gpu(data)
		#compile kernels
		self.split_kernel = self.cuda_compile(split_kernel_source, "split_kernel")
		self.purity_kernel = self.cuda_compile(purity_kernel_source, "purity_kernel")

	def shape():
		return self.data_d.shape

	def purity(indices_d, results_d):
		n, f = self.shape()
		height, width = np.int32(indices_d.shape())

		x = 32
		blocksize = (x,1,1)
		gridsize  = (int(np.ceil(float(height)/x)), 1)

		self.purity(self.data_d, indices_d, results_d, n, f, blocksize=blocksize, gridsize=gridsize)


	def split(indices_d, results_d, feature, threshold):

		feature = np.int32(feature)
		threshold = np.float64(threshold)

		n, f = self.shape()
		height, width = np.int32(indices_d.shape())

		x = 32
		blocksize = (x,1,1)
		gridsize  = (int(np.ceil(float(height)/x)), 1)

		self.split_kernel(self.data_d, indices_d, results_d, feature, threshold, height, n, f, blocksize=blocksize, gridsize=gridsize)


	def cuda_compile(source_string, function_name):
		# Compile the CUDA Kernel at runtime
		source_module = nvcc.SourceModule(source_string)
		# Return a handle to the compiled CUDA kernel
		return source_module.get_function(function_name)





