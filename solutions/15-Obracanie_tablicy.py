n, _ = input().split() # _ ignoruje
tab=[]
for i in range(int(n)):
	tab.append(input().split())
	
for row in zip(*tab):
	print(*row[::-1])