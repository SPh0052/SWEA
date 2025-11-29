'''
처음 5자리 각각 제곱한 수의 합을 10으로
나눈 나머지 6번째 자리수

'''
num_list = list(map(int, input().split()))

total = 0
for num in num_list:
    total +=num**2

print(total%10)