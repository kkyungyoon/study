"""
유형 : 배열
제목 : 구름 찾기 깃발
난이도 난이도2
사이트 : 구름
"""

n, k = map(int, input().split())
matrix = []
for _ in range(n):
	matrix.append(list(map(int, input().split())))

import numpy as np
zero_matrix = np.zeros([n,n])


for i in range(n):
	for j in range(n):
		row_st = i-1
		row_ed = i+1
		col_st = j-1
		col_ed = j+1
		
		if row_st < 0:
			row_st = i
		if row_ed > n-1:
			row_ed = i
		if col_st < 0:
			col_st = j
		if col_ed > n-1:
			col_ed = j
			
		if matrix[i][j] != 1:
			for a in range(row_st, row_ed+1):
				for b in range(col_st, col_ed+1):
						if matrix[a][b] == 1:
							zero_matrix[i][j] += 1
							
cnt = 0
# 리스트 받아올때는 어지간하면 중복 for문으로하는게좋음
for box in zero_matrix:
	for num in box:
		if k == num:
			cnt += 1
print(cnt)