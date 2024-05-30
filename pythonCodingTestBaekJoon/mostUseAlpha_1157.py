# 단어를 입력받고 대문자로 변환
word = input()
wordUpper = word.upper()
max_count = 0
most_char = []
word_dict = {} # 대문자 알파벳과 알파벳 출력 수가 담긴 딕셔너리


# 각 알파벳 개수 계산
for char in wordUpper:
    if char in word_dict:
        word_dict[char] += 1
    else:
        word_dict[char] = 1


for char, count in word_dict.items():
    if count > max_count:
        max_count = count # 가장 큰 수로 max_count 에 지정
        most_char = [char] # count 수 큰 값을 가진 문자로 지정
    elif count == max_count:
        most_char.append(char) # 같은 큰 수 가지면 배열에 알파벳 추가

# 결과 출력
if len(most_char) > 1:  # 가장 많이 나온 문자가 여러 개인 경우
    print("?")
else:
    print(most_char[0])
