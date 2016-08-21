#!/usr/bin/python
import random
import sys

def partition(myArray, l, r):

  firstIndex  = l
  lastIndex   = r - 1
  middleIndex = (l + r-1) / 2
  first       = myArray[firstIndex]
  last        = myArray[lastIndex]
  middle      = myArray[middleIndex]

  medianIndex = firstIndex
  if (first < middle < last) or (last < middle < first):
    medianIndex = middleIndex
  elif (first < last < middle) or (middle < last < first):
    medianIndex = lastIndex

  pivotIndex = medianIndex
  pivot = myArray[pivotIndex]
  myArray[pivotIndex] = myArray[l]
  myArray[l] = pivot
  pivotIndex = l
  i = l + 1

  for j in range(i, r):   
    # don't need to do anything if entry j is > pivot
    if myArray[j] < pivot:      
      tmp = myArray[j]
      myArray[j] = myArray[i]
      myArray[i] = tmp
      i += 1

  tmp = pivot 
  myArray[pivotIndex]   = myArray[i-1]
  myArray[i-1] = pivot

  return i

def quickSort(myArray, lo, hi):
  comparisons = max(hi-lo-1,0)
  #print hi, lo, comparisons
  if lo < hi:    
    p = partition(myArray, lo, hi)        
    comparisons += quickSort(myArray, lo, p-1)
    comparisons += quickSort(myArray, p, hi)

  return comparisons

if __name__ == "__main__":
  debug = False
  sortThis = []
  if debug:
    sortThis = range(0,int(sys.argv[1]))
    random.shuffle(sortThis)
    if len(sortThis) < 30:
      print sortThis
  else:
    test = open("quicksort.txt")
    for line in test:
      sortThis.append(int(line))

  comps = quickSort(sortThis, 0, len(sortThis))
  if len(sortThis) < 30:
    print sortThis
  print comps
