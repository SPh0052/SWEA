
while True:
    num = input()

    if num == '0':
        break

    # int로 정수로 만들지 말고 그냥 몫을 구하기
    # num == num[::-1]
    for i in range(len(num)//2):
        if num[i] != num[-i-1]:
            print('no')
            break
    else:
        print('yes')

'''
while True:
    # 문자열 양쪽 끝의 공백(스페이스, 줄바꿈 등)을 제거해줘.
    num = input().strip()
    
    if num == "0":
        break
    
    # 원래 문자열 == 뒤집은 문자열
    if num == num[::-1]:
        print("yes")
    else:
        print("no")
***
num[::-1] 뜻부터
num[start : end : step]


start, end를 생략

step = -1

👉 문자열을 뒤집어라 라는 뜻
'''