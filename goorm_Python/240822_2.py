N = int(input())
score = set(map(int, input().split()))

sum = 0

for s in score:
	if -s in score:
		pass
	else: 
		sum += s
print(sum)