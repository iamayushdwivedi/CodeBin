t = int(input())
while t > 0:
	org = input()
	fake = input()
	left = fake[2:] + fake[0:2]
	right = fake[0:len(fake) - 2] + fake[len(fake) - 2:]
	if org == right or org == left:
		print("Yes")
	else:
		print("No")