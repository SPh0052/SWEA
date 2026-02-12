'''
칸토어 집합 : 0과 1사이의 실수로 이루어진 집합
[ 0,1]에서 시작해서 각 구간을 3등분하여 가운데 구간을
반복적으로 제외하는 방식

전체 집합은 유한

'''
# N = int(input())

# 파이썬에서는 함수 매개변수로 받은 이름(word)를 global word로 선언할 수 없다.
# word는 "로컬(매개변수)"인데 동시에 "전역"이라고 선언해서 충돌한다.
def divide(idx, word):
    
    if idx == 0:
        # 그냥 return만 하면 자동으로 None 반환.
        return word
    
    # 변수지정
    # one = 3**(idx-1)
    
    # slicing
    # 끝 인덱스가 미포함이다.
    left = word[0:3**(idx-1)]
    right = word[(3**(idx-1))*2:3**idx]
    
    
    # 함수는 실행된다. 그런데 반환값을 버림.
    # 그래서 left는 재귀 이전 값 그대로
    # 반환값을 받아서 left에 갱신***
    left = divide(idx-1, left)
    right = divide(idx-1, right)    
    # 문자열은 불변(immutable)이라서 일부만 직접 수정은 못한다.
    # 슬라이싱 + 이어붙이기로 새 문자열 만들기
    # 반환값을 어디에도 반영하지 않아 word가 갱신되지 않음
    # 계속 반환값을 갱신해야 하는 것을 return에 넣기.
    return left + ' ' * 3**(idx-1) + right
    
    '''
    특히 재귀 함수는 “결과를 위로 반환해서 조립”하는 구조라서,
    word에 담아두는 게 오히려 “이걸 전역으로 누적하는 건가?” 같은 혼동을 만들 수 있어.
    그래서 보통은 조립 결과를 바로 return해.

    결론: 기능상 필수라서가 아니라, 더 깔끔하고 재귀 의도가 분명해져서.
    '''
    

# divide(N, '-'*(3**N))

while True:
    try:
        N = int(input())
    except EOFError:
        break
    print(divide(N, "-" * (3 ** N)))