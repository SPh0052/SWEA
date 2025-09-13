'''
서로 다른 정수 N개
-> '정렬된' 리스트 A에 저장
리스트 B에 저장된 M개의 정수
가 A에 들어있는 수인지 확인

A에 들어있으면서,
탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수(-> 양쪽 끝 값이 아니라, 중간에 있는 값들 중에 target을 정해라)

예를 들어 10을 찾는 경우 오른쪽-오른쪽 구간을 선택하므로 조건에 맞지 않는다
'''

T = int(input())


    
def binary_search(target):
    left = 0
    right = len(A) - 1 # A에서 검사하니까
    stack = []
    
    while left <= right:
        #mid의 위치가 계속 바뀌므로 while문 안에 넣어줘야 됨
        mid = (left + right) // 2
        #값이 같으면 -> 찾았네? 탐색 종료
        if target == A[mid]:
            #타겟이 어느 위치에 있는지 return
            return 1
        
        elif target < A[mid]:
            right = mid - 1
            #if stack and 'l' == stack.pop():
            #pop()을 하면 반환하면서 삭제시키기 때문에 안된다.
            # 그리고 pop()을 2번하면 stack안에 없는데 pop을 시킬 수도 있으므로 IndexError가 날 수도 있음
            if stack and 'l' == stack[-1]:

                return 0
            else:
                stack.append('l')
            
        else:
            left = mid +1
            if stack and 'r' == stack[-1]:
                return 0
            else:
                stack.append('r')
            
    return 0
            
    #이렇게 다 했는데도 안 찾아지고
    #left >right 가 되었다? 교차되었다? 없는 거임
    #return -1
    #return값 있을 필요 없음. 리턴할 값이 필요없으니까
    #지만 **return이 없으면 자동으로 'None'을 반환하기 때문에, 그걸 바로 cnt에 더한다.

# B가 A에 있는지 확인

#target은 모든 B의 요소

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for b in B:
        cnt += binary_search(b)
        
    print(f'#{tc} {cnt}')
    
#stack 말고 last_dir = 0, -1 ,+1로 해서 푸는 방법도 있음.
#최근 '1번만'보면 되니까, 스택을 쓰지 않고 '변수 하나'로 단순화할 수 있다.