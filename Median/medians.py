#!/usr/bin/python

def heapInsert(theHeap, num, maintainMin = True):
  theHeap.append(num)
  index = len(theHeap) - 1
  parentIndex = (index-1)/2  
  if maintainMin:
    while (theHeap[index] < theHeap[parentIndex]) and (index > 0):
      tmp = theHeap[index]
      theHeap[index] = theHeap[parentIndex]
      theHeap[parentIndex] = tmp
      index = parentIndex
      parentIndex = (index-1)/2
  else:
    while (theHeap[index] > theHeap[parentIndex]) and (index > 0):
      tmp = theHeap[index]
      theHeap[index] = theHeap[parentIndex]
      theHeap[parentIndex] = tmp
      index = parentIndex
      parentIndex = (index-1)/2

  return

def twoValMinIndex(myArr, index):
  leftChildIndex  = 2*index + 1
  rightChildIndex = 2*index + 2
  infty      = float("inf")
  leftChild  = infty
  rightChild = infty

  if leftChildIndex < len(myArr):
    leftChild = myArr[leftChildIndex]
  if rightChildIndex < len(myArr):
    rightChild = myArr[rightChildIndex]
  
  if min(rightChild, leftChild) == infty:
    return infty
  elif rightChild < leftChild:
    return rightChildIndex
  else:
    return leftChildIndex

def twoValMaxIndex(myArr, index):
  leftChildIndex  = 2*index + 1
  rightChildIndex = 2*index + 2
  infty      = float("inf")
  leftChild  = -infty
  rightChild = -infty

  if leftChildIndex < len(myArr):
    leftChild = myArr[leftChildIndex]
  if rightChildIndex < len(myArr):
    rightChild = myArr[rightChildIndex]

  if max(rightChild, leftChild) == -infty:
    return infty
  elif rightChild < leftChild:
    return leftChildIndex
  else:
    return rightChildIndex


def heapExtract(theHeap, maintainMin = True):
  tmp = theHeap[0]
  theHeap[0] = theHeap[len(theHeap) - 1] 
  theHeap[len(theHeap) - 1] = tmp
  retval  = theHeap.pop()
  index = 0
  infty = float("inf")
  if maintainMin:
    minChildIndex = twoValMinIndex(theHeap, index)
    while minChildIndex < infty:
      if theHeap[index] > theHeap[minChildIndex]:
        tmp = theHeap[index]
        theHeap[index] = theHeap[minChildIndex]
        theHeap[minChildIndex] = tmp
        index = minChildIndex
        minChildIndex = twoValMinIndex(theHeap, index)      
      else:
        break
      
  else:
    maxChildIndex = twoValMaxIndex(theHeap, index)
    while maxChildIndex < infty:
      if theHeap[index] < theHeap[maxChildIndex]:
        tmp = theHeap[index]
        theHeap[index] = theHeap[maxChildIndex]
        theHeap[maxChildIndex] = tmp
        index = maxChildIndex
        maxChildIndex = twoValMaxIndex(theHeap, index)
      else:
        break

  return retval

if __name__=="__main__":
  testVals = open("medianMaintTest.txt")
  heaplo  = []
  heaphi  = []  
  medians = []
  numvals = 0 

  # This is better done in a single for loop, but I got started down a path 
  # and it was just easier to leave this setup in place
  minv = float("inf")
  maxv = -minv

  for line in testVals:
    line = line.strip()
    num  = int(line)
    
    if num < minv:
      minv = num
    if num > maxv:
      maxv = num
    numvals += 1
    if numvals == 1:
      medians.append(num)
    if numvals > 1:
      break

  heaplo.append(minv)
  heaphi.append(maxv)
  medians.append(minv)

  for line in testVals:
    line = line.strip()
    num  = int(line)
    if num <= heaplo[0]:
      heapInsert(heaplo, num, False)
    else:
      heapInsert(heaphi, num, True)
   
    numvals += 1
    if (numvals % 2) == 0:
      if len(heaphi) > len(heaplo):
        heapInsert(heaplo, heapExtract(heaphi, True), False)
      elif len(heaplo) > len(heaphi):
        heapInsert(heaphi, heapExtract(heaplo, False), True)

    # now get median
    if (numvals % 2) == 0:
      if len(heaplo) == numvals/2:
        medians.append(heaplo[0])
      else:
        print "Something's wrong"
    else:
      if len(heaplo) == (numvals + 1)/2:
        medians.append(heaplo[0])
      elif len(heaphi) == (numvals + 1)/2:
        medians.append(heaphi[0])        
      else:
        print "Bad things happened"

  zz = sum(medians)
  mod = zz % 10000
  print zz
  print mod
  # answer is 1213
