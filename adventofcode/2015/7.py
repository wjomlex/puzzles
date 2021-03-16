import sys

needValue = set()
inputs = {}
value = {}

for line in sys.stdin:
  tokens = line.split()
  if tokens[0] == 'NOT':
    operator = 'NOT'
    target = tokens[3]
    operand = tokens[1]

    try: operand = int(operand)
    except: pass

    inputs[target] = (operator, operand, None)
    needValue.add(target)
  elif len(tokens) > 3:
    operator = tokens[1]
    target = tokens[4]
    operand1 = tokens[0]
    operand2 = tokens[2]

    try: operand1 = int(operand1)
    except: pass
    try: operand2 = int(operand2)
    except: pass

    inputs[target] = (operator, operand1, operand2)
    needValue.add(target)
  else:
    try:
      value[tokens[2]] = int(tokens[0])
    except:
      inputs[tokens[2]] = ("EQUAL", tokens[0], None)
      needValue.add(tokens[2])

# Find a target that needs a value
while len(needValue) > 0:
  for target in needValue:
    operator, operand1, operand2 = inputs[target]
    if not isinstance(operand1, int) and operand1 not in value:
      continue
    if operand2 is not None and not isinstance(operand2, int) and operand2 not in value:
      continue

    print("GONNA DO", operator, operand1, operand2)
    if operand1 in value:
      operand1 = value[operand1]
    if operand2 in value:
      operand2 = value[operand2]
    print("GONNA REALLY DO", operator, operand1, operand2)

    if operator == "NOT":
      value[target] = operand1 ^ 65535
    elif operator == "OR":
      value[target] = operand1 | operand2
    elif operator == "AND":
      value[target] = operand1 & operand2
    elif operator == "LSHIFT":
      value[target] = (operand1 << operand2) % 65536
    elif operator == "RSHIFT":
      value[target] = operand1 >> operand2
    elif operator == "EQUAL":
      value[target] = operand1

    needValue.remove(target)
    print("DID", target)
    print(value)
    break

  #print ("NOTHING?")




print(value['a'])
