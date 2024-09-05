user_input = input()

L = []
a = -1

L.append(user_input[0])	
for idx, i in enumerate(user_input[1:]):
	if L and L[-1] > i:
		# print(i)
		L.pop()
		a = idx
		break
	L.append(i)
	
if a==-1:
	print(''.join(L[:-1]))
else:
	for i in range(a+1, len(user_input)):
		L.append(user_input[i])
	print(''.join(L))