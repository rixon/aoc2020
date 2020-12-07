#!/opt/local/bin/python

bp_file="5_input.txt"

def load_file(filename):
  record_list=[]
  bpfile=open(filename, "r")
  for i in bpfile:
    record_list.append(i)
  return record_list

def find_row(bpass):
  bitmap=""
  for i in bpass[0:7]:
#    print(i,)
    if i == "B":
      bitmap+="1"
    elif i == "F":
      bitmap+="0"
    else:
      print ("INVALID SPEC")
  return (int(bitmap, 2))

def find_col(bpass):
  bitmap=""
  for i in bpass[7:10]:
#    print(i,)
    if i == "R":
      bitmap+="1"
    elif i == "L":
      bitmap+="0"
    else:
      print ("INVALID SPEC")
  return (int(bitmap, 2))

def seat_id(row, col):
  return row * 8 + col

def test():
  #    FBFBBFFRLR: row 44, column 5, seat ID 357.
  #    BFFFBBFRRR: row 70, column 7, seat ID 567.
  #    FFFBBBFRRR: row 14, column 7, seat ID 119.
  #    BBFFBBFRLL: row 102, column 4, seat ID 820.
  
  seatmaps=["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
  for seatmap in seatmaps:
    print("seatmap:", seatmap, end=" ")
    row = find_row(seatmap)
    print ("row:", row, end=" ")
    col = find_col(seatmap)
    print ("col:", col, end=" ")
    print ("seat id:", seat_id(row, col))

test()
seatmaps = load_file(bp_file)
highest_seat=0
for i in seatmaps:
  seatnum = int(seat_id(find_row(i), find_col(i)))
  if seatnum > highest_seat:
    highest_seat = seatnum
print (highest_seat)

