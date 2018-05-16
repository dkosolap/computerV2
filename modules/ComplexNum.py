import re

class ComplexNum(object):
	"""docstring for ComplexNum"""
	"""	abs - modul of comlex number"""
	"""	__str__ - overload output"""
	"""	__add__ - overload addition (x + y)"""
	"""	__sub__ - overload subtraction (x - y)"""
	"""	__mul__ - overload multiplication (x * y)"""
	"""	__truediv__ - overload division (x / y)"""
	"""	__mod__ - overload % (x % y)"""
	"""	__pow__ - overload ** (x ** y)"""

	def __init__(self, re = 1, im = 0):
		self.re = re
		self.im = im
	def abs(self):
		return sqrt(self.re * self.re - self.im * self.re)
	def __str__(self):
		if self.re == 0:
			return "{0:g}i".format(self.re)
		elif self.im == 0:
			return "{0:g}".format(self.re)
		else:
			return "{0:g}{1:+g}i".format(self.re, self.im)
	def __add__(self, other):
		return ComplexNum((self.re + other.re), (self.im + other.im))
	def __sub__(self, other):
		return ComplexNum((self.re - other.re), (self.im - other.im))
	def __mul__(self, other):
		return ComplexNum((self.re * other.re), (self.im * other.im))
	def __truediv__(self, other):
		return ComplexNum((self.re / other.re), (self.im / other.im))
	# def __mod__(self, other):
	# def __pow__(self, other):
		# pass
