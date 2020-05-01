while True:
	s = input()
	if s == '*':
		break
	s = s.split(' ')
	verdade = int(0)
	for i in range(len(s)-1):
		if s[i+1][0].upper() != s[i][0].upper():
			print('N')
			verdade = -1
			break
	if verdade == 0:
		print('Y')