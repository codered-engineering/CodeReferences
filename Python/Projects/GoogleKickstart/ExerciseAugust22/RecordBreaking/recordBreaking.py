def checkRecord(x, visitors, i):
    j = 0
    while j < i:
        if visitors[j] >= x:
            break
        j += 1
    if j == i:
        return 1
    else:
        return 0


def recordBreaking(number):
    # input
    days = int(input())
    visitors = list(map(int, input().split()))

    # algorithm
    count_records = 0
    i = 0
    for x in visitors:
        if i == days - 1:
            count_records += checkRecord(x, visitors, i)
        elif x > visitors[i + 1]:
            count_records += checkRecord(x, visitors, i)
        i += 1

    # output
    print(f"Case #{number}: {count_records}")


cases = int(input())
i = 1
while i <= cases:
    recordBreaking(i)
    i += 1


