# 2061 좋은 암호

K, L = map(int, input().split())

# 소인수분해 함수
def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors

if min(prime_factors(K)) >= L:
    print('GOOD')
else:
    print('BAD', min(prime_factors(K)))
