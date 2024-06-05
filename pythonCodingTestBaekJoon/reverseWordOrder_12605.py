# 12605 단어순서 뒤집기

N = int(input())
sentenceList = []

for i in range(N):
    # N 개 만큼 sentence 입력 받기
    sentence = input()
    # sentenceList 리스트에 입력 받은 문장들 요소로 추가
    sentenceList.append(sentence)
# print(sentenceList)

for i in range(N):
    # sentenceList 요소 하나씩 순회하면서 스페이스로 요소 나누기
    target = sentenceList[i].split()
    # for 문 안에 둬서 순회할 때 reverseList 초기화! 처음에 for 문 밖에 둬서 누적되서 출력됨
    reverseList = []
    # target 요소가 2개 이상일 때는 뒤집기 실행
    if len(target) > 1:
        # 중요! target 이 빈 리스트[] 가 아닐 때만(true) 반복
        while target:
            reverseList.append(target.pop())
        # print(reverseList)
        print(f'Case #{i+1}:', ' '.join(reverseList))
    # target 요소가 1개만 있을 때는 그대로 출력
    else:
        # print(target)
        print(f'Case #{i+1}:', ' '.join(target))

# 기억
# 입력을 모두 받은 후 한 번에 출력하도록 하려면,
# 입력된 문장들을 ★리스트★에 저장한 후,
# 반복문을 사용하여 출력

# IndexError: pop from empty list
# while i < N: 루프 조건으로 설정해서 target 리스트가 빈 상태에서도 pop() 메서드를 호출함
# while target: 으로 변경
