# 3107 IPv6

summarized = input().split(':')
print(summarized)

total = []
# 0000 아예 없는 그룹 + 0000 1개 있는 그룹 까지 들어옴
if len(summarized) == 8:
    for i in range(8):
        if len(summarized[i]) <= 4:
            # 앞에 부족한 4 - len(summarized[i]) 만큼 0 붙이기
            result = ''.join(list('0'*(4 - len(summarized[i])) + summarized[i]))
            total.append(result)
finalResult = ':'.join(total)
print(finalResult)

# 0000 이 2개 이상인 그룹
def insert_spaceElement(lst, target, element):
    index = lst.index(target)
    lst.insert(index, element)

if len(summarized) < 8:
    insert_spaceElement(summarized, '', '')

구현 중... 시간 초과로 여기까지 제출 (나머지 완성해야 함)
