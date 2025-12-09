'''
find() 함수
S.find(x) : 어떤 찾는 문자가 문자열 안에서 첫 번재에 위치한 순서를 숫자로 출력
S.index(x) : 문자열 안에서 그 수의 인덱스 출력
'''
# s = input()


s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in s:
        # 백준에서는 줄 끝 공백 무시한다.
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')
'''
#'-97'하기
# print(ord('a'))
#28개 : 0-27 인덱스
num_list = [-1]*26
for i in range(len(s)):
    #s[i] : 0번 글자
    if num_list[ord(s[i])-97] == -1:
        num_list[ord(s[i])-97] = i

print(' '.join(map(str, num_list)))
'''