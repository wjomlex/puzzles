import sys

ins = sys.stdin.readline().strip()
h = set()
r, c = 0, 0

for d in ins:
  if d == '^': r -= 1
  elif d == '<': c -= 1
  elif d == '>': c += 1
  else: r += 1
  tup = (r, c)
  h.add(tup)

print(len(h))
