def add(x,y):
    return x+y
	
def subtract(x,y):
    return x-y

def multiply(x,y):	
    mul = x*y		#in bug456
	return mul

def divide(x,y):
    if y==0:					#Done by resolving conflicts
		return DIVIDE_BY_0_ERROR
	else:
		return x/y

def square(x):
	pass
