'''
0층 1호 : 1명
1층 1호 :1명

3층 4호
: 2층 1~4호
: 1층 1호 + (1층 2호)
: 0층 1호 + (0층 1 + 0층 1~2호)



1 1+3 1+3+6
'''

T = int(input())


for _ in range(T):
    k = int(input())
    n = int(input())

    # 0층 더하기
    # 0호 남겨두기
    floor_k = []
    floor_k.append(0)
    for i in range(1, n+1):
        floor_k.append(i)

    for floor in range(1, k+1):
        for room in range(1, n+1):
            floor_k[room] += floor_k[room-1]

    print(floor_k[n])

    # 1층 만들기
    '''
    1호 : floor_0[0]
    2호 : [0] + [1]
    '''




