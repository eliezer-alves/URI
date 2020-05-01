while True:
	n=input()
	if n=="0 0":
		break
	
	a,b = n.split(' ')
	cont=("1")
	resp=("")
	for i in range(len(b)):
		if a!=b[i]:
			if b[i]!="0":
				cont="0"
			if b[i]=="0" and cont=="0":
				resp=resp+b[i]
			elif b[i]!="0":
				resp=resp+b[i]
	if resp=="":
		resp="0"
	print(resp)