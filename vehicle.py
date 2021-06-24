class Student():
	rollno=0
	name=" "
	email=" "
	def __init__(self,rollno,name,email):
		self.rollno=rollno
		self.name=name
		self.email=email
	def view(self):
		print(self.rollno)
		print(self.name)
		print(self.email)
	
studanu=Student(1,"anu","anu@gmail.com")
studchinnu=Student(2,"chinnu","chinnu@gmail.com")
studnalu=Student(3,"nalu","nalu@gmail.com")

studanu.view()
studchinnu.view()
studnalu.view()
