# 검색하지 말고 혼자 하나씩 생각하기
# 반복문을 돌면서 입력한 수 만큼 * 이 나란히 붙어서 출력된다
# n개 입력 시, n 개 출력 이니까 * 곱하기 n 개 후 1씩 증가
# while n <= 100:
#     print(n*"*")
#     n += 1
# 이렇게 하니 입력한 수 부터 100까지만 출력! 써놓고 보니 당연하다
# 다시 1부터 n 까지 출력으로 아래 test code 작성 후 최종 코드 완성
# 💡 알게된 점! range() 함수의 기능 : range(a) → 0 ~ a-1 까지 1씩 증가해서 출력
# if n == 5:
#     show_star(1)
#     show_star(2)
#     show_star(3)
#     show_star(4)
#     show_star(5)

n = int(input())

def show_star(num):
    print(num * "*")

for i in range(n):
    if n > 100:
        break
    else:
        show_star(i+1)
        i += 1
        if i == n:
            break
