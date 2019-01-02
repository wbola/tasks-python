rok1,miesiac1,dzien1=input().split()
rok2,miesiac2,dzien2=input().split()
rok1=int(rok1)
rok2=int(rok2)
miesiac1=int(miesiac1)
miesiac2=int(miesiac2)
dzien1=int(dzien1)
dzien2=int(dzien2)
if rok1*1000 + miesiac1*10 + dzien1 < rok2*1000 + miesiac2*10 + dzien2:
	print(rok1,miesiac1,dzien1)
else:
	print(rok2,miesiac2,dzien2)