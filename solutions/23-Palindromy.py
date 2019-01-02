for i in range(int(input())):  #pętla się wywoła tyle ile jest miejsca
	s=input()
	print(s+("==" if s==s[::-1] else "!=")+s[::-1]) #+ - łączymy łańcuchy
