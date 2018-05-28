import re
from multimethod import multimethod

class Matrix(object):
	"""docstring for Matrix"""
# INIT STR
	@multimethod
	def __init__(self: object, arg: str):
		self.i = len(re.findall(r'\[', arg)) - 1
		tmp = re.findall(r'([\-]?\d+(?:\.\d+)?)', arg)
		self.j = int(len(tmp) / self.i)
		self.arr = []
		k = 0
		for i in range(0,int(self.i)):
			col = []
			for j in range(0,int(self.j)):
				pass
				col.append(float(tmp[k]))
				k += 1
			self.arr.append(col)
		# print(self.i, self.j, self.arr, arg)
		# print(len(self.arr))
# INIT ARRAY
	@multimethod
	def __init__(self: object, arg: object):
		self.i = len(arg)
		try:
			self.j = len(arg[0])
		except:
			print("Error: need matrix")
			return
		self.arr = arg
		# print(self.i, self.j, self.arr)
# STR
	def __str__(self):
		res = ''
		for i in range(0,int(self.i)):
			res += '[ '
			for j in range(0,int(self.j)):
				res += "{0:g}".format(self.arr[i][j])
				if j < self.j - 1:
					res += ', '
			res += ' ]'
			if i < self.i - 1:
				res += '\n'
		return res
# ADD
	def __add__(self, other):
		if self.i == other.i and self.j == other.j:
			newArr = []
			for i in range(0,int(self.i)):
				col = []
				for j in range(0,int(self.j)):
					col.append(self.arr[i][j] + other.arr[i][j])
				newArr.append(col)
			return Matrix(newArr)
		else:
			print("Error: not supported")
		return
# SUB
	def __sub__(self, other):
		if self.i == other.i and self.j == other.j:
			newArr = []
			for i in range(0,int(self.i)):
				col = []
				for j in range(0,int(self.j)):
					col.append(self.arr[i][j] - other.arr[i][j])
				newArr.append(col)
			return Matrix(newArr)
		else:
			print("Error: not supported")
		return
# MUL FLOAT
	@multimethod
	def __mul__(self: object, k: float):
		# if self.i != other.j and self.j != other.i:
			# print("Error: not supported!")
			# return
		newArr = []
		for i in range(0,int(self.i)):
			col = []
			for j in range(0,int(self.j)):
				col.append(self.arr[i][j] * k)
			newArr.append(col)
		return Matrix(newArr)
# MUL OBJEXT
	@multimethod
	def __mul__(self: object, k: object):
		print("Error: not supported")
		return

