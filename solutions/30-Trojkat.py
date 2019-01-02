from math import *
n=int(input())
for i in range(n):
	a,b=input().split()
	a=int(a)
	b=int(b)
	if a>b:
		a,b=b,a
	print(ceil(sqrt(a*a+b*b)), round(atan(a/b)*180/pi))