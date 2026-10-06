from collections import deque

lst = deque([])

lst.append(123)
lst.append(122)
lst.append(121)
lst.appendleft(124)
lst.appendleft(125)
lst.appendleft(123)
lst.popleft()
lst.pop()
lst.popleft()

print(lst)