class Library:
	def registration(self):
		print("welcome to registration")
	def searchbook(self,bookid):
		print("hai hello")
		if bookid>=20:
			print("book is available")
		else:
			print("book is not available")
	def searchuser(self):
		n=int(input("enter a your number"))
		if(n==9448708768):
			print("user found")
		else:
			print("user not found")
class Digitallibrary:
	def scanqrcode(self):
		print("qr code")		
		
lourdlibrary=Library()
lourdlibrary.registration()
lourdlibrary.searchbook(25)
lourdlibrary.searchuser()

diglib=Digitallibrary()
diglib.scanqrcode()	