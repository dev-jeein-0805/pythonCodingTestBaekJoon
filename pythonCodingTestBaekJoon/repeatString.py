
# 문제
# 문자열 S를 입력 받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
# S에는 QR Code "alphanumeric" 문자만 들어 있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다.
# 각 테스트 케이스에 대해 P를 출력한다.

# 내 풀이
# 오늘 푼 4 문제 중 나에겐 가장 어려웠다.
# JS 와 또 헷갈려서, 기억하기! str.length 가 아니라 파이썬은 len(str) !
# 파이썬에서 _ (언더스코어) 의 활용: index 가 필요 없는 for 문 작성 시 사용 가능
# 지정한 문자형태만 출력 가능하게 할 경우, if i in str 형태로 조건 걸어주기.
# 한번에 출력을 위해 배열에 담았다가 append() 함수로 한번에 출력.
# indented block : 들여쓰기 주의

numOfTest = int(input())
results = []

if numOfTest >= 1 and numOfTest <= 1000:
    for _ in range(numOfTest):
        num, string = input().split()
        num = int(num)

        if (num >= 1 and num <= 8) and len(string) >= 1 and len(string) <= 20:
            QR_Code_alphanumeric = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ$%*+-./:"

            final = ""
            for i in string:
                if i in QR_Code_alphanumeric:
                    final += i * int(num)
            results.append(final)
        else:
            break

    for output in results:
        print(output)
