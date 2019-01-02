from math import *
n=int(input())
wsp=[]
for i in range(n):
	wsp.append(input().split())
o=0
for i in wsp:
	o=o+(int(i[0])+int(i[1]))
s=0
for i in wsp:
	s=s+sqrt(int(i[0])*int(i[0])+int(i[1])*int(i[1]))
print("%.3f"%(o),"%.3f"%(s))