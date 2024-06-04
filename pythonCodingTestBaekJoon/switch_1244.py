# 1244 스위치 켜고 끄기

numOfSwitch = int(input())
switchStatus = list(map(int, input().split()))
numOfStudent = int(input())
# numOfStudent 만큼 반복
for _ in range(numOfStudent):
    gender, switchNumber = map(int, input().split())
    # men
    if gender == 1:
        # switchNumber가 5라면 4번 인덱스부터 시작이니까 switchNumber - 1 부터 시작
        for i in range(switchNumber - 1, numOfSwitch, switchNumber):
            switchStatus[i] = 1 - switchStatus[i]
    # women
    else:
        # 인덱스 0 부터 시작
        switchNumber -= 1
        for i in range(numOfSwitch):
            if switchNumber - (i+1) >= 0 and switchNumber + (i+1) < numOfSwitch:
                if switchStatus[switchNumber - (i+1)] == switchStatus[switchNumber + (i+1)]:
                    switchStatus[switchNumber - (i+1)] = 1 - switchStatus[switchNumber - (i+1)]
                    switchStatus[switchNumber + (i+1)] = 1 - switchStatus[switchNumber + (i+1)]
                else:
                    break
            else:
                break
        # 첫 번 부터 좌우 숫자 다를 경우 본인 스위치 번호만 반전함
        switchStatus[switchNumber] = 1 - switchStatus[switchNumber]

# 20개씩 끊어서 출력
for i in range(0, numOfSwitch, 20):
    print(' '.join(map(str, switchStatus[i:i+20])))
