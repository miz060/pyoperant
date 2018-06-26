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
    elif re.match('~ /\S+/')
