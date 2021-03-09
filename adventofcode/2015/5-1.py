import sys

ans = 0

for line in sys.stdin:
  line = line.strip()

  vowels = 0
  doubles = False
  badness = False

  for i in range(len(line)):
    if line[i] in 'aeiou': vowels += 1
    if i < len(line) - 1:
      if line[i] == line[i+1]: doubles = True
      if line[i:i+2] in 'ab|cd|pq|xy': badness = True

  if vowels >= 3 and doubles and not badness: ans += 1

print(ans)
