#!/opt/local/bin/python

numlist = [0, 3, 6] # 2020
numlist = [1, 3, 2] # 2020
numlist = [2, 1, 3] # 2020
numlist = [1, 2, 3] # 2020
numlist = [2, 3, 1] # 2020
numlist = [3, 2, 1] # 2020
numlist = [3, 1, 2] # 2020
numlist = [14, 8, 16, 0, 1, 17] # ?
steps = 2020
steps = 30000000
count={}
last_spoken=0
turn = 0

def speak_number():
  # If turn < len(numlist):
    # Speak one from the numlist.
  # Else speak using last_spoken.
    # speak = (turn[last_spoken] - turn_before[last_spoken])
      # If first time spoken, then 0.
  # Update the count for number.
  # Update last_spoken. prior last_spoken down one on the stack.
  global turn
  global last_spoken
  #print("Turn:", turn, end="  ")
  if turn < len(numlist):
    last_spoken = numlist[turn]
  else:
    last_spoken = get_count(last_spoken)
  update_count(last_spoken)
  turn += 1
  #print(last_spoken)

def get_count(number):
  if number in count:
    if len(count[number]) > 1:
      return count[number][0] - count[number][1]
    else:
      return 0
  else:
    return 0

def update_count(number):
  global count
  if number in count:
    if len(count[number]) > 1:
      count[number][1] = count[number][0]
      count[number][0] = turn
    else:
      count[number].append(count[number][0])
      count[number][0] = turn
  else:
    count[number] = []
    count[number].append(turn)

for i in range(steps):
  speak_number()
print(last_spoken)
