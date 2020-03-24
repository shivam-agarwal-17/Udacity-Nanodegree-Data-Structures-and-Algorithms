from heapq import heappop, heappush
import math

class Node:
    
    def __init__(self, idx=None, f=float("inf"), predecessor_idx=None):
        self.idx = idx
        self.f = f
        self.predecessor_idx = predecessor_idx
    
    def __gt__(self, node):
        return self.f > node.f
    
def eucledian_distance(M, node_1, node_2):
    """
    Calculates the eudcledian distance between two nodes of the Map.
    """
    return math.sqrt((M.intersections[node_1][0] - M.intersections[node_2][0])**2 + \
                     (M.intersections[node_1][1] - M.intersections[node_2][1])**2)

def shortest_path(M,start,goal):
    print("shortest path called")
    
    def edge_weight(node_1, node_2):
        return eucledian_distance(M, node_1, node_2)
    
    def heuristic(node):
        return eucledian_distance(M, node, goal)
    
    frontier = [Node(start, heuristic(start))]
    explored = dict() # dictionary of explored nodes, maps node index to Node object
    
    while len(frontier) != 0:
        from_node = heappop(frontier)
        
        if from_node.idx == goal: # goal node is popped from frontier, no further exploration is needed
            explored[from_node.idx] = from_node
            break
        
        if from_node.idx in explored: 
            continue
        
        for to_node_idx in M.roads[from_node.idx]:
            if to_node_idx in explored:
                continue
            
            curr_edge_weight = edge_weight(from_node.idx, to_node_idx)
            to_node_f = from_node.f - heuristic(from_node.idx) + curr_edge_weight + heuristic(to_node_idx)
            
            heappush(frontier, Node(to_node_idx, to_node_f, from_node.idx))
            
        explored[from_node.idx] = from_node
    
    path = []
    curr_node_idx = from_node.idx
    while curr_node_idx is not None:
        path.append(curr_node_idx)
        curr_node_idx = explored[curr_node_idx].predecessor_idx
        
    return path[::-1]
        
## for debugging
def path_cost(M, path):
    path_cost = 0
    for idx in range(1, len(path)):
        print(f"Adding distance between {path[idx]} and {path[idx-1]}")
        path_cost += heuristic(M, path[idx], path[idx-1])

    print("Total path cost: ", path_cost)
    return path_cost
    
            