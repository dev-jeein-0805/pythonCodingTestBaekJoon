# 세 자리 수 두 개 입력 받고,
# 각 수의 자리 별 숫자를 거꾸로 뒤집은 후 큰 수를 출력

# 처음엔 문자열로 그대로 둠 (배열 성격 유지)
num1, num2 = input().split()

def printLargeNum(num1, num2):
    # reverse() 함수 이용해서 문자열 뒤집고, 숫자(int) 로 형변환
    def printReverseNum(num):
        number_list = list(num)
        number_list.reverse()
        result = ''.join(number_list)
        return int(result)
    # 형변환 된 두 수 선언
    changedNum1 = printReverseNum(num1)
    changedNum2 = printReverseNum(num2)
    # 삼항 연산자 이용해서 큰 값 출력 -> max(a, b) 써도 되겠다.
    largeNum = changedNum1 if changedNum1 > changedNum2 else changedNum2
    print(largeNum)

printLargeNum(num1, num2)


# 문자열 뒤집고 정수로 변환하는 다른 방법
# int(num[::-1])
# [::-1] : 슬라이스 문법.
