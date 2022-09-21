def CandyCoverage(number):
    (bags, kids) = tuple(map(int, input().split()))
    candies = list(map(int, input().split()))
    sum_candies = sum(candies)
    remain = sum_candies % kids
    print(f"Case #{number}: {remain}")

cases = int(input())
i = 1
while i <= cases:
    CandyCoverage(i)
    i += 1

