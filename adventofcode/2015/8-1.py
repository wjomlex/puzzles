import sys

rawTotal = 0
newTotal = 0
for line in sys.stdin:
  line = line.strip()
  subRaw = len(line)
  subNew = 0

  escaping = False
  i = 1

  while i < len(line) - 1:
    if not escaping and line[i] != "\\": 
      subNew += 1
    elif not escaping and line[i] == "\\": 
      escaping = True
    elif escaping and line[i] == "x":
      subNew += 1
      i += 2
      escaping = False
    else:
      subNew += 1
      escaping = False

    i += 1

  # print(subRaw, subNew)
  rawTotal += subRaw
  newTotal += subNew

print(rawTotal - newTotal)
