def recordBreaking(cases):
    #input
    days = int(input())
    visitors = list(map(int, input().split()))

    #algorithm
    i, count_records, current_record = 1, 0, 0
    if len(visitors) == 1 and visitors[0] > 0:
        count_records += 1
        current_record = visitors[0]
    elif visitors[0] > visitors[1]:
        current_record = visitors[0]
        count_records += 1
        i += 1

    while i < days-1:
        if visitors[i] > current_record:
            current_record = visitors[i]
            if current_record > visitors[i+1]:
                count_records += 1
                i += 1
        i += 1

    if visitors[-1] > current_record:
        count_records += 1

    #output
    print(f"Case #{cases}: {count_records}")


cases = int(input())
for j in range(1, cases+1):
    recordBreaking(j)

