#!/opt/local/bin/python

filename="6_input.txt"

def load_file(filename):
  records = []
  srcfile = open(filename, "r")
  for i in srcfile:
    records.append(i)
  return records

def parse_groups(records):
  group_list = []
  group = []
  index = 0
  for r in records:
    if r == "\n":
      index += 1
      group_list.append(group)
      group = []
    else:
      group.append(r.rstrip())
  group_list.append(group)
  return group_list

def unique_ans_list(responses):
  ans_list={}
  for resp in responses:
    for letter in resp:
      ans_list[letter] = True
  return ans_list


inputfile = load_file(filename)
collated_answers = parse_groups(inputfile)
ans_cnt=0
for grp_ans in collated_answers:
  ans_list = unique_ans_list(grp_ans)
  ans_cnt += len(ans_list)

print (ans_cnt)
