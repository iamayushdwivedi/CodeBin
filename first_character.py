t = int(input())
while t > 0:
	n = int(input())
	str = input()
	x, y = 0, 0
	cc = ''
	if str[0] == 'L':
		x -= 1
		cc = 'L'
	elif str[0] == 'R':
		x += 1
		cc = 'R'
	elif str[0] == 'U':
		y += 1
		cc = 'U'
	else:
		y -= 1
		cc = 'D'
	for i in range(1, n):
		if cc == 'L' or cc == 'R':
			if str[i] == 'U':
				y += 1
				cc = 'U'
			elif str[i] == 'D':
				y -= 1
				cc = 'D'
		else:
			if str[i] == 'L':
				x -= 1
				cc = 'L'
			elif str[i] == 'R':
				x += 1
				cc = 'R'
	print(x, y)
	t -= 1