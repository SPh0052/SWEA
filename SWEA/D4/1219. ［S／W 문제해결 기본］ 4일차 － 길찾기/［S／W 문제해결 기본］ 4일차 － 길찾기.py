#일방통행, 방향성 그래프임. 되돌아올 수 없다
#A->B, 0~99사이
#모든길은 순서쌍으로.
#정점(분기점)의 개수가 최대 100개이기 때문에,
#size[100]의 정적배열 2개 선언,
#각 정점의 번호를 주소로, 데이터는 도착하는 정점의 번호로 저장

T = 10
V = 99


def DFS(start, V):
    visited = [0] * (V + 1)  # 1번부터 N정점까지 기록
    stack = []  # 갈림길 생기면 정점 빼놓는?
    curr_v = start  # s가 계속 바뀌므로
    visited[curr_v] = 1
    while True:
        for nv in adjL[curr_v]:  # 인접한 정점만 꺼내옴
            if visited[nv] == 0:
                stack.append(curr_v)  # 저장하고
                curr_v = nv  # 점프
                if curr_v == 99:
                    return 1
                visited[curr_v] = 1
                break  # for문을 종료시킴

        else:  # break없이 끝까지 실행됐을 때만 else 블록이 실행됨
            # 만약 이웃 중에 갈 만한 정점이 하나도 없으면
            # 스택에서 이전 정점으로 되돌아가기(백트래킹) 수행
            if stack:
                curr_v = stack.pop()

            else:
                return 0

for _ in range(1, T+1):
    tc, E = map(int, input().split())
    graph = list(map(int, input().split()))
    adjL = [[] for _ in range(V + 1)]
    for i in range(E):
        s, e = graph[2*i], graph[2*i+1]
        adjL[s].append(e)

    print(f'#{tc} {DFS(0, V)}')

