rok = input()
rok=int(rok)
if rok%4==0 and rok%100!=0 or rok%400==0:
	print("Yes")
else:
	print("No")