# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
  N = int(input())
  price = list(map(int, input().split()))

  max_price = 0
  profit = 0

  for i in reversed(price):
    if i > max_price:
      max_price = i

    else:
      profit += (max_price - i)


  print(f'#{test_case} {profit}')