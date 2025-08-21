# 맨 앞의 숫자: front
# 맨 뒤의 숫자: rear
# 맨 앞에 있는 숫자를 알려면? 한 번 더 꺼내야 됨.

# 꺼내서 뒤로 넣기
#dequeue 와 enqueue를 M번 반복

#원형큐

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) #N개의 숫자, M개
    cq = [0] + list(input().split()) #입력받은 건 0~N까지 총 N+1개 원소인데,
                                     # front, rear 계산을 보면 0~ N-1범위만 쓴다고 가정함.
                                    # N개의 원소가 0~N-1 인덱스를 차지해야 원형 큐 연산이 정상적으로 돎  

    front = 0
    rear = N

    for _ in range(M): #N개인데 왜 +1함? front 때문에. front,1,,,N-1인 것.
        front = (front+1) % (N+1)   # N+1은 개수, #front = 0 일 때는 아무런 값도 없으므로 1부터 시작함.
        rear = (rear+1) % (N+1)   #N+1인 이유는 front와 rear를 구분하기 위해 1칸을 비워두는 원형 큐의 특징
        cq[rear] = cq[front]

    #여기까지 M회 끝남.
    # 그리고 이 때의  front가 rear로 옮겨진 거니까, front 다음 값이 이 답의 문제가 된다.
    
    front = (front+1) % (N+1)   #front +=1을 하면 안된다!!!

    print(f'#{tc} {cq[front]}')

    