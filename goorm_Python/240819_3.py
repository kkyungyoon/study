from collections import deque
N, M = map(int, input().split())
W = deque()

for i in range(M):
	L = list(input().split())
	
	while len(W) != 0 and N >= int(W[0][1]):
			N -= int(W[0][1])
			W.popleft()
		
	if L[0] == 'deposit':
		N += int(L[1])
	elif L[0] == 'pay':
		if N >= int(L[1]):
			N -= int(L[1])
	elif L[0] == 'reservation':
		if N < int(L[1]) or len(W) !=0 :
			W.append(L)
		else:
			N -= int(L[1])
			
while len(W) != 0 and N >= int(W[0][1]):
			N -= int(W[0][1])
			W.popleft()
print(N)