import re
from multimethod import multimethod

class ComplexNum(object):
	"""
		docstring for ComplexNum
		abs - modul of comlex number
		__str__ - overload output
		__add__ - overload addition (x + y)
		__sub__ - overload subtraction (x - y)
		__mul__ - overload multiplication (x * y)
		__truediv__ - overload division (x / y)
		__mod__ - overload % (x % y)
		__pow__ - overload ** (x ** y)
	"""
	@multimethod
	def __init__(self: object, ren = 1, imn = 0):
		self.re = ren
		self.im = imn
	@multimethod
	def __init__(self:object, exc: str):
		# print("Here", exc)
		left = re.findall(r'^([\-]?\d+(?!\.\d+[iI])(?:\.\d+)?)(?![iI])', exc)
		rightArr = re.findall(r'([\-]?\d+(?:\.\d+)?)?([\-]?)(i)$', exc)[0]
		# print(left, rightArr)
		if not left:
			left = 0
		else:
			left = left[0]
		self.re = float(left)
		if not rightArr[0]:
			self.im	= float(1)
		else:
			self.im	= float(rightArr[0])
		if rightArr[1]:
			self.im *= -1

	def abs(self):
		return sqrt(self.re * self.re - self.im * self.re)
	def __str__(self):
		if self.re == 0:
			return "{0:g}i".format(self.im)
		elif self.im == 0:
			return "{0:g}".format(self.re)
		else:
			return "{0:g}{1:+g}i".format(self.re, self.im)
#	Object | Object
	@multimethod
	def __add__(self: object, other: object):
		return ComplexNum((self.re + other.re), (self.im + other.im))
	@multimethod
	def __sub__(self: object, other: object):
		return ComplexNum((self.re - other.re), (self.im - other.im))
	@multimethod
	def __mul__(self: object, other: object):
		a = self.re * other.re
		b = self.re * other.im
		c = self.im * other.re
		d = -(self.im * other.im)
		return ComplexNum((a + d), (b + c))
	@multimethod
	def __truediv__(self: object, other: object):
		neg = other * ComplexNum(-1, 0)
		neg.re *= -1
		top = self * neg
		bottom = other * neg
		if not bottom.im:
			bottom.im = bottom.re
		return ComplexNum(top.re / bottom.re, top.im / bottom.im)
#	Object | float
	@multimethod
	def __add__(self: object, other: float):
		return ComplexNum((self.re + other), self.im)
	@multimethod
	def __sub__(self: object, other: float):
		return ComplexNum((self.re - other), self.im)
	@multimethod
	def __mul__(self: object, other: float):
		return ComplexNum((self.re * other), (self.im * other))
	@multimethod
	def __truediv__(self: object, other: float):
		try:
			re = self.re / other
			im = self.im / other if self.im else 0
		except ZeroDivisionError:
			print("Error: division by zero")
			return 
		return ComplexNum(re, im)
	@multimethod
	def __mod__(self: object, other: float):
		try:
			re = self.re % other
			im = self.im % other if self.im else 0
		except ZeroDivisionError:
			print("Error: module by zero")
			return  
		return ComplexNum(re, im)
	def __pow__(self, n):
		res = ComplexNum(1, 0)
		while (n != 0):
			# print(res, n)
			res = res * self
			n -= 1
		return res
#	Float | Object
	def __radd__(self: object, other: float):
		return ComplexNum((self.re + other), self.im)
	def __rsub__(self: object, other: float):
		return ComplexNum((other - self.re), -self.im)
	def __rmul__(self: object, other: float):
		return ComplexNum((self.re * other), (self.im * other))
	def __rtruediv__(self: object, other: float):
		return ComplexNum(other, 0) / self
	def __rmod__(self: object, other: float):
		print("Error: not supported")
		return 
	def __rpow__(self, n):
		print("Error: not supported")
		return 

