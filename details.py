def data():
	print("enter the first number")
	a=int(input())
	print("enter the second number")
	b=int(input())
	selchoice=choice()
	
	if selchoice==1:
		add(a,b)
		choice()
	elif selchoice==2:
		sub(a,b)	
		choice()
	elif selchoice==3:
		mult(a,b)
		choice()
	elif selchoice==4:
		div(a,b)
		choice()
	else:
		print("hai")

def choice():
	print("1.addition")
	print("2.subtraction")
	print("3.multiplication")
	print("4.division")
	print("enter your choice")
	choice=int(input())
	return choice

	

def  add(a,b):
	sum=a+b
	print("sum=",sum)

def sub(a,b):
	diff=a-b
	print("diff=",diff)

def mult(a,b):
	mult=a*b
	print("mult=",mult)

def div(a,b):
	div=a/b
	print("div=",div)
data()	
	



	