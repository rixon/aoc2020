#!/opt/local/bin/python
rule_file = "16_test.rules"
near_file = "16_test.nearby"
rule_file = "16_input.rules"
near_file = "16_input.nearby"

your_ticket=[7,1,14]
your_ticket=[73,101,67,97,149,53,89,113,79,131,71,127,137,61,139,103,83,107,109,59]

rules = {}     # Dict of rules: {"rulename": [[start1, end1], [start2, end2]]
tickets = []   # List of ints

def load_data():
  global rules
  global tickets
  for line in open(rule_file):
    rulename, ruleline = line.split(":")
    #first, second = ruleline.split(" or ")
    #first = [int(x) for x in first.split("-")]
    #rules[rulename] = y.split(" or ")
    rule_ranges = [j.split("-") for j in ruleline.split(" or ")]
    # Okay, this feels hackey.  Should be a way to incoroporate those int() into the above!
    for index, r in enumerate(rule_ranges):
      rule_ranges[index][0] = int(r[0])
      rule_ranges[index][1] = int(r[1])
    rules[rulename] = rule_ranges

  for j in open(near_file):
    tickets.append([int(k) for k in j.split(",")])
  print (rules)
  print (tickets)

def check_ticket(ticket):
  err = 0
  for entry in ticket:
    err += check_entry(entry)
  return err
    
def check_entry(entry):
  for rule in rules:
    #print("Checking if", entry, "is in", rule)
    r = rules[rule]
    if (entry >= r[0][0] and entry <= r[0][1]) \
      or (entry >= r[1][0] and entry <= r[1][1]):
      #print("OK")
      return 0
  return entry

load_data()
total = 0
for ticket in tickets:
  total += check_ticket(ticket)
print("Total:", total)
