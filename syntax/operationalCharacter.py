#!/usr/bin/python3

def logicOperator():
	a = 20
	b = 10
	
	print('a = ', end = '');print(a)
	print('b = ', end = '');print(b)
	if(a and b):
		print("1 - a,b all true")
	else:
		print("1 - a and b at least one is false ")

	if(a or b):
		print("2 - a and b at least one is true")
	else:
		print('2 - a and b all is false')

	c = 0
	if(not c):
		print('c = 0')
	else:
		print('c != 0')

def memberOperator():
	a = 1
	b = 20
	list = [1,2,3,4,5,6];

	print('list:', end = '');print(list)
	print('a = ', end = '');print(a)
	print('b = ', end = '');print(b)

	if(a in list):
		print("1 - a is  in list")
	else:
		print('1 - a not in list')
	
	if(b not in list):
		print('2 - b is not in list')
	else:
		print('2 - b is in list')

	a = 50
	print('a = ', end = '');print(a)
	print('b = ', end = '');print(b)
	if(a not in list):
		print('a = 50 is not in list')
	else:
		print('a = 50 is in list')
	
	b = 50
	print('a = ', end = '');print(a)
	print('b = ', end = '');print(b)
	
	if(a is b):
		print('1 - a and b have same id')
	else:
		print('1 - a and b have not same id')

	
	if(id(a) == id(b)):
		print('2 - a and b have same id')
	else:
		print('2 - a and b have not same id')

	b = 20
	
	print('a = ', end = '');print(a)
	print('b = ', end = '');print(b)
	if(a is b):
		print('3 - a and b have same id')
	else:
		print('3 - a and b have not same id')

	if(id(a) == id(b)):
		print('4 - a and b have same id')
	else:
		print('4 - a and b have not same id')
