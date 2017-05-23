def gcd(m,n):
	while m%n!=0:
		oldm = m
		oldn = n
		n=m%n
		m=oldn
	return n

class Fraction:
	def __init__(self,top,bottom):
		self.num = top
		self.den = bottom
	def show(self):
		print(self.num,"/",self.den)
	def __str__(self):
		return str(self.num) + "/" + str(self.den)
	def __add__(self, otherfrac):
		newnum = self.num*otherfrac.den + self.den*otherfrac.num
		newden = self.den*otherfrac.den
		common = gcd(newnum,newden)
		return Fraction(newnum//common,newden//common)


a=Fraction(1,2)
b=Fraction(1,4)
c=a+b
print c