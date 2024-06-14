# 14659 한조서열정리하고옴ㅋㅋ

# 입력
N = int(input())
peak = list(map(int, input().split()))

# 그리디
high_max = 0  # 현재까지의 최고 높이를 저장
count = 0  # 현재 최고 높이보다 낮은 연속된 값의 개수를 저장
max_kill = 0  # 최종 결과값으로서 연속된 값의 최대 개수를 저장

for i in peak:
    # 더 높은 봉우리 만나면 갱신
    if i > high_max:
        high_max = i
        count = 0

    # 더 낮은 봉우리면 kill
    if i < high_max:
        count += 1
    max_kill = max(max_kill, count)

print(max_kill)

# max_kill 변수에 죽인 적의 수가 누적되고 count 와 비교되기 때문에 보존됨
