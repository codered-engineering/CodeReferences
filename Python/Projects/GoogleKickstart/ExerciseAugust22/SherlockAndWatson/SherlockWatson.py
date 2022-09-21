def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        A, B, N, K = map(int, input().split())

        total = calcPairs(A, B, N, K)
        print(f'Case #{test_case}: {total}')

def calcPairs(A, B, N, K):
    total = 0
    for i in range(1, N+1):
        iAmodK = (i ** A) % K
        for j in range(1, N+1):
            if i == j:
                None
            elif (iAmodK + (j**B)) % K == 0:
                total += 1
    return total % 1000000007

if __name__ == '__main__':
  main()