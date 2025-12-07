H, M = map(int, input().split())

'''
하루가 넘어갈 때 표현
'''
if M < 45:
    if H>0:
        H -=1
    else:
        H = 23
    M += 15
else:
    M -= 45

print(f'{H} {M}')