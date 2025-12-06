'''
정문으로부터 거리가 가장 짧도록 방 배정
정문 : 일층 엘리베이터 바로 앞
정문에서 엘리베이터까지의 거리 무시
모든 인접한 두 방사이의 거리 동일
호텔의 정면 쪽에만 방이 있음
W : 방 개수
H : 층

층수 엘리베이터에서 세었을 때의 번호
거리 같을 때는 아래층의 방 선호
Y XX
YY XX

N번째로 도착한 손님에게 몇 번 방?
H다 돌고
그다음 W
'''

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    cnt  = 0

    for width in range(1, W+1):
        for height in range(1, H+1):
            cnt +=1
            if cnt == N:
                if width < 10:
                    print(f'{height}0{width}')
                else:
                    print(f'{height}{width}')
                break