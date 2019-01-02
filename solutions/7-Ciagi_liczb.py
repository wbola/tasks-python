a,b=input().split()
a = int(a)
b = int(b)
znak = input()
if znak=='n' and a%2==0 or znak=='p' and a%2==1:
	a += 1
for i in range(a,b+1,2):
	print(i, end=" ") # end - przechodzenie do następnej linii