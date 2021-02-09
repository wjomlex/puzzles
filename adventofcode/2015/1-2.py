import sys

ins = sys.stdin.readline().strip()
floor = 0
idx = 0

for c in ins:
  idx += 1
  if c == '(': floor += 1
  else: floor -= 1

  if floor == -1:
    print idx
    break
