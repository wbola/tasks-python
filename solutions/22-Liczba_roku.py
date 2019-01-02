n=int(input())
A=input().split()
A=[int(i) for i in A]
m=int(input())
for i in range(m):
	liczba=int(input())
	k=0
	for j in range(n):
		if liczba%A[j]==0:
			k=k+1
	print(k)