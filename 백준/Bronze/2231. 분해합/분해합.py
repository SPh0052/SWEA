N = int(input())

# 어차피 다 돌릴 거라면 생성자 1부터 찾기.
# 최솟값이 바로 나오니까.
for i in range(1,N+1):
    # i의 각 자리수 더하기.
    cons = sum(map(int,str(i))) + i
    
    if cons == N:
        print(i)
        break
    
    # 생성자 i ==N 이라는 것은 생성자가 없다는 뜻    
    if i == N:
        print(0)