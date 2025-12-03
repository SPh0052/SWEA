N, X = map(int, input().split())
num_list = list(map(int, input().split()))
ans_list = []

for num in num_list:
    if num < X:
        ans_list.append(num)

print(' '.join(map(str,ans_list)))
# print(' '.join(str(ans_list))) # str([1, 4, 5])  →  "[1, 4, 5]"

