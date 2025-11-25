N = int(input()) # num_list 개수
num_list = list(map(int,input().split()))
total = 0

def prime(num):
    for i in range(2, num):
        if num == 2:
            return 1
        if num % i ==0: # 만약 i로 나눠진다면
            return 0

    return 1

for num in num_list:
    if num != 1:
        total += prime(num)

print(total)