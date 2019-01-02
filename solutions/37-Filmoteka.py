n=int(input())
lista=[]
for i in range(n):
	lista.append(input().split())
a=int(input())
b=int(input())
c=input()
for i in lista:
	if a<int(i[1]):
		print(i[0]+" "+i[1]+" ("+i[2]+")")
for i in lista:
	if 2014-int(i[3])<b:
		print(i[0]+" "+i[1]+" ("+i[2]+")")
for i in lista:
	if i[0][0]==c:
		print(i[0]+" "+i[1]+" ("+i[2]+")")