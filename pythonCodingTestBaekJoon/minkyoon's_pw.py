# 9933 민균이의 비밀번호

# 단어가 한 줄에 하나씩 적혀있음
# 모든 단어의 길이가 홀수
# ★비밀번호를 뒤집어서 쓴 문자열도 포함
# length : 3 ~ 13 (홀수)

N = int(input())
pworiginList = []
pwreversedList = []

for _ in range(N):
    pw = input()
    pworiginList.append(pw)
# print(pworiginList)

for i in range(N):
    reversed = pworiginList[i][::-1]
    pwreversedList.append(reversed)
# print(pwreversedList)

# 각각의 리스트에서 일치하는 값만 set 집합 자료구조 형태로 가져오기
sameWord = set(pworiginList) & set(pwreversedList)
# print(sameWord)
# '토마토' 같이 1개 요소만 있는 경우 set 요소 1만 나옴
# 원래pw + 뒤집은pw 이렇게 2개 있는 경우, 2개 같이 나옴

# 무조건 하나 요소 출력 후(set - 순서 랜덤) 가운데 요소만 출력
randomOne = sameWord.pop() # set 자료구조에서 랜덤 1개 추출
# print(randomOne)
# print(len(randomOne))

# length : 3 ~ 13 (홀수)
# 3개 -> 2번째 (3//2 + 1)
# 5개 -> 3번째 (5//2 + 1)
# ...
# 13개 -> 7번째 (13//2 + 1)
# 인덱스 번호니 -1 빼주기
# print(randomOne[len(randomOne)//2])
print(len(randomOne), randomOne[len(randomOne)//2], end='')
