text = input()

totalText = ''
if len(text) <= 100:
    # 0부터 문자열의 길이까지 10씩 증가하는 range() 함수 이용
    for i in range(0, len(text), 10):
        # 문자열의 i부터 (i+10)-1 인덱스까지 출력
        print(text[i:i + 10])

# range() 함수 확실히 이해하기!
# range(start, end, step)
# start : start 부터 리턴
# end : end-1 까지 리턴
# step : start~end 연속된 숫자들 중에, step의 간격씩 리턴
