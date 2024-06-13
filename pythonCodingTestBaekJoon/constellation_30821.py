# 30821 별자리가 될 수 있다면

# from itertools import combinations
from math import comb

N = int(input())
vertex_numbering = []

for i in range(N): # 전체 꼭짓점 수(N) 만큼 넘버링해서 1~N까지 리스트에 요소로 넣기
    element = i + 1
    vertex_numbering.append(element)
    
# N 개 중 5개(별의 꼭짓점 수 고정) 조합으로 경우의 수 추출 (방문순서는 상관없기 때문에 조합으로 적용)
result = comb(N, 5) 
print(result)

# 고민 or 고려한 점: 처음에는 combinations 라이브러리로 경우의 수를 모두 뽑은 다음에 나온 경우의 수 개수를 계산하려고 했으나 
# 다시 리스트에 담고 카운트 하는 것이 코드가 난잡해질 것으로 생각되어, 검색하다가 math 라이브러리의 comb 내장함수를 발견하여 적용함.
