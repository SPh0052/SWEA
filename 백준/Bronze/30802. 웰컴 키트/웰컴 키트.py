'''
티셔츠 한 장, 펜 한자루 ->웰컴 키트
N 명
T:T장씩 최대 몇 묶음? :
P자루씩 최대 몇 묶음?
-> 같은 사이즈의 T장 묶음으로만 주문 가능
-> 펜을 P자루씩 묶음으로 주문 가능, or 한 자루만 주문 가능.

'''
N = int(input())
shirt_list = list(map(int, input().split()))
T, P = map(int, input().split())

def shirt(num_size):
    if num_size == 0:
        return 0
    if num_size % T == 0: #T개씩 깔끔하게 묶어진다면
        shirt_bundle = num_size // T
    else:
        shirt_bundle = num_size // T + 1
    # print(shirt_bundle)
    return shirt_bundle

shirt_total = 0
for i in shirt_list:
    shirt_total += shirt(i)
    # print(shirt_total)


# 펜 구하기
pen_bundle = N // P
pen_num = N % P

print(shirt_total)
print(f'{pen_bundle} {pen_num}')