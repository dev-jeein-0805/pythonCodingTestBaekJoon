# 2851 슈퍼 마리오

# 10개의 숫자 입력 받음
# 순서대로 더할 때 100에 가까운 점수 출력

nums = [int(input()) for _ in range(10)]
# print(nums) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

sum = 0
first_max_sum = 0
second_max_sum = 0

for i in nums:
    sum += i
    if sum <= 100:
        first_max_sum = sum # 합이 100 이하인 값 중 최댓값을 저장
    else:
        second_max_sum = sum # 합이 100 초과인 최초값 저장 후 바로 break 문으로 탈출
        break

# 놓친 부분: 10개를 다 더해도 100 초과 안 할 수 있음. 그러면 first_max_sum 출력.
if second_max_sum == 0:
    print(first_max_sum)
# 10 개 안에서 중간에 100 에 가까운 합이 발견될 때
else:
    under_hundred = 100 - first_max_sum # 나중에 발견 : abs() 절대값 함수로 하면 더 간편함.
    over_hundred = second_max_sum - 100

    if under_hundred < over_hundred:
        print(first_max_sum)
    elif under_hundred == over_hundred:
        print(second_max_sum)
    else:
        print(second_max_sum)
