def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    N, R, C, Sr, Sc = map(int, input().split())
    instructions = input()

    final_r, final_c = end_position(N, R, C, Sr, Sc, instructions)
    print(f'Case #{test_case}: {final_r} {final_c}')

def end_position(N, R, C, Sr, Sc, instructions):
  # TODO: Complete this function and return the final position (row, column) of
  # the robot
  final_r, final_c = Sr, Sc
  visitedSquares = [(Sr, Sc)]
  i = 0
  while i < N:
      # movement
      move = instructions[i]
      if move == "N":
          final_r -= 1
      elif move == "E":
          final_c += 1
      elif move == "S":
          final_r += 1
      else:
          final_c -= 1
      # checking if robot has been in current square before
      if (final_r, final_c) not in visitedSquares:
          visitedSquares.append((final_r, final_c))
          i += 1

  return final_r, final_c

if __name__ == '__main__':
  main()