x,y=input().split()
x=int(x)
y=int(y)
n=int(input())
punkty_karne=0
trafienie=input().split()
trafienie=[int(i) for i in trafienie]

for i in trafienie:
	if i>=x and i<=y:
		punkty_karne=0
	else:
		if i<x:
			punkty_karne=punkty_karne+x-i
		else:
			if i>y:
				punkty_karne=punkty_karne+i-y
print(punkty_karne)