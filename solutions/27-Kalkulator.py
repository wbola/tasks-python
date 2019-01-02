n=int(input())
for i in range(n):
	a,op,b=input().split()
	a=int(a)
	b=int(b)
	if op=='+':
		print(a+b)
	if op=='-':
		print(a-b)
	if op=='*':
		print(a*b)