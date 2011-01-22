import Queue

class SortNode(object):
    
    array = []
    cost = 0
    pos = 0

    def __init__(self, array, cost, pos):
        self.array = list(array)
        self.cost = cost
        self.pos = pos


    def __str__(self):
        return '%s, %d, %d' % (self.array, self.cost, self.pos)


def find_unsorted_element(array):
    '''
    Returns index before first unsorted element in array.
    Returns -1 if array is sorted.
    '''
    for i in xrange(0, len(array)-1):
        current = array[i]
        next = array[i+1]
        if (current > next):
            return i
            
    return -1 


def is_sorted(node):
    '''
    Check if node is sorted.
    '''
    return find_unsorted_element(node.array) == -1


def get_nodes(node):
    '''
    Generates new nodes to check.
    '''
    v1_idx = find_unsorted_element(node.array)
    if (v1_idx == -1):
        raise RuntimeError('Array is sorted')

    v2_idx = v1_idx + 1

    v2 = node.array[v2_idx]

    # Decreasing number case
    dnc = SortNode(node.array, node.cost, v2_idx)
    j = v1_idx

    # Decrease all previous number that bigger than v2
    while(j >= 0 and dnc.array[j] > v2):
        dnc.cost += dnc.array[j]-v2
        dnc.array[j] = v2
        j-=1

    # Removing number case
    rnc = SortNode(node.array, node.cost, v1_idx)
    del rnc.array[v2_idx]
    rnc.cost += node.array[v2_idx]

    return (dnc.cost, dnc), (rnc.cost, rnc)


def sort(A):
    '''
    Actual method to solve the problem.
    Modification of Dijkstra shortest path algorithm.
    
    Note: It's somewhat inefficient to iterate over the array
    both inside is_sorted() and get_nodes() functions.
    But it was made intensionally to clarify relation to Dijkstra
    shortest path algorithm.
    '''
    initial = SortNode(A, 0, 0)
    queue = Queue.PriorityQueue()

    queue.put((0, initial))

    while(True):
        p, next = queue.get()
        print 'Got from queue:', next

        if (is_sorted(next)):
            return next.array, next.cost

        new_nodes = get_nodes(next)

        for n in new_nodes:
            queue.put(n)

