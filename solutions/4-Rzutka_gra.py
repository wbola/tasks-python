we = input().split()
a = int(we[0])
b = int(we[1])
x = int(input())

if x<a:
	print(a-x)
elif x>b:
	print(x-b)
else:
	print("BINGO")