#뒤집기: i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 같은 색이면 뒤집고 다른색이면 그대로 둠.
#인덱스: [i-1] 사이에 두고 [i-j-1]~[i-2] / [i]~[i+j-1]
# 0<=i+j-2<N
#0은 흰색, 1은 검정
#toggle: 두 가지 상태를 번갈아 전환하는 것
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #N개 돌, M번 뒤집기 하기
    initial_arr = list(map(int, input().split()))

    flip_list= [list(map(int, input().split())) for _ in range(M)] # [[2,2],[5,1]]

    for flip in flip_list: #flip = [2,2]
        i, j = flip[0], flip[1]
        for k in range(1,j+1):
            if (0<= i-k-1< N) and (0<= i+k-1< N): #if 0 <= i-k and i+k<N: #왼쪽이나 오른쪽으로 벗어나지 않고
                if initial_arr[i-k-1] == initial_arr[i+k-1]:
                    #***toggle
                    initial_arr[i-k-1] = (initial_arr[i-k-1]+1) %2 # 0이면 1로 바뀌고
                    initial_arr[i+k-1] = (initial_arr[i+k-1] + 1) % 2 #1이면 0으로 바뀜...ㄷㄷ미쳤다ㅠㅠ 이거 어떻게 생각해요...

                    # arr[i-k] ^= 1 #0^1 -> 1(서로 달라서)
                    # arr[i+k] ^= 1 #1^1 -> 0(같아서)


                    #내 원래 코드>>
                    # if initial_arr[i+k-1] ==1:
                    #     initial_arr[i + k - 1], initial_arr[i-k-1] = 0,0
                    # elif initial_arr[i+k-1] ==0:
                    #     initial_arr[i + k - 1], initial_arr[i-k-1] = 1,1



    initial_arr = map(str, initial_arr)
    final_arr = ' '.join(initial_arr)
    print(f'#{tc} {final_arr}')