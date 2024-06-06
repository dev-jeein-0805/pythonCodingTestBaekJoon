# 31562 전주 듣고 노래 맞히기

# 윤수는 노래의 첫 네 음
# 정환은 윤수를 이기기 위해 첫 세 음
# 노래가 여러 개 있어 무슨 노래 인지 정확히 알 수 없는 경우 ?를 출력
# 저장된 노래가 없을 경우 !를 출력
# 대문자와 소문자를 구분

N, M = map(int, input().split())
inputSongList = []
for _ in range(N):
    songInfo = input().split() # 0번 개수 # 1번 제목 # 2~8번 음계
    inputSongList.append(songInfo)
# print(inputSongList)
# print(inputSongList[0][2:5]) # ['C', 'C', 'G']
# print(inputSongList[1][2:5]) # ['E', 'D', 'E']
# print(inputSongList[2][2:5]) # ['C', 'C', 'C']
# print(inputSongList[3][2:5]) # ['C', 'C', 'C']

# 마지막에 한번에 출력 받을 리스트
outputList = []

for _ in range(M):
    threePitch = input().split()

    matchedSongs = []
    for songDetail in inputSongList:
        if threePitch == songDetail[2:5]:
            # 일치 데이터가 있으면 노래 제목 matchedSongs 리스트에 추가
            matchedSongs.append(songDetail[1])

    if len(matchedSongs) == 1:
        outputList.append(matchedSongs[0])
    elif len(matchedSongs) > 1:
        outputList.append("?")
    else:
        outputList.append("!")

for result in outputList:
    print(result)

# 메모리 : 31,120KB / 시간 : 300ms / 언어 : Python 3
# 시간이 너무 오래 걸린다
