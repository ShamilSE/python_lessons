def tickets(people):
    stack = []
    i = 0
    j = 0
    while i < len(people):
        if people[i] == 25:
            stack.append(people[i])
        if people[i] == 50:
            while j < len(stack):
                if stack[j] == 25:
                    del stack[j]
                    stack.append(people[j])
                    break
                j = j + 1
            else:
                return "NO"
        i = i + 1
    return "YES"

