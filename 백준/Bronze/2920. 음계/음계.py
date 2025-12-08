num_list = list(map(int,input().split()))
'''
a = list(map(int, input().split()))
 
if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')
'''
# or a.sort()
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