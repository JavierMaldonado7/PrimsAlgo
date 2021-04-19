#Prims Algo
#Javier Maldonado Rivera
#4/18/2020

test_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 12, 'D': 10, 'E': 4},
    'C': {'A': 3, 'B': 12, 'F': 5},
    'D': {'B': 10, 'E': 7},
    'E': {'B': 4, 'D': 7, 'F': 16},
    'F': {'C': 5, 'E': 16, 'G': 9},
    'G': {'F': 9},
}

def getNext(key,graph,doned):

    min = 0

    target = 0

    for value in graph.get(key):

        if(min == 0 and value not in doned):
            target = value
            min = graph.get(key).get(value)
        else:
            if(graph.get(key).get(value) < min and value not in doned):
                target = value
                min = graph.get(key).get(value)

    doned.append(target)
    return target

def recursiveSpan(graph, root,MST, done):
    while len(graph) > len(done):

        MST[root] = getNext(root,graph,done)
        print(dict(MST))
        print((done))
        if root not in done:
            done.append(root)
        recursiveSpan(graph,MST.get(root),MST,done)



def create_spanning_tree(graph,root):
    MST = {}

    done = []
    recursiveSpan(graph,root,MST,done)
    print(MST)






















