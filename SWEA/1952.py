# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    day_price, month_price, three_month_price, year_price = map(int, input().split())
    days = [0] + list(map(int, input().split()))

    min_cost = year_price

    def dfs(month, cost):
        global min_cost

        if cost >= min_cost:    # 이미 최솟값보다 큰 경우 넘어가기
            return

        if month >= 13:
            if cost < min_cost:
                min_cost = cost
            return

        # 1일권 선택
        dfs(month + 1, cost + (days[month] * day_price))

        # 1달권 선택
        dfs(month + 1, cost + month_price)

        # 3달권 선택
        dfs(month + 3, cost + three_month_price)

    dfs(1, 0)
    print(f'#{test_case} {min_cost}')