'''
자연수 N의 분해합은
N과, .N을 이루는 각 자리수의 합

M: N의 생성자 : M의 분해합이 N인 경우
생성자가 없을 수도 있다
생성자가 여러 개인 자연수도 있을 수 있다
N의 가장 작은 생성자는?
엥 그냥 생성자 고정 아닌가...????
최소값 구할 수 있는겨??
198+1+9+8 =?
B+1+9+8 =N
'''

N = int(input()) # 문자열
num_list = []

for i in range(N-1, 0 ,-1): # 생성자가 N-1일 때부터 줄여보기
    total = 0
    total +=i # 생성자 ==N-1
    for j in str(i): #j: 자리수 더하는 거
        total += int(j)
    if total == N:
        num_list.append(i)

if num_list:
    print(min(num_list))
else:
    print(0)