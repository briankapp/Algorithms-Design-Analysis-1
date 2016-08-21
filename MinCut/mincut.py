#!/usr/bin/python
import random

def removeEdge(adjList, vertex1, vertex2, supernodes):
  # hand over all edges from in vertex2 to vertex 1
  for vertex in adjList[vertex2]:
    if not (supernodes[vertex] == vertex1):
      adjList[vertex1].append(supernodes[vertex])

  del adjList[vertex2]

  # update supernode list; probably doing too much work here
  for i in supernodes:
    if supernodes[i] == vertex2:
      supernodes[i] = vertex1
  
  # update adjacency list to get everybody's supernode
  tmp = []
  for i in range(0,len(adjList[vertex1])):
    if not supernodes[adjList[vertex1][i]] == vertex1:
      tmp.append(supernodes[adjList[vertex1][i]])
  adjList[vertex1] = sorted(tmp)

  return  

def setupGraph():
  #graphFile = open("dinkyMinCut.txt")
  graphFile = open("kargerMinCut.txt")
  adjacenciesMaster = {}
  supernodes = {}

  for line in graphFile:
    nodeTmp = line.strip().split("\t")
    nodeAdj = []
    for item in nodeTmp:
      nodeAdj.append(int(item))
    i = nodeAdj[0]
    supernodes[i] = 1
    nodeAdj = sorted(nodeAdj[1:])
    adjacenciesMaster[i] = nodeAdj
  graphFile.close()
  return adjacenciesMaster, supernodes


if __name__ == "__main__":
  adjacencies, supernodes = setupGraph()
  numNodes = len(adjacencies)
  minCrossingNum = numNodes - 1
  bestSuperNodes = {}
  for trial in range(0,200):
    adjacencies, supernodes = setupGraph()
    for i in adjacencies:
      supernodes[i] = i

    while len(adjacencies) > 2:
      index1 = random.randint(0,len(adjacencies)-1)
      v1 = adjacencies.keys()[index1]
      index2 = random.randint(0,len(adjacencies[v1])-1)
      v2 = supernodes[adjacencies[v1][index2]]
      removeEdge(adjacencies, v1, v2, supernodes)
  
    if len(adjacencies[adjacencies.keys()[0]]) != len(adjacencies[adjacencies.keys()[1]]):
      print "UH-OH! It looks like something went wrong"
    else:
      crossingNumber = len(adjacencies[adjacencies.keys()[0]])
      print "Crossing number for trial " + str(trial) + " is: " + str(crossingNumber)
      if crossingNumber < minCrossingNum:
        minCrossingNum = crossingNumber
        bestSuperNodes = supernodes
    for v in adjacencies:
      for i in range(0,len(adjacencies[v])):
        adjacencies[v][i] = supernodes[v]
    #print adjacencies

  print "Minimum crossing number is: " + str(minCrossingNum)
    #print adjacencies
  #for i in sorted(supernodes.keys()):
  #  print i, supernodes[i]
  
