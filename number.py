import random
ans = random.randint(1, 100)


while True:
	num = input('pls type number')
	num = int(num)
	if num == ans:
		print('pass')
		break
	elif num > ans:
		print('比較大')
	elif num < ans:
		print('比較小')