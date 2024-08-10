"""
유형 : 배열
난이도 난이도2
사이트 : 구름
"""


N = int(input())

matrix = []
for _ in range(N):
	matrix.append(list(map(int, input().split())))

k = 0
for idx, box in enumerate(matrix):
	if 0 in box:
		k = box.index(0)
		total_sum = sum(box)

for box in matrix:
	if 0 not in box:
		total_sum += box[k]

print(total_sum)