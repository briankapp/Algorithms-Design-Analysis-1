#!/usr/bin/python
import sys

def readGraph(filename):
  graph = {}
  gfile = open(filename)
  totalNodes = 0
  totalEdges = 0
  for line in gfile:
    line  = line.strip()
    parts = line.split("\t")
    node  = int(parts[0])
    if not node in graph:
      graph[node] = {}
      totalNodes += 1
    for part in parts[1:]:
      pp = part.split(",")
      edge = int(pp[0])
      weight = int(pp[1])
      graph[node][edge] = weight      
      totalEdges += 1
  print "Nodes: " + str(totalNodes)
  print "Edges: " + str(totalEdges)
  exit()
  return graph

def dijkstra(graph, start):
  # X keeps track of vertices visited
  X = []
  X.append(start)
  edgeChecks  = 0
  nodeChecks  = 0
  #initialize distances (nec?)
  for node in graph:
    distance = float("inf")
    if node == start:
      distance = 0
    graph[node]['distance'] = distance

  allEdgesInX = False  

  # this while loop will execute at most n-1 times
  while (len(X) < len(graph)) and not allEdgesInX:
    roundMin  = float("inf")
    roundNode = None
    allEdgesInX = True
    # there are always <= m checks of edges in the iteration of the for node in X loop 
    # (won't check any edge more than once)
    for node in X:
      nodeChecks += 1
      for edge in graph[node]:
        if edge == 'distance':
          continue
        edgeChecks += 1
        if not (edge in X):
          allEdgesInX = False
          if graph[node][edge] + graph[node]['distance'] < roundMin:
            roundMin  = graph[node][edge] + graph[node]['distance']
            roundNode = edge
    #print roundNode
    if not (roundNode == None):
      X.append(roundNode)
      graph[roundNode]['distance'] = roundMin
    if allEdgesInX:
      print "Got a break in the work - exiting early"   
  #print "Node checks: " + str(nodeChecks)
  #print "Edge checks: " + str(edgeChecks)
  return edgeChecks

if __name__ == "__main__":
  filename = 'dijkstraData.txt'  
  #basenode = int(sys.argv[1])
  graph = readGraph(filename)
  edgeChecks = 0
  for basenode in range(1,201):
    edgeChecks += dijkstra(graph,basenode)
    print str(basenode) + ":\t",
    for i in [7,37,59,82,99,115,133,165,188,197]:
      print str(graph[i]['distance']) + ",",
    print
  print
  print "total edge checks: " + str(edgeChecks)
