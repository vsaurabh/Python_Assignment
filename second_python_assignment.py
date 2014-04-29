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


'''6) Write a program for following outputs by using map?
       a. output is [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
       b. output is  [3, 5, 7, 9, 15]'''
def evnodd(x):
    if x%2==0:
        return 1
    else:
        return 0

print "Problem 6 (a) =>", map(evnodd, range(10))
print "Problem 6 (b) =>", map(lambda x: x+2,range(1,9,2))

'''7) Write Fibonacci series program by using filter ?'''
def fibFilter(n):
    a, b = 0, 1
    for i in range(n):
    	a, b = a+b, a
    print a,
print "Problem 7=>",filter(fibFilter,range(10))


'''8) Write a program to determine the maximum of a list of numerical values by using reduce ?'''
def maxList(l):
	try:
		a = reduce(lambda a,b: a if(a>b)else b, l)
		print "Problem 8=>max num is",a
	except:
		print "Problem 8=> Please pass a list"


'''9) Write a program to calculate the sum of the numbers from 1 to 100 by using reduce ?'''
def sumByReduce():
	a = reduce(lambda x,y:x+y ,range(1,101))
	print "Problem 9=>Sum of fist 100 num is ",a


'''10) Write a program for following operation into the file?'''
def fileOperations():
	try:
		with open('myfile.txt','r+') as f:
		
			print "Problem 10=>Read()",f.read()
			f.seek(0)
			print "Problem 10=>readline()",f.readline()
			f.truncate()
			f.writelines(['this is 1st line\n','this is 2nd line\n','this is 3rd line\n','this is 4th line\n'])
			f.seek(34)
			print "Problem 10=>readlines() after seek(34)",f.readlines()
	except IOError:
		print "Problem 10 => Please give the right location of your file"


'''11)Write a program to print each line of a file in reverse order.	   
		Ex:
		   cat file.txt
		She sells seashells on the seashore;
		The shells that she sells are seashells I'm sure.
		So if she sells seashells on the seashore,

		Reverse order:
		So if she sells seashells on the seashore,
		The shells that she sells are seashells I'm sure.
		She sells seashells on the seashore;'''
def fileReverse():
	try:
		with open('cat file.txt','r+') as f:
			for line in reversed(f.readlines()):
				print "Problem 11 =>",line
	except IOError:
		print "Problem 11 => Please give the right location of your file"


'''12)What will be the output of the following program?
		def f():
		    try:
		        print "a"
		        return
		    except:
		        print "b"
		    else:
		        print "c"
		    finally:
		        print "d"

		f()'''


	'''ANs) Output:
			a
			d
		Because we use return after the try block so it will not execute the else part.'''
