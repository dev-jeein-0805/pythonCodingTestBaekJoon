# 11557 Yangjojang of The Year

# T : 테스트 케이스 개수 -> 딕셔너리 개수 출력
# N : 각 딕셔너리에서 pair 개수 출력
# 딕셔너리 구조 : {학교이름(str) : 지난 해 소비한 술의 양(int)}

# 입력 받을 테스트 케이스 개수
T = int(input())

# 마지막에 한번에 출력할 학교이름을 담은 리스트 초기화
final_univ_list = []
for _ in range(T):
    N = int(input())

    univ_dict = {}
    for _ in range(N):
        input_pair = input().split(' ')
        univ_name = input_pair[0]  # 학교 이름
        alcohol_amount = int(input_pair[1])  # 지난 해 소비한 술의 양
        univ_dict[univ_name] = alcohol_amount

    # 생성된 딕셔너리 출력
    # print(univ_dict)

    # 가장 많은 술을 소비한 학교 이름 출력
    max_univ = max(univ_dict, key=univ_dict.get)
    # print(max_univ)
    final_univ_list.append(max_univ)

for univ in final_univ_list:
    print(univ)

# 17 라인 : input_pair = input().split(' ')
# input() 함수: ★문자열(str) 형태★로 사용자로부터 입력받음.
# .split() 메소드: 문자열을 특정 구분자를 기준으로 나누어 ★리스트 생성★

# 26 라인 : max_univ = max(univ_dict, key=univ_dict.get)
# max() 함수: 주어진 컬렉션(리스트, 딕셔너리 등)에서 가장 큰 값을 찾아 반환하는 함수
# max() 함수는 univ_dict의 각 키를 univ_dict.get 함수에 전달, 이 함수가 반환하는 값(=key 의 value)을 기준으로 최댓값을 찾아 value(최고 술 소비량)의 key(학교 이름) 를 반환 
