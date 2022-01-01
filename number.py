import random
start = input('pls type start value')
end = input('pls type end value')
start = int(start)
end = int(end)
ans = random.randint(start, end)
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