N = int(input()) # 숫자의 개수
# num_list = list(map(int, input())
num_list = list(input())
total = 0
for i in num_list:
    total += int(i)
print(total)