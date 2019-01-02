n=int(input())
osoba=[]
for i in range(n):
	osoba.append(input().split())
x=int(input())
y=float(input())
for i in osoba:
	if int(i[2])>x:
		print(i[0],i[1])
print("----")
for i in osoba:
	if float(i[3])<y:
		print(i[0],i[1])