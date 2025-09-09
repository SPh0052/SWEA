'''
맞으면 1, 아니면 0

S를 함수의 인자로 전달받아 팰린드롬 여부를 반환값으로 알아낼 것이다
recursion 함수를 몇번 호출하는지 세기
'''

T = int(input())
depth = 0

def recursion(s, l, r, depth):
    depth +=1
    if l >= r: return 1, depth  # 기저조건
    elif s[l] != s[r]: return 0, depth  # 하나라도 다르다면 return 0
    else: return recursion(s, l+1, r-1, depth)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0) #index니까 총길이-1

for T in range(T):
    S = list(input())
    result, cnt = isPalindrome(S)
    print(f'{result} {cnt}')

#반환값, 함수호출횟수