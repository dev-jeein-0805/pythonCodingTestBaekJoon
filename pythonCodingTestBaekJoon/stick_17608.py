# 17608 막대기

N = int(input())
stack = []
for _ in range(N):
    # N 개 만큼 정수 입력 받기
    num = input()
    # stack 구조로 하나씩 추가하기
    stack.append(num)

# 맨 뒤에 요소 먼저 pop 으로 빼기
last = int(stack.pop())

# 맨 끝에 있는 요소가 뒤에 막대들 가리는 기준이니 기본 1개 설정
count = 1

# stack = [] 빈 list 이면 false 로 while 문 탈출
while stack:
    current = int(stack.pop())

    if current > last:
        last = current
        count += 1

print(count)

! Python 3 로 제출 했더니 시간초과가 나와서, PyPy3 로 제출해서 겨우 통과하였다.
메모리 : 117,500KB	/ 시간 : 164ms / 코드 길이 : 247B
