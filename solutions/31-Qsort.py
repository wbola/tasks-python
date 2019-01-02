d=int(input())
for i in range(d):
	n=int(input())
	A=input().split()
	A=[int(i) for i in A]
	A.sort()
	print(*A[::-1])