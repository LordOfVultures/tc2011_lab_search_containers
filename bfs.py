import fileinput
import copy

initial_state = []
end_state = []
visited = []
forExploring=[]

leaves_nodes =[]

#function that reads input
def readingInput(): 
    #input = fileinput.input()
    archi=open('Test1.txt','r')
    global end_state
    global initial_state
    i = 0
    #for line in input:  # read line by line of stdin
    for line in archi.readlines():  
        i += 1
        if i == 1:  # reads first line, which contains maximum stack height
            max_stack = int(line.strip())
            print (max_stack)
        elif i == 2:  # reads second line, which contains the intial state
            # the following block formats the line and creates the initial state data structure
            initial_state = line.strip()
            initial_state = initial_state.replace(" ", "")
            initial_state = initial_state.replace("(", "")
            initial_state = initial_state.replace(")", "")
            initial_state = initial_state.split(';')
            for i, element in enumerate(initial_state):
                initial_state[i] = element.split(",")
            print(initial_state)
        elif i == 3:  # reads the third line, which contains the end state
            # the following block formats the line and creates the end state data structure
            end_state = line.strip()
            end_state = end_state.replace(" ", "")
            end_state = end_state.replace("(", "")
            end_state = end_state.replace(")", "")
            end_state = end_state.split(';')
            for i, element in enumerate(end_state):
                end_state[i] = element.split(",")
            print(end_state)
        
    
    archi.close()


def bfs():
    global initial_state
    global end_state
    global visited 
    global forExploring
    forExploring.append(initial_state)
    visited.append(initial_state)
    current_node =[]
    while(forExploring ):#if not empty
        current_node=forExploring.pop(0)#getting first element of the list
        print ("Current",current_node)
        creatingNode(current_node)        
        
    

def creatingNode(state):
    global leaves_nodes #variable that has the results of the nodes
    
    
    for element in range(len(state)): 
        #print ("Elemento:",state[element]) 
        
        
        for listNode in range(len(state)):
            
            list_Nodes=copy.deepcopy(state) #copying the state
            if (list_Nodes[element]):
                #print(list_Nodes)
                
                if (list_Nodes[element]): #in case the spot is not empty
                    #list_Nodes[element].remove(state[element][0]) #remove the element from the list                       
                    list_Nodes[element].pop(0)
                
                
                if (element != listNode ):  
                    
                    #if (not list_Nodes[listNode]):#is empty
                    # list_Nodes[listNode].append("")
                    #print ( state[element][0] , state[listNode])
                                                        
                    list_Nodes[listNode].append(state[element][0]) #adding the new element to the assigned space
                    #print ("        Final",list_Nodes)
                    leaves_nodes.append(list_Nodes) #Saving Result
    
    comparingLists(visited,leaves_nodes)
    
def comparingLists(listVisited , listNewNodes):
        global visited
        
        
        for nodeVisited in range(len(listVisited)):
            for nodeNew in range(len(listNewNodes)):
                if (cmp(listVisited[nodeVisited], listNewNodes[nodeNew]) != 0): #if the nodes are not in the visited list
                    forExploring.append(listNewNodes[nodeNew]) #adding new nodes to forExploring
                    visited.append(listNewNodes[nodeNew]) #adding new nodes to visited
        
        #print(leaves_nodes)
        
readingInput()
#creatingNode( [['A'], ['B'], ['C']])
bfs()
