# sys.stdin.readline() 함수를 사용하기 위해 sys 모듈 호출
# 전체 수행 횟수는 1부터 n - 2까지 각 1부터 해당 값까지의 합의 결과를 모두 더한 총 결과
# 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수는 3

import sys

n = int(sys.stdin.readline())

print( (n * (n - 1) *  (n - 2)) // 6 )
print(3)
