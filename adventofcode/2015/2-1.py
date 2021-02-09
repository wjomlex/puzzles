import sys

sum = 0

for line in sys.stdin:
  line = line.strip()

  l, w, h = [int(x) for x in line.split('x')]

  f1 = l*w
  f2 = w*h
  f3 = h*l
  sum += 2 * (f1 + f2 + f3) + min(f1, f2, f3)

print(sum)
