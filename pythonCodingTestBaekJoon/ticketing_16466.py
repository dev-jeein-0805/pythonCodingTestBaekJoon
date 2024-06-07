# 16466 콘서트

# 티켓팅
# 첫째 줄 : 출력할 정수 개수(10^6 이하) -> O(n) 이하로 풀어야 함
# 둘째 줄 : 첫째 줄 개수 만큼 정수 출력 (공백으로 구분)

N = int(input())

for _ in range(N):
    num = list(map(int, input().split()))
    num.sort() # 오름차순 먼저 정렬
    # print(num)

    find_number = None

    # 0번째 인덱스부터 1씩 증가하면서 비어있는 숫자 찾기
    for i in range(len(num)):
        if num[i] != i+1:
            find_number = i+1
            print(find_number)
            break

    # 위에 for 문 모두 순회했는데 find_number 값을 못 얻었을 경우
    if find_number is None:
        print(len(num) + 1) # 마지막 숫자에 +1한 숫자 출력

# 파이참에서는 값이 잘 나오는데, 백준은 계속 런타임 에러가 나온다..
# 아마 O(n) 으로 제출해야 하는데, O(n^2) 로 나와서 에러인 것 같다.
