#!/usr/bin/python3

def dictionaryTest():
	fish = {}
	fish['one'] = 'shark'
	fish['four'] = 'whale'
	fish[4] = 'dolphin'
	fish[3] = 'tuna'
	print("fish['one']:", end = ''); print(fish['one'])
	print("fish['four']:", end = '');print(fish['four'])
	print("fish[4]:", end = '');print(fish[4])
	print("fish[3]:", end = '');print(fish[3])

	placename = {'asia' : 'china', 'europe': 'english', 'north america':'america', 'fruit': 'apple'}
	print("placename:", end = ''); print(placename)
	print("placename['north america']:", end = ''); print(placename['north america'])
	print('placename.keys():', end = ''); print(placename.keys())
	print('placename.values():', end = ''); print(placename.values())

def setTest():
	country = {'china', 'korea', 'chian', 'italy', 'indian', 'japan', 'north korea', 'america', 'england'}
	print("country:", end = ''); print(country)
	if 'indian' in country:
		print('the set of country is include indian')
	else:
		print('the set of country is not include indian')
	
	fruit0 = set('applepear')
	fruit1 = set('applegrape')

	print('set fruit0:', end = '');print(fruit0)
	print('set fruit1:', end = '');print(fruit1)
	
	print('fruit0 - fruit1:', end = '');print(fruit0- fruit1)
	print('fruit1 - fruit0:', end = '');print(fruit1- fruit0)
	print('fruit0 | fruit1:', end = '');print(fruit0| fruit1)
	print('fruit0 & fruit1:', end = '');print(fruit0& fruit1)
	print('fruit0 ^ fruit1:', end = '');print(fruit0^ fruit1)
	

def tupleTest():
	tuple0 = ("atlantic", 34, 'asia', "europe", 'north america', 'oceania', 'antarctica')
	tuple1 = ('atlantic ocean', 'pacific ocean', 'indian ocean', 'arctic ocean', 'antarctic ocean')
	tuple2 = tuple0 + tuple1

	print("output tuple0:", end = '');print(tuple0)
	print("output tuple1:", end = '');print(tuple1)
	print("output tuple2:", end = '');print(tuple2)

	print("outout tuple[2]:", end = '');print(tuple0[2])
	print("output tuple2[3:9]:", end = '');print(tuple2[3:9])
	print("tuple2[:6]:", end = '');print(tuple2[:6])
	print("tuple2[5:8]:", end = '');print(tuple2[5:8])
	print("tuple2[2:9:2]:", end = '');print(tuple2[2:9:2])
	print("tuple2[-1:-9:3]:", end = '');print(tuple2[-1:-9:-2])

def varAssign():
	a, b , c = 10, 2.5, "pear"
	print(a); print(b); print(c)
	print(type(a));print(type(b)); print(type(c))
	a1 = isinstance(a, int)
	b1 = isinstance(b, str)
	print(type(a1));print(a1)
	print(type(b1));print(b1)

def numericCalculation(a,b):
	#a = 10
	#b = 30
	a = a + b #addition
	b = a - b #subtraction
	print("a,b additon subtraction: ");print(a);print(b)
	a = a * b #multiplication
	b = a / b  #division method
	print("multiplication division :");print(a); print(b)
	a = 10 // 3 #division method and get a integer
	b = 10 % 3 #division method and then get a remainder
	c = 2 ** 4 #4th power of 2 
	print("division get integer and get remainder:");print(a);print(b)
	print(c)
	c = True
	return c

def stringTest():
	str = "bananapeargrape"
	
	#print("str %s\n", str)
	print("str:%s" % str)
	print("str[0:-1]:%s" % str[0:-1])
	print("str[0]:%c" % str[0])
	print("str[2:5]:%s" % str[2:5])
	print("str[2:]:%s" % str[2:])
	print("str*2:%s" % str*2)
	print('str + "TEST":%s' % str + "TEST")
	
def listTest():
	list0 = ["pear", 123, 'apple', 15.6, "banana", 'orange', "pineapple"]
	list1 = [89, 13.2, "grape", 'mango']
	
	print("output list0:", end = '');print(list0)
	print("output list1:", end = '');print(list1)
	
	print("list0[0]:", end = ''); print(list0[0])
	list0[0] = 50
	print("change list0[0]:", end = ''); print(list0[0])
	print("list0[2:6]:", end = ''); print(list0[2:6])
	print("list0[3:]:", end = ''); print(list0[3:])
	print("list0[:5]:", end = ''); print(list0[:5])
	list2 = list0 + list1
	print("list0 + list1:", end = ''); print(list2)
	print("list2[3:7:2]:", end = ''); print(list2[3:7:2])
	print("list2[-1:-5:-2]:", end = ''); print(list2[-1:-5:-2])

def listTest1():
	list3 = [1,2,3,4,5,6]
	print('list3:', list3)
	print('list3**2:', [x**2 for x in list3])
	print('list3**2 >5 :', [x**2 for x in list3 if x > 2])
	print('list3*5 to dict:', dict([(x,x*5) for x in list3]))
	print('[(x,y) for x in range(10) if x > 2 for y in range(10) if y%2]:')	
	print([(x,y) for x in range(10) if x > 2 for y in range(10) if y%2])

	vec0 = [2,3,4]
	vec1 = [5,6,7]
	print('vec0:', vec0)
	print('vec1:', vec1)
	print('vec0[i]+vec1[i]:',[vec0[i]+vec1[i] for i in range(len(vec0))])

	print('vec0[i] * vec1[i]:', [x*y for x in vec0 for y in vec1])


def dataType():
	counter = 12 #integer variable
	mile = 24.5  #float variable
	name  = "apple" #string variable

	print(counter)
	print(mile)
	print(name)

	varAssign()

