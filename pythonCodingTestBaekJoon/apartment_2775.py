# 2775 부녀회장이 될테야

# 2층 1 4 10
# 1층 1 3 6
# 0층 1 2 3

T = int(input())

# Bottom-up
def persons(k, n):
    stairs = {0: [i for i in range(1, n+1)]}  # base case

    for i in range(1, k+1):
        stairs[i] = [1] * n # 항상 1호실 사람 수는 1명이기 때문에 먼저 초기화
        for j in range(1, n):
            stairs[i][j] = stairs[i][j-1] + stairs[i-1][j]
    return stairs[k][n-1] # k층 n호(인덱스 번호=n호-1) 값 리턴

results = []
for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    results.append(persons(k, n))

for result in results:
    print(result)
