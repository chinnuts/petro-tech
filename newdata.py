class Window():
	q=10
	r=5
	s=6
	

	def __init__(self,a,b,c):
		self.q=a
		self.r=b
		self.s=c
	
	
	def funs(self):
		print(self.q)
		print(self.r)
		print(self.s)

w=Window(4,5,6)
print(w.q)
print(w.r)
print(w.s)
w.funs()
print(w.q)
print(w.r)
print(w.s)
