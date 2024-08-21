
N, M = map(int, input().split())
W = input()
Q = []

cnt = 1
tmp = None

for w in W:
	if tmp == w:
		continue
	else:
		tmp = None # 초기화 필요
	
	if Q and Q[-1] == w:
		cnt += 1
	else:
		cnt = 1
		
	if cnt >= M-1 and Q[-(M-1):] == [w]*(M-1):
			tmp = w
			for _ in range(M-1):
				Q.pop()
	else:
		Q.append(w)
		
if len(Q) == 0:
	print('CLEAR!')
else:
	print(''.join(Q))