# 입력 받을 정수 num 선언
num = int(input())

# 문제에서 준 의사코드를 함수로 변형
def menOfPassion(n):
    sum = 0
    for _ in range(n):
        sum += 1 # 코드 1
    return print(sum)

# 입력 받은 정수를 menOfPassion() 함수에서 인자로 받아 출력 후, 정수는 # 코드 1 실행횟수 만큼 그대로 출력되고, (즉, num == sum)
# 정수는 단항 이기 때문에 어떤 정수 받아도 차수 1 출력 되도록 하드코딩..? print(1) 넣어 버림.
menOfPassion(num)
print(1)
