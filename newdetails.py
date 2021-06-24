class Car():
	x=10
	num=10
	def _init_(self,num,m):
		self.num=num
		self.m=m
	def hello(self):
		print("how are you")
	def hai(self,colour):
		print("what is this",colour)
	def huy(self,colour,number):
		print("how are you",number,colour)
	
car=Car()
print(car.num)
car=Car()
car.hello()
car.hai("blue")
car.huy("green",5)
print(car.x)
car.x=car.x+1
print(car.x)
q=Car()
print(q.x)
