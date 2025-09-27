'''
NxN 배열
MxM의 파리채

N: 5~15
M: 2~N
파리개수: 30이하

최대의 파리개수?
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_flies_list = []
    for i in range(N-M+1): # N-M-1
        for j in range(N-M+1):
            total_flies = 0
            for p in range(i, i+M):
                for q in range(j, j+M):
                    if 0 <= p < N and 0 <= q < N:
                        total_flies += arr[p][q]

            total_flies_list.append(total_flies)

    max_v = max(total_flies_list)

    print(f'#{tc} {max_v}')

