import hashlib

input = 'yzbqklnj'
suffix = 1

while True:
  s = input + str(suffix)
  hash_prefix = hashlib.md5(s.encode('utf-8')).hexdigest()[:6]
  print(hash_prefix)

  if hash_prefix == '000000':
    print()
    print("Answer: ", suffix)
    break

  suffix += 1
