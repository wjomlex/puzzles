import sys

rawTotal = 0
newTotal = 0
for line in sys.stdin:
  line = line.strip()
  subRaw = len(line)
  subNew = 2 # Always need two quotes

  for i in range(len(line)):
    if line[i] in "\\\"": subNew += 2
    else: subNew += 1

  # print(subRaw, subNew)
  rawTotal += subRaw
  newTotal += subNew

print(newTotal - rawTotal)
