# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    word = []
    for _ in range(5):
        word.append(input())

    word_list = []

    for i in range(15):
        for j in range(5):
            if len(word[j]) <= i:
                continue
            else :
                word_list.append(word[j][i])

    print(f"#{test_case} {''.join(word_list)}")