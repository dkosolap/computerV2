import re
from modules.ComplexNum import *

class Calculator:
	def __init__(self, exc):
		self.__res = None
		if not self.__validation(exc):
			return
		self.__counting(self.__getExpression(exc))
	def __getExpression(self, exc):
		# Search complexNum and numbers	# (\d+(?:\.\d+)?(?:[\+\-])?(?:\d+(?:\.\d+)?)?[iI])|(\d+(?:\.\d+)?)
		# ((?:\d+(?:\.\d+)?(?:[\+\-])?(?:(?:\-)?\d+(?:\.\d+)?)?[iI])|(?:\d+(?:\.\d+)?))
		# ((?:\d+(?:\.\d+)?(?:[\+\-])?(?:(?:\-)?\d+(?:\.\d+)?)?[iI])|(?:(?:(?<=[\(\*\/\%\^\+])\-)?\d+(?:\.\d+)?))
		# ((?:(?:(?:\-)?\d+(?:\.\d+)?)?[iI])|(?:(?:(?<=[\(\*\/\%\^\+])\-)?\d+(?:\.\d+)?))

		# Search operators	# ([\+\-\*\/\^\%\(\)](?!\d+(?:\.\d+)?[iI]))
		# ([\+\*\/\^\%\(\)]|([\-](?<=\()))
		# (?<![\(\*\/\%\^\+])[\-]
		# ((?<![\(\*\/\%\^\+])[\-](?!\d+(?:\.\d+)?[iI]))
		# (?<![\(\*\/\%\^\+])[\-](?!\d+(?:\.\d+)?[iI])|[\+\/\*\^\%\(\)]|

		# 10+-5.5+-5+(-48-42)+5^-2-42+10.2i
		parcExc = re.findall(r'((?<![\(\*\/\%\^\+])[\-](?!\d+(?:\.\d+)?[iI])|[\+\/\*\^\%\(\)]|(?:(?:(?:\-)?\d+(?:\.\d+)?)?[iI])|(?:(?:(?<=[\(\*\/\%\^\+])\-)?\d+(?:\.\d+)?))', exc)
		numbers = []# re.findall(r'((?:\d+(?:\.\d+)?(?:[\+\-])?(?:(?:\-)?\d+(?:\.\d+)?)?[iI])|(?:(?:(?<=[\(\*\/\%\^\+])\-)?\d+(?:\.\d+)?))', exc)
		operators = []# re.findall(r'((?<![\(\*\/\%\^\+])[\-](?!\d+(?:\.\d+)?[iI])|[\+\/\*\^\%\(\)])', exc)
		output = []

		for i, val in enumerate(parcExc):
			if self.__isOperator(val):
				if val == '(':
					operators.append(val)
				elif val == ')':
					s = operators.pop()
					while s != '(':
						output.append(s)
						s = operators.pop()
				else:
					if len(operators):
						if self.__getPriority(val) <= self.__getPriority(operators[-1]):
							output.append(operators.pop())
					operators.append(val)
			else:
				output.append(parcExc[i])
		while operators:
			output += operators.pop()
		return output

	def __counting(self, exc):
		res = ComplexNum(0, 0)
		stk = []
		exc.reverse()
		while exc:
			op = exc.pop()
			if self.__isOperator(op):
				# print(stk, op)
				a = stk.pop()
				b = stk.pop()
				if re.findall('[iI]', a):
					a = ComplexNum(a)
				else:
					a = float(a)
				if re.findall('[iI]', b):
					b = ComplexNum(b)
				else:
					b = float(b)
				if op == '+':
					tmp = b + a
				elif op == '-':
					tmp = b - a
				elif op == '*':
					tmp = b * a
				elif op == '/':
					try:
						# print("Here", b, a)
						tmp = b / a
					except:
						print("Error: division by zero")
						return 
				elif op == '^':
					tmp = b ** a
				elif op == '%':
					try:
						tmp = b % a
					except:
						print("Error: module by zero")
						return 
				stk.append(str(tmp))
			else:
				stk.append(op)
		res = stk.pop()
		if type(res) is float:
			print("{0:g}".format(res))
		else:
			print("{0}".format(res))

	def __isOperator(self, c):
		return {
			'(': 1,
			')': 1,
			'+': 3,
			'-': 3,
			'*': 4,
			'/': 4,
			'%': 4,
			'^': 5,
		}.get(c, False)
	def __getPriority(self, c):
		return {
			'(': 0,
			')': 1,
			'+': 3,
			'-': 3,
			'*': 4,
			'/': 4,
			'%': 4,
			'^': 5,
		}.get(c, 6)
	def res(self):
		return self.__res

# VALIDATION
	def __validation(self, exc):
		def checkBrackets(exc):
			checkLeft = re.findall(r'\(', exc)
			checkRight = re.findall(r'\)', exc)
			if len(checkLeft) != len(checkRight):
				raise SyntaxError("wrong pair rackets")
		def withoutNumber(exc):
			check = re.findall(r'\d+', exc)
			if not check:
				raise SyntaxError("wrong amount numbers")
		def operWithotPair(exc):
			# check = re.findall(r'[\+\-\\\*\^\%]{2,}', exc)
			check = re.findall(r'[\+\\\*\^\%]]{2,}|(?:\--)|(?:[\+\-\\\*\^\%]{3,})', exc)
			if check:
				raise SyntaxError("wrong amount operator")
			check = re.findall(r'[\*\-\+\^\*\\\%]$', exc)
			if check:
				raise SyntaxError("wrong number of arguments in statement".format(check[0]))
			check = re.findall(r'[\*\-\+\^\*\\\%](?=\))', exc)
			if check:
				raise SyntaxError("wrong number of arguments in statement".format(check[0]))
			check = re.findall(r'(^[\*\^\*\\\%])|(\([\*\^\*\\\%])', exc)
			if check:
				raise SyntaxError("wrong amount operator")
		try:
			checkBrackets(exc)
			withoutNumber(exc)
			operWithotPair(exc)
		except SyntaxError as err:
			print(err)
			return 0
		return re.sub(r' ', '', exc)
