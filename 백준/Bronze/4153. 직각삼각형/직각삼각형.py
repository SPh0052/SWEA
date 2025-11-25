'''
주어진 세 변의 길이로 삼각형이 직각인지 구분하시오
맞다면 right, 아니라면 wrong
'''
while True:
    tri_list = list(map(int, input().split()))
    if sum(tri_list) == 0:
        break
    tri_list.sort()

    if tri_list[2]**2 == tri_list[0]**2 + tri_list[1]**2:
        print("right")
    else:
        print("wrong")

