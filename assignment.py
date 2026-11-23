# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = [-1, -1, -1, -1, -1, -1, -1, -1]
TopOfStack = -1

def Push(Item):
    global Stack, TopOfStack
    if TopOfStack >= 7:
        return False
    TopOfStack += 1
    Stack[TopOfStack] = Item
    return True


def Pop():
    global Stack, TopOfStack
    if TopOfStack < 0:
        return -1
    Item = Stack[TopOfStack]
    TopOfStack -= 1
    return Item


# Exercise 2
def ShowStack():
    global Stack, TopOfStack
    if TopOfStack < 0:
        return ""
    items = []
    for i in range(TopOfStack, -1, -1):
        items.append(str(Stack[i]))
    return " ".join(items)


# Exercise 3
def DecimalToBinary(Number):
    global Stack, TopOfStack
    TopOfStack = -1
    if Number == 0:
        return "0"
    while Number > 0:
        Push(Number % 2)
        Number = Number // 2
    binary_digits = []
    while TopOfStack >= 0:
        binary_digits.append(str(Pop()))
        
    return "".join(binary_digits)

# Exercise 4
def Editor(Commands):
    global Stack, TopOfStack
    TopOfStack = -1
    for cmd in Commands:
        parts = cmd.split(" ")
        if parts[0] == "type":
            Push(parts[1])
        elif parts[0] == "undo":
            if TopOfStack >= 0:
                Pop()
    result_chars = []
    for i in range(TopOfStack + 1):
        result_chars.append(str(Stack[i]))
    return "".join(result_chars)
