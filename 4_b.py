#!/opt/local/bin/python

import re

batch_file='4_batch.txt'
#batch_file="4_test_invalid.txt"
field_file='4_fields.txt'
optional="cid"

def loadfields(filename):
  # Read field definition file
  # Field definitions are as follows:
  #tla (Description Field)
  # All we want is the first three chars.
  myfile = open(filename, 'r')
  fields = []

  for line in myfile: 
    #print ("Line: ", line.rstrip()) 
    fields.append(line[0:3])

  return fields

def loadbatch(filename):
  # Read passport batch file
  # Field definitions are as follows:
  #fld:any_data[ fld:more_data]
  #[fld:optional_addtl_lines]
  #
  # The blank line is the record separator.  Can me multiple fields per line.
  myfile = open(filename, 'r')
  records = [{}]
  fields = {}
  current_record=0
  current_field=0

  # Do it in two passes? First, get a set of fields in a line.  Then break each into a dict.
  # Or one pass - go until blank line

  for line in myfile: 
    if line == "\n":
      # Blank line - end of record!
      #print ("Blank line found - starting new record.")
      eor = True
      current_record += 1
      records.append({})
      continue
    else:
      # Line has data - process and add to current record.
      #print ("Adding line ", line, "to record", current_record)
      #records[current_record] += line.rstrip()
      records[current_record].update(parserecords(line))

  return records

def parserecords(line):
  # Take a string that was read from a file, and return a dict.
  rec_name=""
  rec_data=""
  name_or_data=0
  tempdict={}

  # Format of each field is xxx:yyyyyy...
  field_list = line.split(" ")
  for field in field_list:
    rec_name, rec_data = field.split(":")
    tempdict[rec_name] = rec_data.rstrip()

  return tempdict

def check_record(record):
  # Let's create a dict of fieldtypes.  We'll walk through the record, and mark each
  # fieldtype when found.  After, we'll look for any not set and return true if all
  # required are found, false if not.
  field_hash = {}  
  # Start by creating each possible field, then setting it False.
  #print(" record:", record)
  for i in fields:
    field_hash[i] = False
    #print("Added fields:", field_hash)
  # Now we go through and set True any which are in our record.
  for field_key in record:
    #print("checking field_key:", field_key)
    field_data = record[field_key]
    #print("checking field_record:", field_data)

    field_hash[field_key] = validate_field(field_key, field_data)
    #print("Added records:", field_hash)
  #print (field_hash)
  for i in field_hash:
    # Now we look through for any False.
    if field_hash[i] == False:
      if i == optional:
        # Doesn't matter for optional vars.
        continue
      print (field_hash)
      print ("RETURNING FALSE")
      return False
  #print ("returning true")
  return True

def validate_field(field_key, field_value):
  # Validate the field.  Check against a rule for each field; if it checks out
  # then return True, otherwise return False.

  # Validation rules:
  # 
  #  byr (Birth Year) - four digits; at least 1920 and at most 2002.
  #  iyr (Issue Year) - four digits; at least 2010 and at most 2020.
  #  eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
  #  hgt (Height) - a number followed by either cm or in:
  #      If cm, the number must be at least 150 and at most 193.
  #      If in, the number must be at least 59 and at most 76.
  #  hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
  #  ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
  #  pid (Passport ID) - a nine-digit number, including leading zeroes.
  #  cid (Country ID) - ignored, missing or not.


  #field_key = list(field.keys())[0] 
  #field_value = list(field.values())[0] 
  #print ("Validating key, value:", field_key, field_value)
  if field_key == fields[0]:
    # byr - >= 1920 <= 2002
    if int(field_value) >= 1920 and int(field_value) <= 2002:
      return True
    print ("byr 1920-2002 fail:", field_value)
    return False
  elif field_key == fields[1]:
    # iyr - 2010<2020 
    if int(field_value) >= 2010 and int(field_value) <= 2020:
      return True
    print ("iyr 2010-2020 fail:", field_value)
    return False
  elif field_key == fields[2]:
    # eyr - 2020<2030
    if int(field_value) >= 2020 and int(field_value) <= 2030:
      return True
    print ("eyr 2020-2030 fail:", field_value)
    return False
  elif field_key == fields[3]:
    # hgt - 150<193 cm OR 59<76 in
    (hval, htype) = splithgt(field_value)
    if htype == "cm":
      if int(hval) >= 150 and int(hval) <= 193:
        return True
    elif htype == "in":
      if int(hval) >= 59 and int(hval) <= 76:
        return True
    print ("hgt NNNin fail:", field_value)
    return False
  elif field_key == fields[4]:
    # hcl - #xxxxxx
    if re.search(r'^#(?:[0-9a-fA-F]{6}){1}$', field_value):
      return True
    print ("hcl #xxxxxx fail:", field_value)
    return False
  elif field_key == fields[5]:
    # ecl - vvv those vvv
    # This is a terrible hack - index 0 willmade the following statement False, so fill
    # index 0 with any invalid value.
    ecl = ["x", "amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    try:
      if ecl.index(field_value):
        return True
    except:
      print ("ecl (color abbrev) fail:", field_value)
      return False
    print ("ecl (color abbrev) fail:", field_value)
    return False
  elif field_key == fields[6]:
    # pid - 9 dig num
    if re.search(r'^(?:[0-9]{9}){1}$', field_value):
      return True
    print ("pid NNNNNNNNN fail:", field_value)
    return False
  elif field_key == fields[7]:
    # cid - ignored
    return True
  else:
    print ("INVALID FIELD!!!")
  
def splithgt(raw):
  # This is a hack - instead of returning None, return an out-of-range value to let things work.
  #return (''.join(filter(str.isdigit, raw)) or None, ''.join(filter(str.isalpha, raw)) or None)
  return (''.join(filter(str.isdigit, raw)) or "999", ''.join(filter(str.isalpha, raw)) or "xx")

# Main program
#fields = loadfields(field_file)  
# I'm just going to manually define them, and the rules for each.
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

batch = loadbatch(batch_file)
# Now we have parsed data.

valid=0
invalid=0

for record in batch:
  if check_record(record) == True:
    valid += 1
  else:
    invalid += 1
print(valid, "records valid;", invalid, "records invalid.")
