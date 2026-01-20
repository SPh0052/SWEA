N, M = map(int, input().split())

arr = list(range(1, N + 1))
selected = [0] * N   # arr의 i번째를 썼는지 표시 (visited 역할)
subset = []          # 지금 만들고 있는 수열(순서 있음)

def pick(idx, selected, cnt):
    if cnt == M:
        print(' '.join(map(str, subset)))
        return

    # idx는 이제 "depth" 같은 의미라서, idx==N 체크는 필요 없음

    for i in range(N):
        if selected[i]:      # 이미 쓴 숫자면 skip
            continue

        selected[i] = 1
        subset.append(arr[i])

        pick(idx + 1, selected, cnt + 1)

        subset.pop()
        selected[i] = 0

pick(0, selected, 0)
