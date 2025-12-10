N, M = map(int, input().split())
num_list = list(map(int, input().split()))

max_v = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            s = num_list[i] + num_list[j] + num_list[k]
            if s <= M and s > max_v:
                max_v = s

print(max_v)
