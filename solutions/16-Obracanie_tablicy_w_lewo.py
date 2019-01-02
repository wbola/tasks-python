n, _ = input().split()
tab=[]
for i in range(int(n)):
	tab.append(input().split()[::-1])
	
for row in zip(*tab):
	print(*row)