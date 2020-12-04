#!/opt/local/bin/python

batch_file='4_batch.txt'
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
  for i in fields:
    field_hash[i] = False
  for i in record:
    field_hash[i] = True
  print (field_hash)
  for i in field_hash:
    # Now we look through for any False.
    if field_hash[i] == False:
      if i == optional:
        # Doesn't matter for optional vars.
        continue
      print ("returning false")
      return False
  print ("RETURNING TRUE")
  return True



# Main program
fields = loadfields(field_file)  
batch = loadbatch(batch_file)
# Now we have parsed data.

#print ("There are", len(fields), "fields:", fields)
#print
#print ("There are", len(batch), "records in batch: ", batch)

valid=0
invalid=0

for record in batch:
  if check_record(record) == True:
    valid += 1
  else:
    invalid += 1
print(valid, "records valid;", invalid, "records invalid.")
