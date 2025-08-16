#N개의 0과 1로 이루어진 수열
#"연속한" 1의 개수 중 최댓값 출력
# 1시작 -> 세다가 0 만나면 다시 초기화

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(input())
    result = []
    cnt_1 = 0
    for i in range(N):
        if arr[i] == '1':
            cnt_1 += 1
            #if max_v < c:
                #max_v = c #c를 하나씩 더 해서 그 때마다 max_v와 비교하기. 그리고 제일 큰 값 출력

        else: #0이 출현하면
            result.append(cnt_1) #1이 마지막으로 끝났을 때는?
            cnt_1 = 0

    result.append(cnt_1) #1이 마지막으로 끝났을 때도 포함


    print(f'#{tc} {max(result)}')
