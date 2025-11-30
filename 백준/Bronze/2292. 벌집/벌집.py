'''
3(n-1)*(n-2)+2 <= x <= 3n(n-1)+1
n은 층이고,
x는 벌집 넘버이다.
'''
'''
#1트
print(int(((X-1)/3 +1/4)**0.5 + 1/2 +1))
이 식으로 썼다면 (X-1)/3 +1/4)**0.5 + 1/2 이 식이 정수일 때 오류가 났겠군.
math.ceil() : 올림(천장)
math.floor() : 내림
math.round() : 반올림
'''
# import math
# X = int(input())
# 
# print(math.ceil(((X-1)/3 +1/4)**0.5 + 1/2))

n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)