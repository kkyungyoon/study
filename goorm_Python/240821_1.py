from collections import deque
N, K = map(int, input().split())

D = deque()
for _ in range(N):
	order = list(input().split())
	if order[0] == 'push':
		print('Overflow') if len(D) == K else D.append(order[-1])
	else:
		print('Underflow') if len(D) == 0 else print(D.pop())