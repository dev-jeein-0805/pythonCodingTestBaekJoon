# 10419 지각 

T = int(input())

class_time_list = []
for _ in range(T):
    class_time = int(input())
    class_time_list.append(class_time)
# print(class_time_list)

late_time_list = []
for i in range(len(class_time_list)):
    a = 0
    while a + (a ** 2) <= class_time_list[i]:
        a += 1
        # print(a)
    late_time_list.append(a - 1) # 처음에 0으로 초기화하고 +1 씩 추가해야 되는데 그렇게 되면 a = 0 일 때도 최종 a = 1 로 출력되게 된다. 결국 답을 위해 마지막에 a-1 처리함.. (논리적이진 않음)

for i in late_time_list:
    print(i)

# 메모리: 	31120KB / 시간: 40ms / 언어: Python 3
