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


  boxdone = [None] * numBoxes
  for i in range(numBoxes):
    boxdone[i] = 0

  realLineNum = 0
  for j in range(len(lines)):
    line = lines[i].strip()

    if re.match('/^\#/', line):
      #print("ignoring a comment line\n")
    elif re.match('~ /\S+/'):

        fields = []
        for word in line.split('/\s+/')
            fields.append(word)
        if len(fields)==5:
            if(fields[0]>0 && fields[0]<=numBoxes):
                if(boxdone[fields[0] - 1] == 0):
                    boxdone[fields[0] - 1] =1
                
                    f = 0
                    for string in fields:
                        current = string.strip()
                        while re.match('~ /<(\d+)>/', current) && match_0> 0 && match_1 <= f:
                            # print "\n"$current matched for $1\n"
                            # current = ~ s/<(\d+)>/$fixed[$realLineNumNum][match_1-1]
                        fixed[realLineNum[f] = current
                        # print ("fixed[realLineNum[f] \t")
                        f++
                print ("\n")
                realLineNum++

                else:
                    print("ignoring an additional line for box %d in the file", fields[0])
            else:
                print("ignoring a line for box %d in the file", fields[0])

        else:
            print("ignoring a line in the file %s that contains something other than 5 columns")
    else:
        print("ignoring a blank line\n")
    j++
return fixed
    
