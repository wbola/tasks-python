dl = int(input())
litery = input().split()
lista=[]
for i in range(dl):
	if litery[i].isupper():
		lista.append(litery[i])
lista.reverse()
for i in lista:
	print(i, end=" ")