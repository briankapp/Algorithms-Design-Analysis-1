#!/usr/bin/python

import random
import sys

numItems = int(sys.argv[1])
items    = range(0,numItems)
random.shuffle(items)
print items

count = 0
for i in range(0,numItems):
  for j in range (i+1, numItems):
    if items[i] > items[j]:
      count += 1

print count
