def myfunc():
	try:
		numb=10/0
		print(numb)
	except:
		print("something went wrong")
	c=2+3
	print(c)

def mydeser():
	try:
		numb=10/0
		print(numb)
	except:
		print("something went wrong")
	finally:
		num=10
		print(num)
		print("exception completed")
	c=2+3
	print(c)
mydeser()