import random,os

'''1) What is compound Object ?? Corelate in terms of deep and shallow copy ??
	Ans) compound objects are objects which contains objects, like lists or dict or classes.
			Shallow Copy : In shallow copy, a new object is created which contains the exact copy of the values in the original object. 
				it follows the bit-wise copy approach. In shallow copy if the field is a memory address, then the address is copied. 
				Thus if the address is changed by one object, the change gets reflected everywhere.

			Deep Copy : In deep copy, not only all the fields of an object are copied, 
						all the dynamically allocated memory address which are pointed by that object are also copied.'''


'''2) Consider This scenario
		Since both are shallow copies, why is that the dict.copy() doesn't work as expected ??'''

''' Ans) original = dict(a=1, b=2)
		>>> new = original.copy()
		>>> new.update({'c': 3})
		>>> original
		{'a': 1, 'b': 2}
		>>> new
		{'a': 1, 'c': 3, 'b': 2}

		we are creating a new dict which is a copy of the references of objects contained in the original dictionary.

		>>> original = [1, 2, 3]
		>>> new = original
		>>> new.append(4)
		>>> new, original
		([1, 2, 3, 4], [1, 2, 3, 4])

		we are creating a new reference to the the list referenced by original.'''


'''3) give programming example of nested function?? Write Fibonaci series program using nested functions??'''
def fibona(n):
	def inner(n):
		list_fib = [1]
		a,b = 0,1
		for i in range(n):
			a, b = b , a+b
			list_fib.append(b)
		print "Problem 3=>",list_fib,
	return inner(n)


'''4) write a python program to list all files contains in a directory 'MyDir' placed in your home directory'''
def files():
	try:
		location_dir = "/home/MyDir"
		a = os.listdir(location_dir)
		print "Problem 4=>", a
	except:
		print "Problem 4=> Please give the right location of your directory"


'''5) write a program which will perform certain mathematical operations. Write a program in such a manner that it should always return  something ?? Even on failure'''
def add(x,y):
	try:
		print "Problem 5=>",x+y
	except:
		print "Problem 5=>some random even num=>",random.randrange(2,100,2)


