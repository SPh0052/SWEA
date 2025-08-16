#뒤집기: 인덱스: i번째 부터 j개의 돌을 i번째 돌의 색으로 바꿔놓음. 5,6,7
#인덱스: i-1~ i+j-2
#뒤집기는 가능한 돌에 대해서만 진행함.
# 0<=i+j-2<N
#0은 흰색, 1은 검정
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #N개 돌, M번 뒤집기 하기
    initial_arr = list(map(int, input().split()))

    flip_list= [list(map(int, input().split())) for _ in range(M)] # [[2,2],[5,1]]

    for flip in flip_list: #flip = [2,2]
        i, j = flip[0], flip[1]
        i -=1 #인덱스 니까!!! 인덱스 줄이기,,

        if initial_arr[i] == 0:#**i번째니까 인덱스는 i-1!!!
            for k in range(i, i+j):   # if i+k >= N:  # 배열 오른쪽 끝을 넘으면 중단
                if 0<=k<N:            #     break
                    initial_arr[k] =0 # arr[i+k] = arr[i]

        elif initial_arr[i] == 1:
            for k in range(i, i+j):
                if 0 <= k < N:
                    initial_arr[k] =1

    initial_arr = map(str, initial_arr)
    final_arr = ' '.join(initial_arr)
    print(f'#{tc} {final_arr}')