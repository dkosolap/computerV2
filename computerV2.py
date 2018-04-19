#!/usr/bin/env python3.6

import sys
import readline
import re

class RPN:
	def __init__(self, exc):
		self.__operStack = []
		self.__numberStack = []
		self.__input = self.__getExpression(exc)
		return self.__counting()
	def __getExpression(self, exc):
		i = 0
		lenth = len(exc)
		output = ''
		while i < lenth:
			if exc[i].isdigit():
				num = ''
				while i < lenth and (exc[i].isdigit() or exc[i] == '.'):
					output += exc[i]
					i += 1
				output += ' '
				i -= 1
			if self.__isOperator(exc[i]):
				if exc[i] == '(':
					self.__operStack.append(exc[i])
				elif exc[i] == ')':
					s = self.__operStack.pop()
					while s != '(':
						output += s + ' '
						s = self.__operStack.pop()
				else:
					if len(self.__operStack) > 0:
						if self.__getPriority(exc[i]) <= self.__getPriority(self.__operStack[-1]):
							output += self.__operStack.pop()
					self.__operStack.append(exc[i])
			i += 1
		while len(self.__operStack) > 0:
			output += self.__operStack.pop() + ' '
		print(output)

	def __counting(self):
		pass
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
		    '+': 2,
		    '-': 3,
		    '*': 4,
		    '/': 4,
		    '^': 4,
		    '%': 5,
		}.get(c, 6)
		

class General:
	def __init__(self):
		pass
	def start(self):
		while True:
			try:
				self.__comand = input()
			except EOFError:
				break
			except :
				print("(interrupt) use CTRL + D for exit")
			else:
				self.__pars()
		print("\nThx for wasted time!")
	def __pars(self):
		self.__comand = re.sub(r'\s', '', self.__comand).lower()
		# print(self.__comand)
		lst = RPN(self.__comand)



def main():
	g = General()
	g.start()

if __name__ == "__main__":
	main()
