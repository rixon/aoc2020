#!/opt/local/bin/python

infile="8_test.txt"
infile="8_input.txt"
acc = 0  # Accumulator
ip = 0   # Instruction Pointer
used_lines = []

def load_file(filename):
  myfile = open(filename)
  program = []
  for i in myfile:
    # Take the line, and break up into opcode and operand.
    program.append(i.split(" "))
  return program

def process(opcode, operand):
  global acc
  global ip
  global used_lines

  print ("Checking opcode", opcode, "at", ip, end=": ")
  # First, see if our line has been used before.  If so, return false.
  if ip in used_lines:
    print("This line already run.")
    return False
  used_lines.append(ip)
  # Check the opcodes, and perform the related actions.
  if opcode == "nop":
    # Do nothing.
    ip += 1
    print("NOP")
  elif opcode == "acc":
    print("ACC", acc, "+", operand, end=": ")
    acc += operand
    print(acc)
    ip += 1
  elif opcode == "jmp":
    print("JMP", ip, "+", operand, end=": ")
    ip += operand
    print(ip)
  return True

  
prog =  load_file(infile)
print("Loading...")
for i in prog:
  print("Opcode:", i[0], "Operand:", int(i[1]))

print("Processing...")
new_inst = True
while new_inst:
  new_inst = process(prog[ip][0], int(prog[ip][1]))

print ("ip:", ip, "acc:", acc)

