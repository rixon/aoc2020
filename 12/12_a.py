#!/opt/local/bin/python

# Checked to see which directions we'll be dealing with in the input with the following:
'''
computer:12 paul$ grep L 12_input.txt | tr -d L | sort | uniq -c
  26 180
   7 270
  62 90
computer:12 paul$ grep R 12_input.txt | tr -d R | sort | uniq -c
  22 180
   5 270
  58 90
'''
# So, we're only dealing with simple NSEW directions, but can turn three steps in each direction.

input_file="12_test.txt"  # 25
input_file="12_input.txt" #
headings = ["N", "E", "S", "W"]
movements = ["N", "E", "S", "W", "F"]
turns = ["L", "R"]
heading = "E"
x = 0
y = 0

def load_instructions(filename):
  myfile = open(filename)
  instructions=[]
  for i in myfile:
    # Going ot try this tuple thing...
    instructions.append((i[0], int(i[1:])))
  return instructions

def interpret_instruction(instruction):
  # Check instruction for heading or movement.  If movement, move.  If heading, update.
  if instruction[0] in turns:
    turn_ship(instruction)
  elif instruction[0] in movements:
    move_ship(instruction)
  else:
    print("Invalid instruction!")

def turn_ship(instruction):
  global heading
  # Steps are always 90 degree increments - we can use this for stepping through our LUT.
  steps = int(instruction[1] / 90)
  
  if instruction[0] == "L":
    # Turn left - subtract heading.
    new_heading = (headings.index(heading) - steps) % 4
  elif instruction[0] == "R":
    # Turn right - add heading.
    new_heading = (headings.index(heading) + steps) % 4
  else:
    print("Invalid heading!")
  heading = headings[new_heading]
  #print("Turned", instruction[0], "to", heading)

def move_ship(instruction):
  global x
  global y
  direction = movements.index(instruction[0])

  amount = instruction[1]
  shift = int(direction / 2 * - 1)
  if instruction[0] == "F":
    # Move forward X amount.
    # To use less code, we'll just translate this to a direction and amount.
    direction = movements.index(heading)
  #else:
  # Now that forward was normalized, the remaining movements should work.
  #print("Moving", direction, amount)
  if direction % 2:
    # left-right.
    if int(direction / 2):
      amount *= -1
    x += amount
    #print("Moving x", amount, "to", x)
  else:
    # up-down
    if int(direction / 2):
      amount *= -1
    y += amount
    #print("Moving y", amount, "to", y)

instlist = load_instructions(input_file)
for i in instlist:
  interpret_instruction(i)

print("Final position:", x, y)
print("Manhattan Distance:", abs(x) + abs(y))

     


