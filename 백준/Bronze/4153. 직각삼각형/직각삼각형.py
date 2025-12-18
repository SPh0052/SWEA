while True:
    tri_len = list(map(int, input().split()))

    tri_len.sort()
    if sum(tri_len) == 0:
        break
    if tri_len[2]**2 == tri_len[0]**2 + tri_len[1]**2:
        print('right')
    else:
        print('wrong')