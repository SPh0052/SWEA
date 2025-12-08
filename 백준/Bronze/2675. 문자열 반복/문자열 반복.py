T = int(input())
for _ in range(T):
    P = ''
    R, S = input().split() # R은 지금 문자열임 (반복횟수, 문자열)
    for word in S:
        P += word * int(R)
    print(P)