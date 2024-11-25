import os
import ast
import heapq

# define all possible actions within a dictionary
conversions = {
    1: [1, 0, 0],
    2: [-1, 0, 0],
    3: [0, 1, 0],
    4: [0, -1, 0],
    5: [0, 0, 1],
    6: [0, 0, -1],
    7: [1, 1, 0],
    8: [1, -1, 0],
    9: [-1, 1, 0],
    10: [-1, -1, 0],
    11: [1, 0, 1],
    12: [1, 0, -1],
    13: [-1, 0, 1],
    14: [-1, 0, -1],
    15: [0, 1, 1],
    16: [0, 1, -1],
    17: [0, -1, 1],
    18: [0, -1, -1]
}

# bfs
def bfs(tree, visited, entrance, exit):
    # add starting node to visited and to queue
    visited.add(entrance)
    queue = [(entrance, "(" + str(tuple(entrance)))] # cost, node, path
    prevcost = 0
    # open outfile
    outfile = open("output.txt", "w")
    # while there are still items in queue
    while queue:
        # access next path in queue
        node, temp = queue.pop(0)
        # if node at the end of that path is the exit node, print to outfile
        if node == exit:
            temp = ast.literal_eval(temp + ")")
            outfile.write(str(temp.index(node)) + "\n" + str(len(temp)) + "\n")
            for i in temp:
                outfile.write(str(i).strip("()").replace(",", "") + " " + str(temp.index(i) - prevcost) + "\n")
                prevcost = temp.index(i)
            outfile.close() 
            return
        # create set of children who have not yet been visited
        unvisitedchildren = tree[tuple(node)] - visited
        # ensure that only legal children are in the unvisited set
        # push path for each valid child to queue
        [queue.append((child, str(temp + ", " + str(child)))) for child in unvisitedchildren if child in tree.keys()]
        # add children and node to visited set
        visited.update(tree[tuple(node)])
        visited.add(node)
    # output FAIL if exit is not found
    outfile.write("FAIL") 
    outfile.close() 

# ucs
def ucs(tree, visited, entrance, exit):
    # add starting node to visited and to queue
    visited.add(entrance)
    queue = [(0, entrance, "(" + str(tuple(entrance)))] # cost, node, path
    prevnode = entrance
    # open outfile
    outfile = open("output.txt", "w")  
    # while there are still items in queue
    while queue:
        # pull path with least cost from queue 
        totalcost, node, temp = queue.pop(0)
        # if node at the end of that path is the exit node, print to outfile
        if node == exit:
            temp = ast.literal_eval(temp + ")")
            outfile.write(str(totalcost) + "\n" + str(len(temp)) + "\n")
            for i in temp:       
                outfile.write(str(i).strip("()").replace(",", "") + " " + str(finducscost(prevnode, i, 0)) + "\n")
                prevnode = i
            outfile.close() 
            return
        # create set of children who have not yet been visited
        unvisitedchildren = tree[tuple(node)] - visited
        # ensure that only legal children are in the unvisited set
        # push path for each valid child to queue
        [heapq.heappush(queue, (finducscost(node, child, totalcost), child, str(temp + ", " + str(child)))) for child in unvisitedchildren if child in tree.keys()] 
        # add children and node to visited set
        visited.update(tree[tuple(node)])
        visited.add(node)
    # output FAIL if exit is not found
    outfile.write("FAIL") 
    outfile.close()   

# a*
def astar(tree, visited, entrance, exit):
    # add starting node to visited and to queue
    visited.add(entrance)
    queue = [(findfuturecost(entrance, exit), 0, entrance, "(" + str(tuple(entrance)))] # cost, node, path
    prevnode = entrance
    # open outfile
    outfile = open("output.txt", "w")
    # while there are still items in queue
    while queue:
        # pull path with least cost from queue 
        combinedcost, totalcost, node, temp = queue.pop(0)
        # if node at the end of that path is the exit node, print to outfile
        if node == exit:
            temp = ast.literal_eval(temp + ")")
            outfile.write(str(totalcost) + "\n" + str(len(temp)) + "\n")
            for i in temp:     
                outfile.write(str(i).strip("()").replace(",", "") + " " + str(finducscost(prevnode, i, 0)) + "\n")
                prevnode = i
            outfile.close() 
            return
        # create set of children who have not yet been visited
        unvisitedchildren = tree[tuple(node)] - visited
        # push path for each valid child to queue
        for child in unvisitedchildren:
            if child in tree.keys():
                pastcost = finducscost(node, child, totalcost)
                futurecost = findfuturecost(child, exit)
                combinedcost = pastcost + futurecost
                heapq.heappush(queue, (combinedcost, pastcost, child, str(temp + ", " + str(child)))) 
        # add children and node to visited set
        visited.update(tree[tuple(node)])
        visited.add(node)
    # output FAIL if exit is not found
    outfile.write("FAIL") 
    outfile.close()   

# function to combine lists to make movements
def combine(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

# function to find cost between two nodes for ucs
def finducscost(node, child, totalcost):
    total = abs(node[0] - child[0]) + abs(node[1] - child[1]) + abs(node[2] - child[2])
    if total == 2 or total == 3:
        return totalcost + 14
    elif total == 1:
        return totalcost + 10
    else:
        return 0

# function to estimate future cost for a*
def findfuturecost(child, exit):
    return pow(pow(exit[0] - child[0], 2) + pow(exit[1] - child[1], 2) + pow(exit[2] - child[2], 2), 0.5)

# main function
def main():
    # delete any existing output.txt file
    if os.path.exists("output.txt"):
        os.remove("output.txt")
    else:
        print("The file does not exist")
    # open input.txt file for reading
    infile = open("input.txt", "r")
    inputlines = infile.readlines()
    # store input file contents in variables
    algo = inputlines[0].strip()
    entrance = tuple(int(i) for i in inputlines[2].strip().split())
    exit = tuple(int(i) for i in inputlines[3].strip().split())
    tree = {}
    for numlines in range(5, len(inputlines)):
        line = tuple(int(i) for i in inputlines[numlines].strip().split())
        tree[tuple(line[0:3])] = set(combine(line[0:3], conversions[j]) for j in line[3:])
    infile.close()
    # utilize the appropriate search algorithm
    visited = set()
    if algo == 'BFS':
        bfs(tree, visited, entrance, exit)
    elif algo == 'UCS':
        ucs(tree, visited, entrance, exit)
    elif algo == 'A*':
        astar(tree, visited, entrance, exit)
    else:
        print("Invalid input.txt file search algorithm")

# call main function    
if __name__ == "__main__":
    main()   