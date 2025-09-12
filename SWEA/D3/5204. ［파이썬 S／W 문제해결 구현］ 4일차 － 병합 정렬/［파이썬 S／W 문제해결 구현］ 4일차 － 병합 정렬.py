'''
N개의 정렬대상

L[0  : N//2], L[N//2 : N]
병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력

N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력
left
'''

#병합하면서 정렬하기
def merge(left, right):
    result = [0] * (len(left) + len(right))  # 너무 낭비 아닌가? 각자의 길이가 1씩 있을텐데, 그거를 계속 만든다고?
    l = r = 0
    cnt = 0 #**이거를 왜 해야할까? 이거 하면 안되는 거 아냐? 그러면 지금까지 센 게 초기화 될 것 같아


    if left[-1] > right[-1]:
        cnt +=1
        
    while l < len(left) and r < len(right):

        if left[l] <= right[r]:
            result[l+r] = left[l] # l이 넣어졌으니까
            l+=1

        else : # 클 때 # 오른쪽이 작아야 먼저 복사됨
            result[l+r] = right[r] # r이 작아서 r이 넣어짐
            r+=1


    # left가 남았을 때
    while l < len(left):
        result[l+r] = left[l]
        l+=1

    while r < len(right):
        result[l+r] = right[r]
        r+=1

    return result, cnt





# 분할하기
def merge_sort(li):

    #재귀함수 기저조건
    if len(li) == 1:
        return li, 0

    mid = len(li) // 2 #N//2 : 현재 리스트 길이 기준으로 나누기
    left = li[:mid]
    right = li[mid:]

    left_list, left_cnt = merge_sort(left)
    right_list, right_cnt = merge_sort(right)

    merge_list, merge_cnt = merge(left_list, right_list)

    # left_cnt : 왼쪽 리스트 안에서 발생한 횟수, right_cnt: 오른쪽 리스트 안에서 발생한 횟수, merge_cnt = 왼쪽과 오른쪽을 합칠 때 새로 발생한 횟수
    return merge_list, left_cnt + right_cnt + merge_cnt



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sorted_list, cnt = merge_sort(arr)
    print(f'#{tc} {sorted_list[N//2]} {cnt}')



# while문 안에서는 양쪽 포인터가 동시에 마지막에 도달해야만 세게 되는데, 실제 병합 과정에서는 거의 동시에 안 끝남
