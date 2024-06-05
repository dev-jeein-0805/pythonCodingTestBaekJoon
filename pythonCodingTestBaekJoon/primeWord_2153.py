# 2153 소수 단어

# 파이썬 아스키 코드 변환 함수 검색 => ord() 함수
# 아스키코드 테이블(10진수)
# a ~ z : 97 ~ 122
# A ~ Z : 65 ~ 90

# 문제=> a ~ z : 1 ~ 26 & A ~ Z : 27 ~ 52
# a ~ z : ord('소문자') - 96
# A ~ Z : ord('대문자') - 38

word = input()
# 총 알파벳 별 숫자 더할 total 변수 초기화
total = 0

for i in range(len(word)):
    # 대문자
    if 65 <= ord(word[i]) <= 90:
        total += ord(word[i]) - 38
    # 소문자
    else:
        total += ord(word[i]) - 96

# print(total)

# 소수 : 1은 1만 출력, 그외 2이상 숫자는 1+자기숫자만 출력

# total == 1 인 경우
if total == 1:
    print('It is a prime word.')

# total 이 2 이상인 경우
# n = 2 ~ total-1 순회
else:
    is_prime = True
    for n in range(2, total):
        if total % n == 0:
            is_prime = False
            break

    if is_prime:
        print('It is a prime word.')
    else:
        print('It is not a prime word.')

# total 을 1부터 ~ total 까지 나눴을 때
# 예를 들어,
# 4%1 = 0, 4%2 = 0, 4%3 = 1, 4%4 = 0
# 5%1 = 0, 5%2 = 1, 5%3 = 2, 5%4 = 1, 5%5 = 0
# 즉, 소수는 1과 자기자신 빼고는 2 ~ (자기자신-1)까지 나눴을 때
# 나머지가 0이 아니어야 함

# 어려웠던 점 : else 문 안에 for 문을 넣는 것
# 최종 print 한번만 출력되게 하기 위해서 is_prime = True 선언 !!
