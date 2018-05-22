import re

class Calculator:
	def __init__(self, exc):
		self.__res = None\
		# self.__stackNum = []
		# self.__stackOper = []
		if not self.__validation(exc):
			return
		self.__getExpression(exc)
		# self.__counting(self.__getExpression(exc))
		





	def __getExpression(self, exc):
		# Search complexNum and numbers	# (\d+(?:\.\d+)?(?:[\+\-])?(?:\d+(?:\.\d+)?)?[iI])|(\d+(?:\.\d+)?)
										# ((?:\d+(?:\.\d+)?(?:[\+\-])?(?:(?:\-)?\d+(?:\.\d+)?)?[iI])|(?:\d+(?:\.\d+)?))

		# Search operators	# ([\+\-\*\/\^\%\(\)](?!\d+(?:\.\d+)?[iI]))
							# ([\+\*\/\^\%\(\)]|([\-](?<=\()))
							# (?<![\(\*\/\%\^\+])[\-]
							# ((?<![\(\*\/\%\^\+])[\-](?!\d+(?:\.\d+)?[iI])|[\+\/\*\^\%\(\)])

		# 10+-5.5+-5+(-48-42)+5^-2-42+10.2i
		numbers = re.findall(r'((?:\d+(?:\.\d+)?(?:[\+\-])?(?:(?:\-)?\d+(?:\.\d+)?)?[iI])|(?:(?:(?<=[\(\*\/\%\^\+])\-)?\d+(?:\.\d+)?))', exc)
		operators = re.findall(r'((?<![\(\*\/\%\^\+])[\-](?!\d+(?:\.\d+)?[iI])|[\+\/\*\^\%\(\)])', exc)
		output = []
		print(numbers, operators)
	# def __getExpression(self, exc):
	# 	operStack = []
	# 	i = 0
	# 	lenth = len(exc)
	# 	output = ''
	# 	while i < lenth:
	# 		if exc[i].isdigit():
	# 			num = ''
	# 			while i < lenth and (exc[i].isdigit() or exc[i] == '.'):
	# 				output += exc[i]
	# 				i += 1
	# 			output += ' '
	# 			i -= 1
	# 		if self.__isOperator(exc[i]):
	# 			if exc[i] == '(':
	# 				operStack.append(exc[i])
	# 			elif exc[i] == ')':
	# 				s = operStack.pop()
	# 				while s != '(':
	# 					output += s + ' '
	# 					s = operStack.pop()
	# 			else:
	# 				if len(operStack) > 0:
	# 					if self.__getPriority(exc[i]) <= self.__getPriority(operStack[-1]):
	# 						output += operStack.pop()
	# 				operStack.append(exc[i])
	# 		i += 1
	# 	while len(operStack) > 0:
	# 		output += operStack.pop() + ' '
	# 	print(output)
	# 	return output




	def __counting(self, exc):
		res = 0
		temp = []
		i = 0
		lenth = len(exc)
		while i < lenth:
			if exc[i].isdigit() or exc[i] == '.':
				a = ''
				while i < lenth and (exc[i].isdigit() or exc[i] == '.'):
					 a += exc[i]
					 i += 1
				temp.append(float(a))
				i -= 1
			elif self.__isOperator(exc[i]):
				a = temp.pop()
				if not len(temp):
					b = 0
				else:
					b = temp.pop()

				if exc[i] == '+':
					res = float(b) + float(a)
				elif exc[i] == '-':
					res = float(b) - float(a)
				elif exc[i] == '*':
					res = float(b) * float(a)
				elif exc[i] == '/':
					res = float(b) / float(a)
				elif exc[i] == '^':
					res = float(b) ** float(a)
				elif exc[i] == '%':
					res = float(b) % float(a)
				temp.append(res)
				# print("{0} {2} {1}".format(b, a, exc[i]))
			i += 1
		self.__res = temp.pop()
		print("{0:g}".format(self.__res))
	def __isDelimeter(self):
		pass
	def __isOperator(self, c):
		exc = re.search(r'[+-/*^()%]', c)
		if exc:
			return True
		return False
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
