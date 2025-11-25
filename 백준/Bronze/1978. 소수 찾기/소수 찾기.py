N = int(input()) # num_list 개수
num_list = list(map(int,input().split()))
'''
**제곱근까지만 검사하기!
1. 약수는 항상 '짝'으로 다닌다.(작은 수 x 큰수) 형태로
예를 들어 36:

1 × 36
2 × 18
3 × 12
4 × 9
6 × 6

그런데 이게 제곱근을 기준으로 작은 쪽/ 큰쪽 이 갈린다.
'''
# 제곱근까지만 검사하기!
# 2일 때
def prime(num):
    if num < 2:
        return 0 # return에 아무런 값도 없으면 None을 반환하므로
                 # return값을 쓴다면 무조건 값을 넣어주기.
    for i in range(2, int(num**0.5)+1):
        #만약 num = 2라면 range는 빈 범위를 가지므로 for문이 작동하지 않는다!
        if num % i ==0: # 만약 i로 나눠진다면 소수가 아니야!
            return 0
    return 1

cnt = 0
for num in num_list:
        cnt += prime(num)

print(cnt)