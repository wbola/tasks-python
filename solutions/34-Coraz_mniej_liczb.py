input()
A=input().split()
input()
B=input().split()
for i in B:
	for j in A:
		if j==i:
			x=A.count(j)
			for k in range(x):
				A.remove(j)
	print(*A)