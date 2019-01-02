n=int(input())
kto=[]
for i in range(n):
	kto.append(input())
x=input()
k=0
for i in kto:
	if i==x:
		k=k+1
print(k)