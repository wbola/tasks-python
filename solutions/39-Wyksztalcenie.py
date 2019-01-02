n=int(input())
opis=[]
for i in range(n):
	opis.append(input().split())
x=input()
for i in opis:
	if x=='p':
		if i[1] == 'p' or i[1] == 'g' or i[1] == 's' or i[1] == 'w':
			print(i[0])
	if x=='g':
		if i[1] == 'g' or i[1] == 's' or i[1] == 'w':
			print(i[0])
	if x=='s':
		if i[1] == 's' or i[1] == 'w':
			print(i[0])
	if x=='w':
		if i[1] == 'w':
			print(i[0])