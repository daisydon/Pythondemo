# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def rebuilt_path(node,problem):
  print 'rebuild path here'
  action_list=[]
  init_position=problem.getStartState()
  while not node[0]==init_position:
    action=node[2]
    action_list.append(action)
    node=node[1]
  action_list.reverse()
  return action_list 
  
 
  

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  """ frontier is a stack to store node"""
  frontier=util.Stack()
  position=problem.getStartState() 
  init_node=(position,None,None)
  explored_set=set()
  """ explored_set: store the explored node"""
  frontier.push(init_node)
  while not frontier.isEmpty():
    father_node = frontier.pop()
    print father_node[0]
    position=father_node[0]
    explored_set.add(position)
    if problem.isGoalState(position):
      return rebuilt_path(father_node,problem)
    for successor in problem.getSuccessors(position):
      
      if not successor[0] in explored_set:
        successor_node=(successor[0],father_node,successor[1])
        frontier.push(successor_node)
      
   

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  
  frontier=util.Queue()
  position=problem.getStartState()
  init_node=(position,None,None)
  explored_set=set()
  frontier.push(init_node)
  while not frontier.isEmpty():
    father_node = frontier.pop()
    position=father_node[0]
    explored_set.add(position)
    if problem.isGoalState(position):
      return rebuilt_path(father_node,problem)
    for successor in problem.getSuccessors(position):
      if not successor[0] in explored_set:
        successor_node=(successor[0],father_node,successor[1])
        frontier.push(successor_node)
  
  util.raiseNotDefined()

def Priority(node):
  total_cost=node[3]
  return total_cost
  

def uniformCostSearch(problem):
  
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  
  position=problem.getStartState()
  
  frontier=util.PriorityQueueWithFunction(Priority)
  '''
  node = (position, father node, action from father node, cost from the root)
  '''
  init_node=(position,None,None,0)
  explored_set=set()
  frontier.push(init_node)
  while not frontier.isEmpty():
    father_node = frontier.pop()
    position=father_node[0]
    explored_set.add(position)
    if problem.isGoalState(position):
      return rebuilt_path(father_node,problem)
    for successor in problem.getSuccessors(position):
      if not successor[0] in explored_set:
        successor_node=(successor[0],father_node,successor[1],successor[2]+father_node[3])
        frontier.push(successor_node)
       
def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  
  
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  PriorityInAStar=lambda node: node[3] + heuristic(node[0],problem)
  
  position=problem.getStartState()
  
  frontier=util.PriorityQueueWithFunction(PriorityInAStar)
  '''
  node = (position, father node, action from father node,
  estimated cost of the cheapest solution from root to goal)
  '''
  init_node=(position,None,None,0)
  explored_set=set()
  frontier.push(init_node)
  while not frontier.isEmpty():
    father_node = frontier.pop()
    position=father_node[0]
    if problem.isGoalState(position):
      return rebuilt_path(father_node,problem)
    
    if not father_node[0] in explored_set:
      explored_set.add(position)
      for successor in problem.getSuccessors(position):
        successor_node=(successor[0],father_node,successor[1],successor[2]+father_node[3])
        frontier.push(successor_node)
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
