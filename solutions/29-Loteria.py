n=int(input())
A=[]
for i in range(n):
	A.append(input())
A.sort(key=int)
for i in range(n):
	if A[i]==A[i-1] and (i+1==n or A[i]!=A[i+1]):
		print(A[i])