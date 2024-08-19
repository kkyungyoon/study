N, K = map(int, input().split())
arrow = input()
board = []
for _ in range(N):
	board.append(list(map(int, input().split())))
# 시작위치 찾기 (rx, cx)
cx = 0
for i, b in enumerate(board): # 이렇게 하면 보기 불편하기 때문에 이중 for문 도는게 좋다
	if 1 in b: 
		cx = b.index(1)
		rx = i
# 이동명령 딕셔너리 선언
x_dict = {'U': -1, 'D' : 1, 'L' : 0, 'R': 0}
y_dict = {'U': 0, 'D' : 0, 'L' : -1, 'R': 1}
# 이동명령을 하나씩 불러옴	
move = 0
for arr in arrow:
	# 이동위치값 넣어주기
	new_rx, new_cx = rx + x_dict[arr], cx + y_dict[arr]
	# 보드판 넘어가면 원래값으로 돌려보내기
	if new_rx < 0 or new_rx > N-1 or new_cx < 0 or new_cx > N-1: 
		new_rx = rx
		new_cx = cx
	elif board[new_rx][new_cx] == 0 or board[new_rx][new_cx] == 1: 
		rx = new_rx
		cx = new_cx
		move += 1
	elif board[new_rx][new_cx] == 2: 
		# 탈출
		move += 1
		print('SUCCESS', move) 
		break
	elif board[new_rx][new_cx] == 3:
		# 벽만나면 원래값으로 돌려보내기
		new_rx = rx
		new_cx = cx
if board[new_rx][new_cx] != 2:
	print('FAIL')