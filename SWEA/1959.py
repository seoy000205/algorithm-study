# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M: # 만약 N이 더 크다면
      A, B = B, A # 적은 리스트를 A로 지정
      N, M = M, N # 작은값을 N으로 지정

    max_sum = 0

    for i in range(M - N + 1):  # 짧은 배열이 이동할 수 있는 범위만큼 반복
        num_sum = 0
        for j in range(N):
            num_sum += A[j] * B[i+j]  # B리스트를 한칸씩 뒤로 미루면서 계산

        if num_sum > max_sum: # 더한 값이 최댓값보다 크면
            max_sum = num_sum # 최댓값으로 지정

    print(f'#{test_case} {max_sum}')