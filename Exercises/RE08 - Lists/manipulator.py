'''
1. insert i e: Insert integer e at position i.
2. print: Save list to result string.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list in ascending order.
6. pop: Remove the last element from the list.
7. reverse: Reverse the list.
'''

def manipulator(l, cmds):
    save = ""
    for command in cmds:
        instructions = command.split()
        if "insert" in instructions:
            l.insert(int(instructions[1]), int(instructions[2]))
        if "print" in instructions:   
            save += str(l) + " "
        if "remove" in instructions:
            l.remove(int(instructions[1]))           
        if "append" in instructions:
            l.append(int(instructions[1]))
        if "sort" in instructions:
            l = sorted(l)
        if "pop" in instructions:
            l.pop()       
        if "reverse" in instructions:
            l = l[::-1]
    return save