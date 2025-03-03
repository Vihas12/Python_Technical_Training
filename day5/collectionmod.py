import collections

# Double ended queue
# de=collections.deque([1,2,3])
# print("Dequeue: ",de)                       #Dequeue:  deque([1, 2, 3])
# de.append(4)        
# print(de)                                   #Dequeue:  deque([1, 2, 3, 4])
# de.appendleft(5)
# print(de)

de = collections.deque([6,1,2,3,4,5])
print(de)
de.pop()
print(de)
de.popleft()
print(de)