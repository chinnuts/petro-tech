def choice():
	print("welcome user")
	print("please select your choice")
	print("1.find sum")
	print("2.find subtraction")
	print("3.find multiplication")
	print("4.find division")
	print("5.exit program")
	print("please enter your choice")
	choice=int(input())
	return data
def add(a,b):
	sum=a+b
	print("sum =",sum)
def sub(a,b):
	sub=a-b
	print("sub=",sub)
def mult(a,b):
	mult=a*b
	print("mult=",mult)
def div(a,b):
	div=a/b
	print("div=",div)

def data():
	print("enter the first number")
	a=int(input())
	print("enter the second number")
	b=int(input())
	selchoice=choice()

	if selchoice==1:
		add(a,b)
		choice()
data()