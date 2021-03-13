import sys

h = {}
for i in range(1000):
  for j in range(1000):
    h[(i, j)] = 0

for line in sys.stdin:
  line = line.strip()
  tokens = line.split()
  op = None
  r1 = c1 = r2 = c2 = 0
  if tokens[0] == 'toggle':
    op = 'toggle'
    r1, c1 = [int(x) for x in tokens[1].split(',')]
    r2, c2 = [int(x) for x in tokens[3].split(',')]
  else:
    op = tokens[1]
    r1, c1 = [int(x) for x in tokens[2].split(',')]
    r2, c2 = [int(x) for x in tokens[4].split(',')]
    
  for r in range(min(r1,r2), max(r1,r2)+1):
    for c in range(min(c1,c2), max(c1,c2)+1):
      if op == 'toggle': h[(r, c)] += 2
      if op == 'on': h[(r, c)] += 1
      if op == 'off': h[(r, c)] = max(0, h[(r, c)] - 1)
    


ans = 0
for i in range(1000):
  for j in range(1000):
    ans += h[(i, j)]

print(ans)

