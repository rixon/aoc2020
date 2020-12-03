#!/opt/local/bin/python

f = open('1a.txt', 'r')
l = []

for n in f:
    l.append(int(n))

f.closed

size = len(l)
print("Size: ", size)

''' Iterate through the list of numbers.  Because of the symmetric axiom,
no need to go back and hit all the earlier numbers. '''
index1 = 0
index_max = size
found = False

while index1 < index_max - 2 and found == False:
  index2 = index1 + 1
  while index2 < index_max - 1 and found == False:
    index3 = index2 + 1
    while index3 < index_max and found == False:
#      print ("Trying index 1 (", index1, ") ", l[index1], " / index 2 (", index2, ") ", l[index2], " / index 3 (", index3, ") ",l[index3])
      if l[index1] + l[index2] + l[index3] == 2020:
        found = True
        print ("FOUND! ", l[index1], " + ", l[index2], " + ", l[index3], " = 2020")
        break
      index3 += 1
    if found: break
    index2 += 1
  if found: break
  index1 += 1

print ("Product: ", l[index1] * l[index2] * l[index3])

