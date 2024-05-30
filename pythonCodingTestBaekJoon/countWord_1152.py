# 공백 앞, 중간, 뒤 모두 제거하는 메소드 적용해서-> 테스트 해보니 없어도 잘 출력 되서 사용  안함.
# strip([string]) : 문자열 왼쪽 오른쪽에서 string 제거
# lstrip([string]) : 문자열 왼쪽에서 string 제거
# rstrip([string]) : 문자열 오른쪽에서 string 제거
# 공백으로 구분(split())해서 배열에 먼저 담고 배열의 인덱스 수 구하는 것으로 품.

text = input()

resultArray = text.split()
result = len(resultArray)
print(result)
