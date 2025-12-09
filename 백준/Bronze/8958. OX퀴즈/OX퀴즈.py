T = int(input())


for _ in range(T):
    problem = input()
    score_pro = 0
    total = 0
    for pro in problem:
        if pro == 'O':
            score_pro += 1
            total += score_pro
        else:
            score_pro = 0
    print(total)