a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
d=int(input("enter the 4th number:"))
if a>b&a>c&a>d:
	print("largest=",a)
elif b>c&b>d:
	print("largest=",b)
elif c>d:
	print("largest=",c)
else:
	print("largest=",d)