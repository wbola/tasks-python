input()
ciag = input().split()
ciag = [int(i) for i in ciag[2::3]]
ciag.reverse()
for i in ciag:
	print(i, end=" ")