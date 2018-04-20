#!/usr/bin/env python3.6

import sys
import readline
import re

from modules.Calculator import *

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
		lst = Calculator(self.__comand)

def main():
	g = General()
	g.start()

if __name__ == "__main__":
	main()
