n=int(input())
for i in range(n):
	a,b=input().split()
	if a.isdigit() and b.isdigit():
		print(int(a)+int(b))
	elif a.isdigit():
		print(b[int(a)-1])
	elif b.isdigit():
		print(a[int(b)-1])
	else:
		print(a+b)