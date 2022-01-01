import random
ans = random.randint(1, 100)
count = 0

while True:
	count = count + 1
	num = input('pls type number')
	num = int(num)
	if num == ans:
		print('pass', )
		print('count number', count)
		break
	elif num > ans:
		print('比較大')
	elif num < ans:
		print('比較小')
	print('count number', count)