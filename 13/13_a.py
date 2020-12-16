#!/opt/local/bin/python

input_file="13_test.txt"
input_file="13_input.txt"

def load_times(filename):
  myfile = open(filename)
  filecontents = myfile.readlines()
  buslist = []
  start_time = int(filecontents[0])
  for j in filecontents[1].split(","):
    if j != "x":
      buslist.append(int(j))
  return (start_time, buslist)

start_time, buslist = load_times(input_file)
first_for_bus = 0
earliest_list = []

print("Start time:", start_time, "Bus list:", buslist)
for i in buslist:
  first_for_bus = (int(start_time/i)+1)*i
  earliest_list.append((i, first_for_bus))

print (earliest_list)   

etime = start_time * 2
for bus, time in earliest_list:
  if time < etime:
    # Found a new best.  Let's populate this.
    etime = time
    ebus = bus

wait = etime - start_time
print ("Best is bus", ebus, "at", etime, "for a", wait, "minute wait =", ebus * wait)
