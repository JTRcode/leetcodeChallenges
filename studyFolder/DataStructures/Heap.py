'''
Max Min Heap

Binary Heap
Fibonacci Heap

find min     O(1)       O(1)
delete min   O(logn)    O(logn)
insert       O(logn)    O(1)
decrease key O(logn)    O(1)
merge        O(n)       O(1)
'''

import heapq
H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)

'''
heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

heapq.heappushpop(heap, item)
Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

heapq.heapify(x)
Transform list x into a heap, in-place, in linear time.
'''