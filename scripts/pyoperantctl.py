# a line to line python translation of the pyoperant script
# still in progress
# by Mingcheng Zhu, miz060
import re
import subprocess
import datetime
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
    info[10] = info[10][:-1]
    #info[10].replace(r"^(.*\/python", ".*\/bin\/)"
    current.replace(r"<(\d+)>", fixed[realLineNum][re.findall(r"<(\d+)>", current[0])-1])
    #$info[10] =~ s/^(\/usr\/local\/anaconda\/bin\/python \/usr\/local\/anaconda\/bin\/)//;
    #$info[10] =~ s/^(\/usr\/local\/anaconda\/bin\/python \/usr\/local\/anaconda\/bin\/)//;
    print("s\n", info[10])
    if re.search("behave", info[10]):
        pspieces = info[10].split(" ")
        j = 0 
	while len(pspieces) > j:
	  if pspieces[j] == "-P":
            boxNum = pspieces[1 + j]
          elif pspieces[j] == "-S":
	    birdID = pspieces[1 + j]
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

  currentDT = datetime.datetime.now()
  print(str(currentDT))

  for i in range(len(data)):
    fields[i] = data[i]
   
    if fields[1] != '1':
      print("box %d disabled\n", fields[0])

    boxCorrect[fields[0] -1] = 0
    if shouldKillAll | fields[1] != '1':
      correctProgram[fields[0] - 1] = "NONE"
    else: 
      correctProgram[fields[0] - 1] = fields[4]
    directory[fields[0] -1] = fields[3]
    birdid[fields[0] - 1] = fields[2]

    i=0
    while len(indProcesses)>i:
      if indBoxes[i]==fields[0]:
        #if($indProcesses[$i] eq $fields[3]){
	  if checkoptions(indProcesses[i], correctProgram[fields[0] - 1]):
            if indStatuses[i] == "SL" | indStatuses[i] == "RL":
	      if boxCorrect[fields[0] - 1]== 0:
                print("box %d correctly running %d\n", fields[0], indProcesses[i])
                boxCorrect[fields[0] - 1]= 1;
	      else:
                print("box %d INCORRECTLY running duplicate copy of %d you should kill one of them\n", fields[0], indProcesses[i])
	    elif (indStatuses[i] == "Ss"):
              print("box %d found running session leader process %d\n", fields[0], indIDs[i])
	    else:
              print("box %d running correct process %d but with status %d you should investigate %d\n", \
                fields[0], indProcesses[i], indStatuses[i], indIDs[i])
	      boxCorrect[fields[0] - 1]=1
          else:
            if indStatuses[i] == "Ss":
              print("box %d running session leader process %d\n", fields[0], indIDs[i])
	    else:
              print("box %d INCORRECTLY running %d should kill %d\n", fields[0], indProcesses[i], indIDs[i])
              killID = indBirdIDs[i]
              #killLog = opdatdir."B".$killID."/B".$killID."_log.txt";
              print("log directory is killLog\n")
              if shouldKillProcesses:
                print("attempting to kill $indProcesses[$i] ($indIDs[$i])\n")
                #system "kill $indIDs[$i]";
                #system "cd $directory[$i]; echo '".$date.": ".$killstring." killing $indProcesses[$i]' >> $opdatdir"."B".$birdid[$i]."/B".$birdid[$i]."_log.txt";
                #system "echo '".$date.": killing $indProcesses[$i] :: $killstring' >> $killLog"
    i += 1

  i=0;
  while i < numBoxes:
    if boxCorrect[i]==0:
      if correctProgram[i] == "NONE":
        print("box %d correctly running no program (assuming processes suggested above were killed)\n", i+1)
      else:
        print("box %d needs to start %s in directory %s\n", \
          i+1, correctProgram[i], directory[i])
	    
        if shouldStartProcesses:
          print("attempting to start %s in %s\n", correctProgram[i], directory[i])
          #system "cd $directory[$i]; echo '".$date.": starting $correctProgram[$i]' >> $opdatdir"."B".$birdid[$i]."/B".$birdid[$i]."_log.txt; $correctProgram[$i] &";
    elif boxCorrect[i] == -1:
      print("box %d has no line in file %s\n", i+1, filename)
    elif boxCorrect[i] == 1:
      print("box %d needs no change\n", i+1)
    else:
      print("box %d had some problem that should never happen\n", i+1)
  i += 1


#sub checkoptions(@) {
#	($s1,$s2)=@_;
#
#	$s1=trim($s1);
#	$s2=trim($s2);
#	if($s1=~s/^(\S*)// && $s2=~s/^$1//){
#		$s1=trim($s1);
#		$s2=trim($s2);
#		if($s1=~s/(\S*)$// && $s2=~s/$1$//){
#			$s1=trim($s1);
#			$s2=trim($s2);
#			@s1=split("-",$s1);
#			@s2=split("-",$s2);
#			#print "'".$s1."'"."\t"."'".$s2."'"."\n";
#			@redo=@s2;
#			foreach $o(@s1){
#				@s2=@redo;
#				$o=trim($o);
#				$match=0;
#				$n=0;
#				@redo=();
#				foreach $m(@s2){
#					$m=trim($m);
#					#print "'".$m."'"."\t"."'".$o."'"."\n";
#					if($m=~/^(\S*)\s*(\S*)$/ && $o=~/^$1\s*$2$/){
#						$match=1;
#					} else {
#						$redo[$n]=$m;
#						$n++;
#					}
#				}
#				if($match){
#				} else {
#					#print "no match for option\n";
#					return 0;
#				}
#			}
#			if(scalar(@redo)==0){
#				#success!
#				return 1;
#			} else {
#				#print "leftover options\n";
#				return 0;
#			}
#		} else {
#			#print "not same stimfile\n";
#			return 0;
#		}
#	} else {
#		#print "not same program\n";
#		return 0;
#	}
#}
