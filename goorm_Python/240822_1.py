N, M = map(int, input().split())
card = set()
cnt = 0

for _ in range(M):
	c = int(input())
	card.add(c)
	cnt += 1
	
	if len(card) == N:
		print(cnt)
		break
		
if len(card) != N:
	print(-1)