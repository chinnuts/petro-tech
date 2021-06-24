def  hello():
	print("hai hello")
def hai(a,b):
	print("how are you")
def  mult(a,b):
	product=a*b
	print("product=",product)
	return product
               
def calc():
	number1=int(input("enter the first number"))
	number2=int(input("enter the second number"))
	sum=number1+number2
	print("sum is",sum)	
	return()
def call():
	hello()
	hai(10,10)
	mult(20,20)
	calc()
	
call()
	
	
	