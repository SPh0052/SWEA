'''
T = int(input())

def answer():
    for _ in range(T):
        H, W, N = map(int, input().split())

        # N번째 손님의 층과 호수 계산
        floor = N % H
        room = N // H + 1

        if floor == 0:   # H의 배수인 경우(꼭대기층)
            floor = H
            room = N // H

        # 방 번호 출력 (호수는 항상 2자리)
        print(f"{floor}{room:02d}")

answer()


'''

T = int(input())

def answer():
    for _ in range(T):
        H, W, N = map(int, input().split())
        cnt  = 0
        done = False

        for width in range(1, W+1):
            for height in range(1, H+1):
                cnt +=1
                if cnt == N:
                    #{값:형식}={height:02}
                    # 0 : 빈자리는 0으로 채워라
                    # 전체 길이는 2자리로 맞춰라
                    print(f'{height}{width:02}')
                    done = True
                    break
            if done:
                break

answer()




                # 이 코드에서의 문제점
                # 1. break 문은 가장 인접한 반복문 한 개만 중지시킨다.
                # 그래서 break를 해도 for width 쪽은 다 돈다.
                # 2. f-string 써서 더 간단하게 하기.
                # if width < 10:
                #     print(f'{height}0{width}')
                # else:
                #     print(f'{height}{width}')
                #break
