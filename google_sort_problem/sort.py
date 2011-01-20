import Queue

class SortEntry(object):
    
    array = []
    cost = 0
    pos = 0

    def __init__(self, array, cost, pos):
        self.array = list(array)
        self.cost = cost
        self.pos = pos


    def __str__(self):
        return '%s, %d, %d' % (self.array, self.cost, self.pos)


def sort(A):
    print 'Starting sort'
    initial = SortEntry(A, 0, 0)
    queue = Queue.PriorityQueue()
    queue.put((0, initial))
    while(True):
        p, next = queue.get()
        print 'Got from queue:', next
        for i in xrange(next.pos, len(next.array)-1):
            if (next.array[i] > next.array[i+1]):
                v2 = next.array[i+1]
                # Decreasing number case
                dnc = SortEntry(next.array, next.cost, i+1)
                j = i
                while(j >= 0 and dnc.array[j] > v2):
                    dnc.cost += dnc.array[j]-v2
                    dnc.array[j] = v2
                    j-=1

                queue.put((dnc.cost, dnc))

                # Removing number case
                rnc = SortEntry(next.array, next.cost, i)
                del rnc.array[i+1]
                rnc.cost += next.array[i+1]

                queue.put((rnc.cost, rnc))

                break
        else:
            # If for loop was not break, we have an optimum value
            return next.array, next.cost


