n=input()
cont=int(0)
for i in range(len(n)):
	if n[i]=='0':
		cont+=1
	elif n[i]=='1':
		break
print(cont+1)