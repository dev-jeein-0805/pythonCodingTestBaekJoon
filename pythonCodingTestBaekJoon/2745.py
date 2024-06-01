# 0 ~ 9 (10개 숫자)
# A ~ Z : 10 ~ 35 (26개 알파벳)

N, B = input().split()
B = int(B)

# 최대 36진법(10+26)까지 가능한 모든 문자를 나열한 list 선언
alphabet_list = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# 0부터 35까지의 숫자를 나열한 list 선언
# alphabet_list의 각 문자가 10진법에서 어떤 숫자에 해당하는지 나타냄
# (두 list index 수가 같은 점 이용해서 index 를 키 값으로 join 하기! )
num_list = list(range(36))

sum = 0
# 입력 받은 N 진법의 숫자의 각 위치(i)와 값(char) 순회해서 추출
for i, char in enumerate(N):
    # 현재 문자가 alphabet_list에서 몇 번째에 위치하는지 찾아내어
    # 그 인덱스를 num_idx에 저장
    # num_list에서 해당 문자가 10진법으로 얼마인지 찾는데 사용
    num_idx = alphabet_list.index(char)
    # ?
    sum += (num_list[num_idx] * (B**(len(N) - 1 - i)))
print(sum)
