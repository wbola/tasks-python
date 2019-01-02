def silnie(n,k):
	if n<k:
		return 1
	else:
		return n*silnie(n-k,k)

t=int(input())
for i in range(t):
	n,k=input().split()
	n=int(n)
	k=int(k)
	print(silnie(n,k))