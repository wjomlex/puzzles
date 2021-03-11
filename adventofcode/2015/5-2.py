import sys

ans = 0

for line in sys.stdin:
  line = line.strip()

  oneAwayRepeat = False
  for i in range(len(line)-2):
    if line[i] == line[i+2]: oneAwayRepeat = True

  twoPairs = False
  pairs = []
  for i in range(len(line)-1):
    pairs += [line[i:i+2]]

  for i in range(len(pairs)):
    for j in range(len(pairs)):
      if j >= i-1: continue
      if pairs[i] == pairs[j]: twoPairs = True

  if oneAwayRepeat and twoPairs: ans += 1

print(ans)
