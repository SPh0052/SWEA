#특정한 두 개의 노드에 경로가 존재하는지 확인
#경로가 있으면 1, 없으면 0 출력
#노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있음

T = int(input())


def DFS(start, end):  # s: DFS를 시작할 정점, N: 정점의 개수

    visited = [0] * (V + 1)  # 방문 했는지 안했는지 정점번호(v) 저장 #N은 정점의 개수
    # visted의 인덱스 = 정점 번호
    stack = []  # 갈림길이 나타났을 때의 정점 저장
    curr_v = start  # start: 시작정점 번호, current_v: 현재 탐색 중인 정점, start는 그대로 두고, current_v라는 변수에 "현재 탐색 중인 정점"을 저장해서 이동시키려고 하는 것.
    visited[start] = 1  # 현재 시작한 정점은 방문했다고 표시

    # 시작점 자체가 목표일 수도 있음??????이게 굳이 필요할까??
    if curr_v == end:
        return 1

    while True: #백트래킹하려면 다시 정점 탐색 과정을 반복할 루프가 필요함.
    #스택이 빌 때까지 정점 탐색 과정을 무한 반복
    #for문으로는 정점 한 번만 탐색하고 끝
    # 움직이고 그만 두기
        for nv in range(1,V + 1):  #현재 정점에서 다음 정점 후보를 찾는 반복, 0번 정점은 안 도니까 range(1,V+1)
            if adjM[curr_v][nv] == 1 and visited[nv] == 0:  # 서로 인접, 연결되어 있고 한 번도 방문한 적이 없다면
                stack.append(curr_v)  # 현재 위치를 stack에 저장
                curr_v = nv  # 다음 위치로 넘어가기
                visited[curr_v] = 1  # 넘어간 순간, 방문 기록하기
                if curr_v == end: #이동 직후, 또는 루프 시작 시 바로 체크하는 게 안전하다
                    return 1
                break

        else:  # 만약 서로 인접되어 있는 정점이 없거나, 방문했던 곳이라면
        #for/if-else:구조라면 nv가 한 번이라도 조건에 안 맞으면 바로 else로 들어간다.
        #그런데 그러면 안된다. 다른 후보(nv =2,3,,,)는 확인조차 못 하고 스택팝/종료로 넘어가버림.
        #즉, 갈 수 있는 길이 있어도 첫번 째 후보만 틀리면 길을 못 찾고 돌아가 버림.

            if stack:  # 스택에 전에 갔던 곳이 저장되어 있다면
                curr_v = stack.pop()  # 리스트의 마지막 요소 반환, 리스트에서는 제거
                #없으면 스택에서 꺼내서 이전 정점으로 돌아간 뒤, 그 정점에서 다시 다음 정점 찾기

            else:  # 스택에 없다면
                return 0



for test_case in range(1,T+1):
    V, E = map(int, input().split()) #V : 정점의 개수, E: 간선의 개수
    adjM = [[0] * (V+1) for _ in range(V+1)]  #0은 버퍼, 1부터 쓰기 위해서
    #인접 행렬 저장!!!
    for _ in range(E): #간선의 개수, len(graph)/2와 같음.
        s, e = map(int, input().split())
        adjM[s][e] = 1


    S, G = map(int, input().split())




    print(f'#{test_case} {DFS(S, G)}')
