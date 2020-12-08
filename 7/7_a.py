#!/opt/local/bin/python

filename = "7_test.txt"
filename = "7_input.txt"
rulelist=[]
goalbag = "shiny_gold"

def loadfile(filename):
  rulelist={}
  rule={}
  rulestage=1
  rulename=""
  rulecount=0
  rulepart=""
  infile = open(filename, "r")
  for line in infile:
    # Parse each line.  format is:
    # multiword descr BAGS CONTAINS N multiword descri BAG[S](.|[,N multiword descr BAG[S]])
    # We don't need to be that complex.  Split line into word list. Words 1-2 are always the description (key), etc:
    #  1-2: description (key)
    #  3-4: ignore (bags contain)
    #  5: count of bags of type
    #  6-7: bag type (strip , or .)
    #  8: bag or bags and trailing , or .
    #  Optional:
    #  9,13,17...: count of bags of type
    #  10-11,14-15,18-19...: bag type (strip , or .)
    #  12,16,20...: bag or bags and trailing , or .
    linelist = line.split(" ")

    subruleindex=4
    subruleincr=4
    linelen = len(linelist)
    #subrulelist=[]
    subrulelist={}

    #print(linelist)
    rulename = linelist[0] + "_" + linelist[1]
    while subruleindex < linelen - 2:
      if linelist[subruleindex] != "no":
        #print(subruleindex, linelen, len(linelist))
        rulecount = int(linelist[subruleindex])
        subrule = linelist[subruleindex+ 1] + "_" + linelist[subruleindex + 2]
        #subrulelist.append({subrule: rulecount})
        subrulelist[subrule]=rulecount
      else:
        rulecount = 0
        subrule = "other_bags"
        #subrulelist.append({subrule: rulecount})
        subrulelist[subrule]=rulecount
      subruleindex += subruleincr
    rulelist[rulename] = subrulelist
  return rulelist

def check_can_carry(bag, depth):
  # Check if bag can carry target.
  if bag == "other_bags":
    return False
  bagrules = rulelist[bag]
  print(" " * depth, "Checking", bag, "with rules", bagrules)

  if any(goalbag in l for l in bagrules):
    return True
  else:
    #print(" " * depth, " not found, walking")
    for sub_bag_name in rulelist[bag]:
      #print(" " * depth, "  sub_bag_name", sub_bag_name)
      #print(" " * depth, "   from rulelist", rulelist)
      #sub_bag = rulelist[sub_bag_name]
      if check_can_carry(sub_bag_name, depth + 1):
        return True
    return False

rulelist = loadfile(filename)
print()
print(rulelist)
bagcount=0
for r in rulelist:
  print ("Checking", r, "for", goalbag)
  if check_can_carry(r, 1):
  #if any(goalbag in rs for rs in r[1]):
    print("                                                  FOUND!")
    bagcount += 1
  else:
    print("Not found.")
print (bagcount)


