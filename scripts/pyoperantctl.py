# a line to line python translation of the pyoperant script
# still in progress
# by Mingcheng Zhu, miz060
import re

numBoxes = 16

opdatdir = "/home/bird/opdat"
filename = "${opdatdir}panel_subject_behavior"

# this code parses a file as described in panel_subject_behavior

# trim function is defined in python as strip()

def readfile(filename_in, numBoxes_in){
  filename = filename_in
  numBoxes = numBoxes_in

  lines = []
  with open (filename) as f:
    strings = f.read()
    for line in strings.split('\n'):
      lines.append(line)

  # python cannot create in the fly; therefore needs to declare the return value earlier
  fixed = [[0 for x in range(5)] for y in range(lines)]

  boxdone = [None] * numBoxes
  for i in range(numBoxes):
    boxdone[i] = 0

  realLineNum = 0
  for j in range(len(lines)):
    line = lines[j].strip()

    if re.match(r"^\#", line):
      #print("ignoring a comment line\n")
    elif re.search(r"\S+", line):
      fields = re.compile(r"\s+").rsplit(line, 5)
        if len(fields)==5:
          if(fields[0]>0 and fields[0]<=numBoxes):
            if(boxdone[fields[0] - 1] == 0):
              boxdone[fields[0] - 1] = 1
                
              f = 0
              for str in fields:
                
                current = str.strip()
                while re.search(r"<(\d+)>", current) \
                  and re.findall(r"<(\d+)>", current)[0] > 0 \
                  and re.findall(r"<(\d+)>", current)[0] <= f:
                  # print ("\n $s matched for $d\n", current, re.findall(r"<(\d+)>",current))
                  # current = ~ s/<(\d+)>/$fixed[$realLineNumNum][match_1-1]
                  current.replace(r"<(\d+)>", fixed[realLineNum][re.findall(r"<(\d+)>", current[0])-1])
                fixed[realLineNum[f] = current
                # print ("fixed[realLineNum[f] \t")
                f += 1
              print ("\n")
              realLineNum += 1

            else:
              print("ignoring an additional line for box %d in the file %s\n", fields[0], filename)
          else:
            print("ignoring a line for box %d in the file %s", fields[0], filename)
        else:
          print("ignoring a line for box %d in the file %s because it is less than 0 or bigger than %d \n"\
           , fields[0], filename, numBoxes)
      else:
        print("ignoring a line in the file %s that contains something other than 5 columns")
    else:
      print("ignoring a blank line\n")
    j += 1
  return fixed
    
