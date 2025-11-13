stack = []

def push(stack, element):
    stack.append(element)
    return stack

def pop(stack):
    if len(stack) == 0:
        return "Stack is empty"
    return stack.pop()

def size(stack):
    return len(stack)