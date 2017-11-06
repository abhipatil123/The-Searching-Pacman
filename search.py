# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    # The data structure used is a stack to store the nodes which are eventually popped and expanded to get its successors

    from util import Stack
    L=list()
    expanded=list()
    obj=Stack()
    direction=list()
    current_direction=list()
    current_coordinates=problem.getStartState()
    while((problem.isGoalState(current_coordinates))==False):
       	for i in problem.getSuccessors(current_coordinates):	
		direction=current_direction[:]
		direction.append(i[1])
		if not(current_coordinates in expanded):
			expanded.append(current_coordinates)
		if not(i[0] in expanded):   		
			obj.push((i[0],direction,i[2]))

	current_state=obj.pop()
        
	while(current_state[0] in expanded):
		current_state=obj.pop()

	current_coordinates=current_state[0]
	current_direction=current_state[1]
    L=(current_state[1])
    return L	 
            
    util.raiseNotDefined()


# The data structure used is a queue to store the nodes which are eventually popped and expanded to get its successors.

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    from util import Queue
    L=list()
    expanded=list()
    q=Queue()
    direction=list()
    current_direction=list()
    current_coordinates=problem.getStartState()
    while((problem.isGoalState(current_coordinates))==False):
       	for i in problem.getSuccessors(current_coordinates):	
		direction=current_direction[:]
		direction.append(i[1])
		if current_coordinates not in expanded:
			expanded.append(current_coordinates)
		if i[0] not in expanded:   					
			q.push((i[0],direction,i[2]))

	current_state=q.pop()
        while(current_state[0] in expanded):
		current_state=q.pop()

	current_coordinates=current_state[0]
	current_direction=current_state[1]
    L=(current_state[1])
    return L	 
    util.raiseNotDefined()



# The data structure used is a priority queue to store the nodes which are eventually popped and expanded to get its successors. The priority to the nodes is on the basis of its cost of the path from the start node.
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue
    from searchAgents import PositionSearchProblem
    L=list()
    expanded=list()
    pq=PriorityQueue()
    direction=list()
    current_direction=list()
    current_coordinates=problem.getStartState()
    while((problem.isGoalState(current_coordinates))==False):
       	for i in problem.getSuccessors(current_coordinates):	
		direction=current_direction[:]
		direction.append(i[1])
		if not(current_coordinates in expanded):
			expanded.append(current_coordinates)
		if not(i[0] in expanded):
			
			pq.push((i[0],direction,i[2]),problem.getCostOfActions(direction))

	current_state=pq.pop()
        while(current_state[0] in expanded):
		current_state=pq.pop()

	current_coordinates=current_state[0]
	current_direction=current_state[1]
    L=(current_state[1])
    return L	 
    	
    
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


# The data structure used is a priority queue to store the nodes which are eventually popped and expanded to get its successors. The priority to every node is given on the basis of its heuristic value

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    from searchAgents import manhattanHeuristic
    from searchAgents import PositionSearchProblem
    L=list()
    expanded=list()
    pq=PriorityQueue()
    direction=list()
    current_direction=list()
    current_coordinates=problem.getStartState()
    while((problem.isGoalState(current_coordinates))==False):
       	for i in problem.getSuccessors(current_coordinates):	
		direction=current_direction[:]
		direction.append(i[1])
		if not(current_coordinates in expanded):
			expanded.append(current_coordinates)
		if not(i[0] in expanded):
			
			pq.push((i[0],direction,i[2]),(problem.getCostOfActions(direction)+heuristic(i[0],problem)))

	current_state=pq.pop()
        while(current_state[0] in expanded):
		current_state=pq.pop()

	current_coordinates=current_state[0]
	current_direction=current_state[1]
    L=(current_state[1])
    return L	 
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
