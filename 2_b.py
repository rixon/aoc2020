#!/opt/local/bin/python

myfile = open('2.txt', 'r')
pwlist = []
valid = 0

def check_policy(pw, pwchar, pwcharnum):
  count = 0
  # Break up pwcharnum into first and second fields.
  charfirst = pwpol_first(pwcharnum)
  charsecond = pwpol_second(pwcharnum)
  pwchar = pwchar[0]
  first=False
  second=False

#  print ("Checking ", pw, " for ", pwchar)
  for i in pw:
    if i == pwchar:
      count += 1
#      print (" Found ", pwchar, " - ", count)
  if pw[charfirst - 1] == pwchar: first = True
  if pw[charsecond - 1] == pwchar: second = True
  if (first or second) and not (first and second):
    return True
  else:
    return False
  
def pwpol_first(pol_field):
  # Min is left field.
  val = ""
  for i in pol_field:
    if i == "-":
      return int(val)
    else:
      val += i

def pwpol_second(pol_field):
  # Max is right field.
  val = ""
  firstHalf = True
  for i in pol_field:
    if i != "-" and firstHalf:
      continue
    elif i == "-":
      firstHalf = False
      continue
    val += i
  return int(val)

for line in myfile: 
  #print ("Line: ", line.rstrip())
  # Segment 1: pol_num_allowed
  pol_num_allowed = ""
  # Secment 2: pol_char_applies_to
  pol_char_applies_to = ""
  # Segment 3: password
  password = ""

  # Break into segments
  segment = 0
  for char in line:
    if char == " ":
      # Next field!
      segment += 1
    else:
      if segment == 0:
        pol_num_allowed += char
      elif segment == 1:
        pol_char_applies_to += char
      else:
        password += char
  password.rstrip()   
#  print("Num allowed: ", pol_num_allowed, "  Char: ", pol_char_applies_to, "  PW: ", password)
  #print (line, " --- ", check_policy(password, pol_char_applies_to, pol_num_allowed))
  if check_policy(password, pol_char_applies_to, pol_num_allowed): valid += 1

print ("Valid: ", valid)

