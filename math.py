def add(x,y):
    return x+y
	
def subtract(x,y):
    return x-y 				#done in bug456 branch
	
#mul implementation	
def multiply(x,y):
    return x*y				#done in master branch
	
#div implementation	
def divide(x,y):
    if y==0:					#Done by resolving conflicts
		return DIVIDE_BY_0_ERROR
	else:
		return x/y

def square(x):
	pass