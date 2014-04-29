'''1) What is compound Object ?? Corelate in terms of deep and shallow copy ??
	Ans) compound objects are objects which contains objects, like lists or dict or classes.
			Shallow Copy : In shallow copy, a new object is created which contains the exact copy of the values in the original object. 
				it follows the bit-wise copy approach. In shallow copy if the field is a memory address, then the address is copied. 
				Thus if the address is changed by one object, the change gets reflected everywhere.

			Deep Copy : In deep copy, not only all the fields of an object are copied, 
						all the dynamically allocated memory address which are pointed by that object are also copied.'''