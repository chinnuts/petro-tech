class Window():
	q=10
	r=5
	s=6
	def __init__(self,q,r,s):
		self.q=q
		self.r=r
		self.s=s
	
	def funs(self):
		print(self.q)
		print(self.r)
		print(self.s)
	def volumerect(self):
		volume=self.q*self.r*self.s
		print(volume)
w=Window(9,8,7)

w.volumerect()
z=Window(1,2,3)
z.volumerect()