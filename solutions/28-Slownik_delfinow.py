n=int(input())
slowo=[]
for i in range(n):
	slowo.append(input())
slowo.sort()
print(*slowo, sep="\n")