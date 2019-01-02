input()
ciag = input().split()
ciag = [int(i) for i in ciag[1::2]]
ciag.reverse()
for i in ciag:
	print(i, end=" ")