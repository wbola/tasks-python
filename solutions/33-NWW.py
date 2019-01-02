def NWD(a,b):
	M=a
	m=b
	r=M%m
	while(r!=0):
		M=m
		m=r
		r=M%m
	return m
def NWW(a,b):
	c=round((a*b)/NWD(a,b))
	return c
	
n=int(input())
for i in range(n):
	A=input().split()
	A=[int(i) for i in A]
	print(NWW(A[0],NWW(A[1],NWW(A[2],A[3]))))