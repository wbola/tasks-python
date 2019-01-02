x=int(input())
A=input().split()
A=[int(i) for i in A]
y=int(input())
for i in range(y):
	a,b=input().split()
	a=int(a)-1
	b=int(b)
	suma=0
	for j in range(a,b):
		suma+=A[j]
	print(suma)