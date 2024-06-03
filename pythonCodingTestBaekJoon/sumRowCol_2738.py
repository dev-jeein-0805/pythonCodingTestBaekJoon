# 2738 : 행렬 덧셈

# split() : 입력 받은 문자열을 공백을 기준으로 분리하여 문자열 리스트로 만듬
n, m = map(int, input().split())

A, B = [], []

for row in range(n):
    row = list(map(int, input().split()))
    # 리스트 자체를 추가하면 차원이 늘어난다!
    A.append(row)

for row in range(n):
    row = list(map(int, input().split()))
    B.append(row)

for row in range(n):
    for col in range(m):
        print(A[row][col] + B[row][col], end=' ')
    print()

# 리스트 안에 리스트 넣기
# a = []
# a.append([1, 2, 3]) # a = [[1,2,3]]
# a.append([2, 3, 4]) # a = [[1,2,3], [2,3,4]]
