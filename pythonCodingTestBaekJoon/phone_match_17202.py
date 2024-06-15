# 17202 핸드폰 번호 궁합

A = input()
B = input()

combined = []
for i in range(8):
    a_with_b = ''
    a_with_b = A[i] + B[i]
    combined.append(a_with_b)
full_number = ''.join(combined)
# print(full_number) # 7346715995393764

def topToDown(full_number):
    if len(full_number) <= 2:
        return full_number
    else:
        new_number = ''
        for j in range(len(full_number) - 1):
            modi_line = (int(full_number[j]) + int(full_number[j+1])) % 10
            new_number += str(modi_line)
        return topToDown(new_number)

print(topToDown(full_number))

# return 문에 함수를 다시 재귀 호출하는 방법으로 Top-down 방식으로 풀었다.
