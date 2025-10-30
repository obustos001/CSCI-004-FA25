q = []
head = 0

def tail(q):
    return len(q)

def push(q, e):
    q.append(e)
    return q

def pop(q):
    return q.pop(head)