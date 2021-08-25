def what_to_do(instructions):
    s = "Simon says"
    instructions = instructions.strip(" ")
    poz1 = instructions.find(s)
    poz2 = len(instructions) - (instructions.rfind(s) + len(s))
    
    if poz1 == 0 or poz2 == 0:
        instructions = instructions.replace(s, "")
        instructions = instructions.strip(" ")
        return "I " + instructions
    else:
        return "I won't do it!"
