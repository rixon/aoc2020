#!/opt/local/bin/python
import time
filename="11_test.txt"  # 37.
filename="11_input.txt" # 2222.

floor = "."
empty = "L"
occupied = "#"

crowdlim = 4
iterations = 7

def load_bitmap(filename):
  chairmap=[]
  mask=[]
  # I'm going to cheat and make a no-chair boundary all the way around to make my check-neighbor function easier.
  myfile = open(filename)
  for line in myfile:
    # Load in the bitmap!
    chairmap.append("." + line.strip() + ".")
  linelen = len(chairmap[0])
  chairmap.insert(0, "." * linelen)
  chairmap.append("." * linelen)
  return chairmap

def check_occupied(row, col):
  global waiting_room
  if waiting_room[row][col] == occupied:
    return True
  return False

def check_neighbors(row, col):
  global waiting_room
  crowd = 0
  # Rotate around your position and check if occupied. Return int.
  # Start top left, work clockwise.
  for i in range(row - 1, row + 2):
    for j in range(col -1, col + 2):
      if not (i == row and j == col):
        if check_occupied(i, j):
          crowd += 1
  return crowd

def is_seat(row, col):
  global waiting_room
  if waiting_room[row][col] == floor:
    return False
  return True

def show_seat_count():
  room_count = []
  count = ""
  for i in range(top_end, bottom_end):
    check_row = ""
    for j in range(left_end, right_end):
      if is_seat(i, j):
        count = str(check_neighbors(i, j))
      else:
        count = "."
      check_row += count
    room_count.append(check_row)
  for i in room_count:
    print (i)

  return room_count

def update_seat_map(room):
  global waiting_room
  new_room = []
  count = ""
  global unchanged
  unchanged = 0
  seatcount=0

  for i in range(top_end, bottom_end):
    new_row = ""
    for j in range(left_end, right_end):
      if is_seat(i, j):
        seatcount += 1
        is_occupied = check_occupied(i,j)
        count = check_neighbors(i, j)
        if count >= crowdlim:
          if is_occupied:
            position = empty
          else:
            unchanged += 1
            position = waiting_room[i][j]
        elif (not is_occupied) and count == 0:
          position = occupied 
        else:
          position = waiting_room[i][j]
          unchanged += 1
      else:
        position = floor
      new_row += position
    new_room.append(new_row)
  print(unchanged, "unchanged.", seatcount)
  
  return new_room

def occupancy():
  occupancy = 0
  for i in range(top_end, bottom_end):
    for j in range(left_end, right_end):
      if check_occupied(i, j):
        occupancy += 1
  return occupancy

def max_seats():
  seatcount = 0
  for i in range(top_end, bottom_end):
    for j in range(left_end, right_end):
      if is_seat(i, j):
        seatcount += 1
    print("row", i, seatcount, "seats")
  return seatcount

def show_room():
  global waiting_room
  for i in waiting_room:
    print (i)


# Main

waiting_room = load_bitmap(filename)


left_end = 0
right_end = len(waiting_room[0])
top_end = 0
bottom_end = len(waiting_room)

#print ("Dimensions: Left to right", 0, right_end, "Top to bottom:", 0, bottom_end)
show_room()

#waiting_room = update_seat_map(waiting_room)
#show_room()
#count_map = show_seat_count()

seatcount = max_seats()
unchanged = 1
previous_unchanged = 2
i = 0

while True:
  previous_unchanged = unchanged
  i += 1
  print("Round", i)
  waiting_room = update_seat_map(waiting_room)
  show_room()
  #count_map = show_seat_count()
  print("Checking for", seatcount, "unchanged,", unchanged, "actually unchanged")
  if unchanged == seatcount:
    print("Found!!!!!!!")
    break
  print("Seats occupied:", occupancy())
  #time.sleep(0.5)
  print()

print("After", i, "iterations,", occupancy(), "seats filled.")

