tec=("# ` 1 2 3 4 5 6 7 8 9 0 - = Q W E R T Y U I O P [ ] \ A S D F G H J K L ; ' Z X C V B N M , . /")
tec=tec.split(' ');
cont=int(0)
while True:
	try:
		s=input()
		resp=[]
		if cont==0:
			for i in range(len(s)):
				if s[i] == "`" or s[i] == "Q" or s[i] == "A" or s[i] == "Z":
					cont=1
					break
				elif s[i]==" ":
					print(" ",end="")
				else:
					print(tec[tec.index(s[i])-1], end="")
			#t=''.join(map(str, resp))
			print()
		else:
			break;

	except EOFError:
		break;
