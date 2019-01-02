def NWD(a,b):
	M=a
	m=b
	r=M%m
	while(r!=0):
		M=m
		m=r
		r=M%m
	return m

A=input().split()
A=[int(i) for i in A]
a=0
b=0
suma=0
for i in range(0,len(A)):
	if A[i]==1:
		suma+=NWD(a,b)
	elif A[i]>1:
		a=b
		b=A[i]
print(suma)