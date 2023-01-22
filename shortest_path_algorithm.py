from constants import computer_interpretation_of_the_map, WALLS_POSITIONS


def make_step(k, m):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if i > 0 and m[i-1][j] == 0 and computer_interpretation_of_the_map[i-1][j] == 0:
          m[i-1][j] = k + 1
        if j > 0 and m[i][j-1] == 0 and computer_interpretation_of_the_map[i][j-1] == 0:
          m[i][j-1] = k + 1
        if i < len(m)-1 and m[i+1][j] == 0 and computer_interpretation_of_the_map[i+1][j] == 0:
          m[i+1][j] = k + 1
        if j < len(m[i])-1 and m[i][j+1] == 0 and computer_interpretation_of_the_map[i][j+1] == 0:
           m[i][j+1] = k + 1


def calculate_path(start, end):
    if computer_interpretation_of_the_map[end[0]][end[1]] == 1:
        return -1

    m = []
    for i in range(len(computer_interpretation_of_the_map)):
        m.append([])
        for j in range(len(computer_interpretation_of_the_map[i])):
            m[-1].append(0)

    i, j = start
    m[i][j] = 1

    k = 0
    while m[end[0]][end[1]] == 0:
        k += 1
        make_step(k, m)


    i, j = end
    k = m[i][j]
    the_path = [(i, j)]
    while k > 1:
      if i > 0 and m[i - 1][j] == k-1:
        i, j = i-1, j
        the_path.append((i, j))
        k-=1
      elif j > 0 and m[i][j - 1] == k-1:
        i, j = i, j-1
        the_path.append((i, j))
        k-=1
      elif i < len(m) - 1 and m[i + 1][j] == k-1:
        i, j = i+1, j
        the_path.append((i, j))
        k-=1
      elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
        i, j = i, j+1
        the_path.append((i, j))
        k -= 1

    return the_path[::-1]
