# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
  N = int(input())
  price = list(map(int, input().split()))

  max_price = 0
  profit = 0

  for i in reversed(price): # 뒷쪽부터 반복문 시작
    if i > max_price: # 해당 값이 최댓값보다 크면
      max_price = i #해당 값을 최댓값으로 지정

    else: # 아니라면
      profit += (max_price - i) # 최댓값에서 뺀 값을 이익에 더하기


  print(f'#{test_case} {profit}')