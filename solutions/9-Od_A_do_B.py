n=int(input())
for i in range(1,n+1):
	a,b,znak=input().split()
	a=int(a)
	b=int(b)
	if a==b:
		continue
	if a>b:
		temp=a
		a=b
		b=temp
	if znak=='+':
		wynik=0
		for j in range(a,b+1):
			wynik=wynik+j
	if znak=='-':
		wynik=0
		for j in range(a,b+1):
			wynik=wynik-j
	if znak=='*':
		wynik=1
		for j in range(a,b+1):
			wynik=wynik*j
	print(wynik)