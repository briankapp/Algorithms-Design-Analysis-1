#!/usr/bin/python
import sys
import random

def countInversionsDumbWay(items):
  numItems = len(items)
  count = 0
  for i in range(0,numItems):
    #if (i % 1000 == 0):
    #  print i
    for j in range (i+1, numItems):
      if items[i] > items[j]:
        count += 1
  return count

def countAndMerge(left, right):
  outArr = []
  totalLength = len(left) + len(right)
  leftIndex = 0
  rightIndex = 0
  tally = 0
  for i in range(0,totalLength):
    if leftIndex < len(left):
      if rightIndex < len(right): 
        if (left[leftIndex] <= right[rightIndex]):
          outArr.append(left[leftIndex])
          leftIndex += 1
        else:
          outArr.append(right[rightIndex])
          rightIndex += 1
          tally += len(left) - leftIndex
      else:
        outArr.append(left[leftIndex])
        leftIndex += 1
    else: # leftIndex out of range; no need to update tally so just append
      if rightIndex < len(right):
         outArr.append(right[rightIndex])
         rightIndex += 1

  return (tally, outArr)


def countAndSort(items):
  #print "Input"
  #print items
  #print "ENd INput"
  if len(items) <= 1:
    return (0, items)
  else:
    middle = len(items)/2

    (leftInv, lsorted)  = countAndSort(items[:middle])
    #print "lvals"
    #print leftInv, lsorted
    #print "end lvals"
    (rightInv, rsorted) = countAndSort(items[middle:])

    (splitInv, ssorted) = countAndMerge(lsorted, rsorted)
    return (leftInv + rightInv + splitInv, ssorted)
  #return (0,[])
    

def countInversions(items):
  (count, srtd) = countAndSort(items) # note that length is carried along with the len function
  #print items
  #print srtd
  return count

if __name__ == "__main__":  
  debug = False
  if len(sys.argv) > 1:
    debug = True
  items = []
  if debug:
    items = range(0, int(sys.argv[1]))
    random.shuffle(items)
    print "Naive algorithm gives:"
    print countInversionsDumbWay(items)
    print "======================="
  else:
    integerFile = open('IntegerList.txt')  
    for line in integerFile:
      items.append(int(line))

  # Now for the smarter way  
  print "Naive algorithm gives:"
  print countInversionsDumbWay(items)
  print "======================="

  a = countInversions(items)
  print a

  #print items
  #a = countAndMerge(items[0:len(items)/2],items[len(items)/2:])
  #print a
