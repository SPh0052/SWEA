N = int(input())

def fac(num):
    
    # 팩토리얼에서는 0!=1 도 처리해야 함으로
    if num <= 1:
        return 1
    return num*fac(num-1)
    #result = num*fac(num-1)
    
    
print(fac(N))
