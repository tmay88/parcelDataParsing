#For loop on string stops at specified character/sign
def loopAt(entry):
    newEntry = []
    for x in entry:
        if x != '@':
            newEntry.append(x)
        else:
            break            
    return ''.join(newEntry).strip()
