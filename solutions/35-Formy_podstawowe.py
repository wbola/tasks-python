n=int(input())
wyraz=[]
for i in range(n):
	wyraz.append(input().split())
input()
A=input().split()
for i in range(0,len(A)):
	for j in wyraz:
		if A[i]==j[0]:
			A[i]=j[1]
print(*A)