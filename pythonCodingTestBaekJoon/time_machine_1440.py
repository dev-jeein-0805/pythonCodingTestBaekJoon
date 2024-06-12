
# 시 : 01 ~ 12
# 분, 초 : 00 ~ 59
# 시 에 따라 경우의 수가 달라짐
# '시' 가 모든 자리 가능하면 3 * 2! = 3! = 6(=3*2*1)
# '시' 가 2 자리만 가능하면 2 * 2! = 4
# '시' 가 1 자리만 가능하면 1 * 2! = 2
# '시' 가 모두 가능하지 않으면 0


Time = input()
time_list = Time.split(':')
time_list.sort()
# print(time_list)

count = 0
for i in range(3):
    if 1 <= int(time_list[0]) <= 12:
        count += 1

if count == 3:
    print(6)
elif count == 2:
    print(4)
elif count == 1:
    print(2)
else:
    print(0)

# 왜 틀리지...
