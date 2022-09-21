def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        N = int(float(input()))
        lines = list(map(int, input().split()))
        P = int(input())
        cities = []
        for i in range (1, P+1):
            cities.append(int(input()))

        buses = ''
        for city in cities:
            buses += GBusesPerCity(N, lines, city)
        print(f'Case #{test_case}:{buses}')
        if test_case < test_cases:
            tmp = input()

def GBusesPerCity(N, lines, city):
    bus = 0
    for i in range(0, 2*N, 2):
        start_line = lines[i]
        end_line = lines[i+1]
        while start_line <= end_line:
            if start_line == city:
                bus += 1
                break
            start_line += 1
    return " " + str(bus)

if __name__ == '__main__':
  main()