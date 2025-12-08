num_list = list(map(int,input().split()))

def note():
    for i in range(7):
        if num_list[i] +1 != num_list[i+1]:
            break
    else:
        return 'ascending'

    for i in range(7):
        if num_list[i] -1 != num_list[i+1]:
            break
    else:
        return 'descending'

    return 'mixed'

print(note())