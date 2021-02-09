import sys

ins = sys.stdin.readline().strip()
h = set()
r1, c1 = 0, 0
r2, c2 = 0, 0
is1 = True

for d in ins:
  if is1:
    if d == '^': r1 -= 1
    elif d == '<': c1 -= 1
    elif d == '>': c1 += 1
    else: r1 += 1
    tup = (r1, c1)
    h.add(tup)
  else:
    if d == '^': r2 -= 1
    elif d == '<': c2 -= 1
    elif d == '>': c2 += 1
    else: r2 += 1
    tup = (r2, c2)
    h.add(tup)

  is1 = not is1

print(len(h))
