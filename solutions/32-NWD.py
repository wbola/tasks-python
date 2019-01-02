def NWD(a,b):
	M=a
	m=b
	r=M%m
	while(r!=0):
		M=m
		m=r
		r=M%m
	return m
	
n=int(input())
for i in range(n):
	A=input().split()
	A=[int(i) for i in A]
	print(NWD(A[0],NWD(A[1],NWD(A[2],A[3]))))