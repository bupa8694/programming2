#!/usr/bin/env python3

from integer import Integer

def main():
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())

if __name__ == '__main__':
	main()