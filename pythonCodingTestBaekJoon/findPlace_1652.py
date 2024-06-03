# 1652 : 누울 자리를 찾아라

# 가로 줄 연속된 .. 이 2개 이상이면 True 출력 => True 개수
# 세로 줄 연속된 .. 이 2개 이상이면 True 출력 => True 개수
# 가로 한줄 별로 배열 list 로 나누고, 그 list 내 연속된 .. sorting
# 배열 list 내 [i] 번째 요소 끼리 추출해서 다시 새로운 배열로 만든 다음에,
# 가로 처럼 list 내 연속된 .. 2개 이상 sorting

N = int(input())
rooms = [input().strip() for _ in range(N)]

def count_consecutive_dots(matrix):
    row_count = 0
    col_count = 0

    # 가로 방향 검사
    for row in matrix:
        count = 0
        for col in row:
            if col == '.':
                count += 1
            else:
                if count >= 2:
                    row_count += 1
                count = 0
        if count >= 2:  # 행의 끝에서 체크
            row_count += 1

    # 세로 방향 검사
    for col in range(N):
        count = 0
        for row in range(N):
            if matrix[row][col] == '.':
                count += 1
            else:
                if count >= 2:
                    col_count += 1
                count = 0
        if count >= 2:  # 열의 끝에서 체크
            col_count += 1
            
    return row_count, col_count

row_count, col_count = count_consecutive_dots(rooms)
print(row_count, col_count)
