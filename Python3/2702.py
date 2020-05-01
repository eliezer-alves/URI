n=int(input())
for i in range(n):
	s=input();
	s=list(s)
	cont=int(0)
	if s[0]=="R" and s[1]=="A" and len(s)==20:	
		for j in range(2, len(s)):
			if s[j]!="0":
				cont=1
			if cont==1:
				print(s[j], end="")
		print("")
	else:
		print("INVALID DATA")