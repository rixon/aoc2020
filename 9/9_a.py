#!/opt/local/bin/python
input_filename="9_test.txt"    # Preamble len 5
input_filename="9_input.txt"   # Preamble len 25
preamble_len = 25

def load_input(filename):
  code = []
  myfile = open(filename)

  for i in myfile:
    code.append(int(i.strip()))
  return code

def validate_code(position):
  global array
  global preamble_len
  target = array[position]

  print("Checking if", preamble_len, "digits before", target, "add up.")
  if position < preamble_len:
    return False
  # Walk through position-preamble_len to position-1 and see if the
  # sum of them are equal to position.
  preamble = array[position - preamble_len:position]
  print("Preamble:", preamble)

  for i in preamble:
    if i + i == target:
      # Can't be the same number for both operands.
      continue
    if target - i in preamble:
      print(i, "and", target - i, "are in preamble")
      return True
  return False

array = load_input(input_filename)
print(array)

print(validate_code(6))
for i in range(preamble_len,len(array)):
  if validate_code(i):
    print(i, "ok")
  else:
    print(array[i], " FAILED FAILED FAILED FAILED FAILED FAILED")
    break

