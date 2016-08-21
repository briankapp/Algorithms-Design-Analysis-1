#!/usr/bin/python
import sys

def loadGraph(fname, reverse = False, swaplabels = False, newlabels = []):
  graphFile = open(fname)
  graph     = {}

  for line in graphFile:
    parts  = line.split()    
    source = int(parts[0])
    dest   = int(parts[1])
    if source == dest:
      continue
    if swaplabels:
      source = newlabels[source]
      dest   = newlabels[dest]    

    if not(source in graph):
      graph[source] = {}
      graph[source]['edges'] = []
      graph[source]['explored'] = False
    if not(dest in graph):
      graph[dest] = {}
      graph[dest]['edges'] = []
      graph[dest]['explored'] = False

    if not reverse:      
      graph[source]['edges'].append(dest)
    else:       
      graph[dest]['edges'].append(source)
  graphFile.close()
  return graph

def depthFirstSearch(graph, node, leader):
  global stoptime
  graph[node]['explored'] = True
  graph[node]['leader']   = leader
  for endpoint in graph[node]['edges']:
    if not graph[endpoint]['explored']:
      depthFirstSearch(graph, endpoint, leader)
  stoptime += 1
  graph[node]['stoptime'] = stoptime
  return

def dfsLoop(graph):
  numnodes = len(graph)
  s        = None
  global stoptime 
  stoptime = 0
  r        = range(1,numnodes+1)   
  r.reverse()
  for i in r:
    if not graph[i]['explored']:
      s = i
      depthFirstSearch(graph,i,s)
  return

if __name__ == "__main__":
  sys.setrecursionlimit(250000) # need to couple this with a ulimit -s 250000 on command line
  gfile = sys.argv[1]

  # first pass (on reverse graph)
  graphRev = loadGraph(gfile, reverse = True)
  dfsLoop(graphRev)
  
  # just to help with bookkeeping
  revOrder = []
  # leaving 0 alone just to make indexing easier; 
  # using revorder as an auxiliary can probably be avoided entirely
  for i in range(0,len(graphRev) + 1):
    revOrder.append(0)
  for i in graphRev:
    revOrder[i] = graphRev[i]['stoptime']
  del graphRev
  print "Done with reverse graph"
  # done with first pass

  # second pass (on regular graph relabeled with stop times)
  graph = loadGraph(gfile, reverse = False, swaplabels = True, newlabels = revOrder)
  dfsLoop(graph)
  # just a structure to get a count on the size of the SCC's 
  leaderCounts = {}
  for i in graph:
    if graph[i]["leader"] in leaderCounts:
      leaderCounts[graph[i]["leader"]] += 1
    else:
      leaderCounts[graph[i]["leader"]] = 1
  
  # unnecessary for counts, but kind of handy if you want to reconstruct/debug
  normalOrder = []
  for i in range(0,len(revOrder)):
    normalOrder.append(0)
  for i in range(0,len(revOrder)):
    normalOrder[revOrder[i]] = i
  #for i in leaderCounts:
    #print normalOrder[i]
    #for j in graph:
      #if i == graph[j]['leader']:
        #print "\t" + str(normalOrder[j])

  del graph
  nums = []
  for l in leaderCounts:
    nums.append(leaderCounts[l])

  nums = sorted(nums)
  nums.reverse()
  print nums[0:5]

  
