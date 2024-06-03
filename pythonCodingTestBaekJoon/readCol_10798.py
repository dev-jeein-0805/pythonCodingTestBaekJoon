# 10798 : 세로읽기

alphaSentence = [list(input()) for _ in range(5)]
# 각 행의 길이를 확인하여 가장 긴 행의 길이를 열의 길이 n으로 설정
n = max(len(row) for row in alphaSentence)

sumCol = ''

for col in range(n):
    for row in range(5):
        # 누적하려고 하는 현재 열의 인덱스가 현재 행 길이 보다 작은 경우에만 수행 -> 이 부분 어려웠음
        if col < len(alphaSentence[row]):
            sumCol += alphaSentence[row][col]
print(sumCol)

# 사고과정
# print(alphaSentence[0][0] + alphaSentence[1][0] + ... + alphaSentence[4][0])
# print(alphaSentence[0][1] + alphaSentence[1][1] + ... + alphaSentence[4][1])
# ...
# print(alphaSentence[0][n-1] + alphaSentence[1][n-1] + ... + alphaSentence[4][n-1])
