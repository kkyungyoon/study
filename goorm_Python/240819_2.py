N = int(input())
D = input()
S = list(map(int, input().split()))

move = {'U': [-1,0] ,'D': [1,0],'L':[0,-1],'R':[0,1]}
path = []
result = [1]

st, ed = 0, 0
path.append([st, ed])
for i in range(len(D)):
	x, y = st + move[D[i]][0], ed + move[D[i]][1]
	if [x, y] in path:
		idx = path.index([x, y])
		path = path[:idx]
		result = result[:idx]
		path.append([x, y])
		result.append(S[i])
	else: 
		path.append([x, y])
		result.append(S[i])
	
	st, ed = x, y
print(sum(result))