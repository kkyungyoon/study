"""
유형 : 배열
제목 : M배 배열
난이도 난이도2
사이트 : 구름
"""

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
	
for idx, num in enumerate(num_list[:]):
	if num % m != 0:
		num_list[idx] = num_list[idx] * m
	else:
		continue
	
print(*num_list)