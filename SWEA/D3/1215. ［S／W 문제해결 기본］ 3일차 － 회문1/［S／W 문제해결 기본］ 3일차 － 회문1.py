T = 10  # Number of test cases


# Function to check if a string is a palindrome
def palindrome(txt):
    for p in range(M // 2):
        if txt[p] != txt[M - 1 - p]:
            return False
    return True

# Loop over each test case
for test_case in range(1, T + 1):
    N = 8  # Grid size (8x8)
    M = int(input())  # Length of palindrome to search for
    arr = [list(input()) for _ in range(N)]  # Grid input


    # Count of palindromes
    cnt_ans = 0

    # Case where M = 1 (every cell is a palindrome)
    if M == 1:
        cnt_ans = N * N
    else:
        # Check horizontally (rows)
        for i in range(N):
            for j in range(N - M + 1):
                txt_list = arr[i][j:j + M]  # Extract substring from the row
                if palindrome(txt_list):
                    cnt_ans += 1

        # Check vertically (columns)
        for j in range(N):
            for i in range(N - M + 1):
                # Extract substring from the column
                txt_list = [arr[k][j] for k in range(i, i + M)]
                if palindrome(txt_list):
                    cnt_ans += 1

    # Output the result for the current test case
    print(f'#{test_case} {cnt_ans}')
