def fib(n):
    if n==1 or n==2:
        return 1
    # fib 재귀함수 호출
    else:
        return fib(n-1)+fib(n-2)
        
def fibonacci(n):
    # n+1 길이의 리스트 dp를 생성, 모든 요소를 0으로 초기화
    dp=[0]*(n+1)
    # 피보나치 수열의 첫 번째와 두 번째 항은 1로 설정
    dp[1],dp[2]=1,1
    # 반복 횟수를 세기 위한 변수 cnt2 초기화
    cnt2=0
  
    for i in range(3,n+1):
        cnt2+=1
        dp[i]=dp[i-1]+dp[i-2]
    return cnt2

n=int(input())
print(fib(n), fibonacci(n))
