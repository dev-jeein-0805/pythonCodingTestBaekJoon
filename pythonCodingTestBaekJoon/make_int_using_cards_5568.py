# 5568 카드 놓기

from itertools import permutations as perm

num_of_cards = int(input()) # 나열한 총 카드 수
selection = int(input()) # 그 중 뽑은 카드 수

card_list = []
for _ in range(num_of_cards):
    card = input()
    card_list.append(card)
# print(card_list)

per = list(perm(card_list, selection))
# print(per) # [('1', '2'), ('1', '12'), ...] 튜플 형태로 반환

int_list = []
for i in range(len(per)):
    if selection == 2:
        newEle = per[i][0] + per[i][1]
    elif selection == 3:
        newEle = per[i][0] + per[i][1] + per[i][2]
    else:
        newEle = per[i][0] + per[i][1] + per[i][2] + per[i][3]
    int_list.append(newEle)
# print(int_list)

remove_duple_list = set(int_list)
print(len(remove_duple_list))

# 18~26 라인 k 값에 따라 동적 처리
# for i in range(len(per)):
#     newEle = ''
#     k = 0
#     while k < selection:
#         newEle += per[i][k]
#         k += 1
#     int_list.append(newEle)
# # print(int_list)
