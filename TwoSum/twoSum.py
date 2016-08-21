#!/usr/bin/python

def canSum(n, hashTable):
  for t in hashTable:
    try:
      if (n-t) in hashTable:
        return 1
    except:
      continue
  return 0

if __name__ == "__main__":
  myfile  = open("twoSum.txt")
  numHash = {}
  for line in myfile:
    line = line.strip()
    numHash[int(line)] = True
  distinctSums = 0
  for i in range(-10000, 10001):
    distinctSums += canSum(i, numHash)
    if ((i+10000) % 100) == 0:
      print i
  print distinctSums
  # answer is 427
