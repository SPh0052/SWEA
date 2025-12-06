# 한 줄에 있을 때만 가능
# num_list = list(map(int, input().split("/n")))

num_list = [int(input()) for _ in range(9)]

max_v = float('-inf')
max_i = 0

for i in range(9):
    if num_list[i] > max_v:
        max_v = num_list[i]
        max_i = i

print(max_v)
print(max_i+1)