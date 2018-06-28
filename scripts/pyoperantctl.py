# a line to line python translation of the pyoperant script
# still in progress
# by Mingcheng Zhu, miz060
import re
import subprocess
numBoxes = 16

opdatdir = "/home/bird/opdat"
filename = "${opdatdir}panel_subject_behavior"

# this code parses a file as described in panel_subject_behavior

# trim function is defined in python as strip()

def readfile(filename_in, numBoxes_in):
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
      print("ignoring a comment line\n")
    elif re.search(r"\S+", line):
      fields = re.compile(r"\s+").rsplit(line, 5)
      if len(fields)== 5:
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
              fixed[realLineNum][f] = current
              # print ("fixed[realLineNum[f] \t")
              f += 1
            #print ("\n")
            realLineNum += 1

          else:
            print("ignoring an additional line for box %d in the file %s\n", fields[0], filename)
        else:
          print("ignoring a line for box %d in the file %s because it is less than 0 or bigger than %d \n"\
            , fields[0], filename, numBoxes)
      else:
        print("ignoring a line in the file %s that contains something other than 5 columns")
    else:
      print("ignoring a blank line\n")
    j += 1
  return fixed


# for now, write sub checkoptions(@) as the main function
def main(): 
  data = readfile(filename, numBoxes)
  #here you should list the programs that may be run
  #this program will kill these processes if they are running for a box if the file above has a line for that box that doesn't match
  psnames = ["behave"]

  #psname = "|".join(psnames)
  # limit the program name to be behave for now
  processes = subprocess.check_output("ps waux | egrep 'behave'", shell=True)
  
  #pass a string containing s as argument 1 to activate starting
  shouldStartProcesses = 0
  #pass a string containing k as argument 1 to activate killing
  shouldKillProcesses = 0
  #pass a string containing d as argument 1 to kill all (needs k to actually work)
  shouldKillAll = 0

  if(argc >= 0):
    print("argv[0] is the first argument")
    if re.search(r"k", argv[0]):
      print("activating killing\n")
      shouldKillProcesses = 1
    else: 
      print("killing inactive.  pass a command line argument containing 'k' to activate.\n")
    if re.search(r"s", argv[0]):
      print("activating starting\n")
      shouldStartProcesses = 1
    else:
      print("starting inactive. pass a command line argument containing 's' to activate.\n")
    if re.search(r"d", argv[0]):
       print("killing all.\n")
       shouldKillAll = 1;
       if not shouldKillProcesses:
         print("you need to also pass 'k' in order for killing all to actually kill.\n")
       else:
         print("pass a command line argument containing 'd' to bring down all processes.\n")
    else:
      print("starting and killing inactive.  pass a command line argument containing 's' and/or 'k', respectively, to activate.\n")
      print("pass a command line argument containing 'd' to bring down all processes.\n")

  killstring = ''
  if argc >= 1:
    killstring = argv[1]
    print("kill string is $killstring\n")
  else:
    killstring = ''
    print("a second argument would have been added to the logfiles when processes are killed (ie a reason for killing the process)\n")

  print("\n");

  i=0
  while len(processes)>0:
    ps = process.pop()
    info = re.compile(" ").rsplit(ps, 11)
    #chop($info[10]);
    #$info[10] =~ s/^(.*\/python .*\/bin\/)//;
    #$info[10] =~ s/^(\/usr\/local\/anaconda\/bin\/python \/usr\/local\/anaconda\/bin\/)//;
    #$info[10] =~ s/^(\/usr\/local\/anaconda\/bin\/python \/usr\/local\/anaconda\/bin\/)//;
    print("s\n", info[10])
    if re.search("behave", info[10]):
        pspieces = info[10].split(" ")
        j = 0 
	while len(pspieces) > j:
	  #if $pspieces[$j] eq "-P":
            #$boxNum = $pspieces[1 + $j]
          #elif $pspieces[$j] eq "-S":
	    #$birdID = $pspieces[1 + $j]
	  j+=1
	indProcesses[i] = info[10]
	indBoxes[i] = boxNum
	indBirdIDs[i] = birdID
	indIDs[i] = info[1]
	indStatuses[i] = info[7]
	i+=1

  i=0
  while numBoxes > i:
    boxCorrect[i] = -1
    correctProgram[i] = ""
    directory[i] = ""
    birdid[i] = 0
    i+=1

