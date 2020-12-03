#!/opt/local/bin/python

f = open('1a.txt', 'r')
l = []

for n in f:
    l.append(int(n))

f.closed

size = len(l)
print("Size: ", size)

for i in l:
  print ("Working with ", i)
  j = 2020 - i
  print ("Looking for ", j)
  try:
    loc = l.index(j)
  except:
    print ("Not found.")
    next
  else:
    print ("FOUND! ", j, " is at ", loc)
    val_a = i
    val_b = j

print ()
print ("Product of ", val_a, " and ", val_b, " is ", val_a * val_b)


