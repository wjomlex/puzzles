import sys

sum = 0

for line in sys.stdin:
  line = line.strip()

  l, w, h = [int(x) for x in line.split('x')]

  p1 = l+w
  p2 = w+h
  p3 = h+l
  sum += 2 * min(p1, p2, p3) + l*w*h

print(sum)
