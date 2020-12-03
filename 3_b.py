#!/opt/local/bin/python

filename='3.txt'
pwlist = []
valid = 0
slope = [3, 1]

def loadfile(filename):
  # Read a file, making a list of rows.
  myfile = open(filename, 'r')
  hill = []

  for line in myfile: 
    #print ("Line: ", line.rstrip()) 
    hill.append(line.rstrip())

  return hill

def toboggan_down(hill):
  over = slope[0]
  down = slope[1]
  current_row = 0
  current_column = 0
  numrows = len(hill)
  linelen = len(hill[0])
  hit_count = 0

  print ("We are going to go over", over, "and down", down)
  print ("Total rows are", numrows, "and the lines are only", linelen, "long.")
  
  while current_row < numrows:
    # We start with a position to check, and will update it after moving/checking.
    #print ("Trying hill[", current_row, "][", current_column, "]")
    current_object = hill[current_row][current_column]
    # Check if the object is a tree or not; increment if it is.
    if current_object == "#":
      hit_count += 1
    
    # Then update our position and go on to the next. Remember the max column width.
    current_row += down
    current_column += over
    current_column %= linelen

  return (hit_count)

# Main program
hill = loadfile(filename)  

slope = [1, 1]
treecount1 = toboggan_down(hill)
print ("You hit", treecount1, "trees going down the hill. Ouch!")

slope = [3, 1]
treecount2 = toboggan_down(hill)
print ("You hit", treecount2, "trees going down the hill. Ouch!")
slope = [5, 1]
treecount3 = toboggan_down(hill)
print ("You hit", treecount3, "trees going down the hill. Ouch!")
slope = [7, 1]
treecount4 = toboggan_down(hill)
print ("You hit", treecount4, "trees going down the hill. Ouch!")
slope = [1, 2]
treecount5 = toboggan_down(hill)
print ("You hit", treecount5, "trees going down the hill. Ouch!")
print (treecount1 * treecount2 * treecount3 * treecount4 * treecount5)

