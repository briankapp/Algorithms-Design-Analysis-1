#!/usr/bin/python

import sys

numnodes = int(sys.argv[1])
outfname = "example" + sys.argv[1] + ".txt"
outfile  = open(outfname,"w")
bigfile  = open("SCC.txt")

for line in bigfile:
  parts = line.split()
  n1 = int(parts[0])
  n2 = int(parts[1])
  if n1 <= numnodes and n2 <= numnodes:
    outfile.write(line)
