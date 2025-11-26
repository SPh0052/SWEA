'''
NxN 미로에서 경로가 존재하는지?
가능하면 1,
불가능이면 0

2 ->3에 도착할 수 있을까?
0은 통로, 1은 길
'''
# answer = 0으로 두고 시작할 수도 있다.

T = int(input())


def DFS(si, sj):

    global answer

    visited[si][sj] = 1

    if miro[si][sj] == 3:
        answer = 1

    else:
        # 답을 못 찾았다면 다른 위치로 이동
        for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
            ni, nj = si + di, sj + dj

            # miro == 0이라고 하지말고, 출발점과 도착점 값이 있으니까
            # 0~N 안에 있는지 범위를 먼저 조건으로 걸어야 한다. miro[ni][nj] != 1 이거를 먼저 검사한다면
            #indexError가 날 수 있다.
            #ni, nj가 이런 조건을 만족한다면
            if 0<=ni<N and 0<=nj<N and miro[ni][nj] != 1 and not visited[ni][nj]:
                # si, sj = ni, nj 로 다시 DFS 돌림.
                DFS(ni,nj)




for tc in range(1, T + 1):

    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]


    visited = [[0] * N for _ in range(N)]

    answer = 0

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:   # 출발점 찾기
                si, sj = i, j     # 출발점 (si, sj) 저장
                break
    DFS(si, sj)
    print(f'#{tc} {answer}')

# 막혔다?
# visited 스택에서 방문한 점들 꺼내서 다시 되돌아가;
#그러다가 안 막힌 구간 찾아내잖아? 그럼 가