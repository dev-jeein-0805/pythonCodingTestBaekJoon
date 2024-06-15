# 11722 가장 긴 감소하는 부분 수열

N = int(input())
num_list = list(map(int, input().split()))

dp = [1] * N # dp를 리스트 크기만큼 1로 초기화

for i in range(N):
    for j in range(0, i):
        # 앞의 수가 현재 위치의 수보다 클 때 앞의 수에 해당하는 dp 값과 현재 위치의 dp 값을 비교하여 큰 값을 현재 위치의 dp값에 넣는다
        if num_list[i] < num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 한 줄 씩 디버깅 계속 해보기
