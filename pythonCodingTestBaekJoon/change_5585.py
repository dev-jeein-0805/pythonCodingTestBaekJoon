# 5585 거스름돈

# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
# 1000엔 - 지불할 돈 -> 받을 잔돈에 포함된 잔돈의 개수 (최솟값)

price = int(input())

coins = [500, 100, 50, 10, 5, 1]
change = 1000 - price

def min_coins(coins, change):
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if change == 0:
            break # 거스름돈 0 원이면 바로 종료
        count += change // coin # 오름차순 되어 있는 coin 의 가장 큰 수로 현재 change 나눔
        change %= coin # 나눈 나머지 금액 다시 change 에 저장

    return count # 누적된 최소 동전 개수 반환

print(min_coins(coins, change))
