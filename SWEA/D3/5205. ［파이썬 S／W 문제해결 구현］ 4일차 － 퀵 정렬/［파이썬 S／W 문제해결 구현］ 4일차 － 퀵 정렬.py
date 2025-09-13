'''
퀵 정렬
N개의 정수 정렬하여 A에 넣고,
A[N//2] 저장된값 출력
'''

T = int(input())


#퀵정렬

def hoare_partition(left, right):
# 가장 왼쪽 값을 pivot이라고 정의
# 각 끝 값을 left, right로 하고
    pivot = arr[left]
    i = left + 1
    j = right
    
    #i == j 일 경우도 탐색해야 됨. 그 위치가 pivot보다 큰지 작은지
    while i <= j:
        
        while i<=j and arr[i] <=pivot: # pivot보다 작은 값이라면
            i +=1
            
        while i<=j and arr[j] >= pivot: #pivot보다 큰 값이라면
            j-=1
            
        #각자 i:큰값, j: 작은 값을 찾았을 때,
        # 찾았는데 이미 교차되었을 수도 있으니까
        if i< j:
            arr[i], arr[j] = arr[j], arr[i]
            
    #swap하는 것도 다 끝남
    # pivot을 넣는 것과, arr[left]를 넣는 것은 다름
    arr[left], arr[j] = arr[j], arr[left]
    #pivot, arr[j] = arr[j], pivot
    #<-pivot은 그냥 변수일 뿐이고 배열이랑 연결돼 있지 않음
    # pivot = arr[j] <- 'pivot'변수에 arr[j]값 저장
    # arr[j] = pivot <- arr의 j자리에 pivot값 저장
    #그래서 pivot값이 반복되어 나올 것임
    
    #재귀로 왼쪽파트, 오른쪽파트 호어파티셔닝 돌려야함
    return j

# i,j 포인터를 써서 서로서로 가까워지면서
#i: pivot보다 큰 값, j: pivot보다 작은 값 탐색
# 그리고 결국 i>j로 교차되었다?
# 그러면 pivot과 arr[j] swap 후 종료

#여기에 left, right 변수 넣어야 하는 이유가
#왼쪽파트, 오른쪽파트로 나뉨에 따라 left, right 값이 바뀌어서
def quick_sort(left, right):
    
    if left< right:
        pivot = hoare_partition(left, right)
        
        quick_sort(left, pivot -1)
        quick_sort(pivot+1, right)

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, len(arr)-1)
    print(f'#{tc} {arr[N//2]}')
