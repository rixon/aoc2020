#!/opt/local/bin/python
filename = "10_input.txt"
step1 = 0
step2 = 0
step3 = 0

def load_adapters(filename):
  adapters=[]
  myfile = open(filename)
  for i in myfile:
    adapters.append(int(i.strip()))
  adapters.sort()
  # Insert the charging outlet, value of 0 jolts
  adapters.insert(0, 0)
  # Add your device, value of device's built in, src +3 jolts.
  adapters.append(adapters[len(adapters)-1]+3)
  return adapters

def walk_adapters(alist):
  global step1
  global step2
  global step3

  for index, value in enumerate(alist):
    if index == 0:
      continue
    diff = value - alist[index - 1]
    if diff == 1:
      step1 += 1
    elif diff == 2:
      step2 += 1
    elif diff == 3:
      step3 += 1
    else:
      print("This should not happen!!!")

adpt_list = load_adapters(filename)

print(adpt_list)

walk_adapters(adpt_list)
print (step1, step2, step3)
print(step1 * step3)

