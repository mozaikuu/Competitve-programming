def elder_age(m, n, l, t):
  lines = []

  for i in range(m):
    row = []

    for j in range(n):
      curr = 0 if i == j else i % t ^ j % t

      row.append(curr - l) if curr >= l else None

    lines.append(sum(row))

  total = sum(lines)

  return total % t