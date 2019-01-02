A=input().split()
A=[int(i) for i in A]
B=[]
s=0
for i in A:
	if i==-1:
		break
	elif i==1:
		print("%.2f"%(s/len(B)))
	elif i==0:
		print(*B)
	else:
		B.append(i)
		s=s+i