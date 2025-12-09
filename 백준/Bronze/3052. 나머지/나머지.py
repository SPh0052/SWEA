
num_list = []

for _ in range(10):
    N = int(input())
    if (N%42) not in num_list:
        num_list.append(N%42)

print(len(num_list))