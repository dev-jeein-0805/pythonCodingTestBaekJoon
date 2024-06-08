# 11899 괄호 끼워넣기

# 올바른 괄호열 만들기
# 0번째 인덱스부터 마지막 인덱스까지 () 모양인게 있으면 모두 제거 * 반복 순회
# => 남아 있는 () 모양이 없을 때까지
# 다 완료하고 마지막에 남은 괄호 개수 출력 -> 그 만큼 대칭되는 괄호 넣어줘야 하니까.

bracketStr = input()

while '()' in bracketStr:
    bracketStr = bracketStr.replace('()', '')
# print(bracketStr)
print(len(bracketStr))

# 신선했던 점 :
# while 문으로 () 가 없을 때까지는 생각 했으나,
# () 가 없는 상태를 다시 집어 넣는 것을 생각하기 어려웠다.
# () 제거한 값을 그대로 다시 bracketStr 에 넣는 것으로 while 문 돌려서 해결.
