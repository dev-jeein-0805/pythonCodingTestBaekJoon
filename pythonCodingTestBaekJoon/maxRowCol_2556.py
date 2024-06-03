# 2556 : 최댓값

table = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_row, max_col = 0, 0

for row in range(9):
    for col in range(9):
        if table[row][col] >= max_num:
            # 0 부터 시작하는 for 문 인덱스 특성 상 +1 로 1행 1열로 초기화해서 시작
            max_row = row + 1
            max_col = col + 1
            # 큰 값 저장해서 반복문 수행
            max_num = table[row][col]

print(max_num)
print(max_row, max_col)
