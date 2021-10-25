""" Python interface to the C++ Integer class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libinteger.so')

class Integer(object):
	def __init__(self, val):
		lib.Integer_new.argtypes = [ctypes.c_int]
		lib.Integer_new.restype = ctypes.c_void_p
		lib.Integer_get.argtypes = [ctypes.c_void_p]
		lib.Integer_get.restype = ctypes.c_int
		lib.Integer_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Integer_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Integer_new(val)

	def get(self):
		return lib.Integer_get(self.obj)

	def set(self, val):
		lib.Integer_set(self.obj, val)
        
	def __del__(self):
		return lib.Integer_delete(self.obj)