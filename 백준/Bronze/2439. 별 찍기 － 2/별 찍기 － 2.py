N = int(input())
blank = ' '
star = '*'
for i in range(1, N+1):
    print(f'{blank* (N - i)}{star*i}')