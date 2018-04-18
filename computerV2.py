#!/usr/bin/env python3.6

import sys
import readline

def main():
	while True:
		try:
			comand = input()
		except EOFError:
			break
		except :
			print("(interrupt) use CTRL + D for exit")
		else:
			print(comand)
	print("\nThx for wasted time!")

if __name__ == "__main__":
	main()
