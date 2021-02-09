import sys

ins = sys.stdin.readline().strip()
floor = 0

for c in ins:
  if c == '(': floor += 1
  else: floor -= 1

print floor
