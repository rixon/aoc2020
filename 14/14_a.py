#!/opt/local/bin/python

'''
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
'''

input_file="14_test.txt" # 165
memsize = 10
input_file="14_input.txt" # 18630548206046
memsize = 100000

# zeromask is a bitmap of 0s set. All 1s except where 0s are, so we can AND.
zeromask=0b0
# onemask is a bitmap of 1s set. All 0s except where 1s are, so we can OR.
onemask=0b0

memory=[]

def load_data(filename):
  with open(filename) as f:
    instr_list = f.read().splitlines()
  instr_list = [tuple(x.split(" = ")) for x in instr_list]
  return instr_list

def interpret_line(instr, operand):
  if instr == "mask":
    load_mask(operand)
    return
  memloc = int(instr[4:len(instr)-1])
  wrmem(memloc, operand)

def load_mask(maskdef):
  # Create two masks - a 1s mask and a 0s mask.
  global zeromask
  global onemask
  zeromask = 0
  onemask = 0
  for i in maskdef:
    zeromask <<= 1
    onemask <<= 1
    if i == "0":
      # Although these effectively do nothing, this is to remember what we're doing.
      zeromask |= 0b0
      onemask |= 0b0
    elif i == "1":
      zeromask |= 0b1
      onemask |= 0b1
    elif i == "X":
      zeromask |= 0b1
      onemask |= 0b0
    else:
      print("Invalid mask found!")
  print("Input:", maskdef)
  print("Zero :", bin(zeromask))
  print("One  :", bin(onemask))

def wrmem(loc, num):
  num = int(num)
  num &= zeromask
  num |= onemask
  memory[loc] = num
  print("write", num, "at", loc)

def init_mem(size):
  for i in range(size):
    memory.append(0)


instr = load_data(input_file)
init_mem(memsize)

for i in instr:
  #print(i)
  interpret_line(*i)
  
total = 0
for i in memory:
  total += i
print ("Total:", total)

