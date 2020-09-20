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
                    stack.append(people[i])
                    j = 0
                    break
                j += 1
            else:
                return "NO"
        if people[i] == 100:
            bill = 100
            while j < len(stack):
                if stack[j] == 50:
                    del stack[j]
                    j = 0
                    bill -= stack[j] 
                    break
                j += 1
            j = 0
            while j < len(stack) or bill == 25:
                if bill == 25:
                    stack.append(people[i])
                    j = 0
                    break
                if stack[j] == 25:
                    bill -= stack[j]
                    del stack[j]
                    j -= 1
                j += 1
            else:
                return "NO"
                j += 1
        i += 1
    return "YES"
