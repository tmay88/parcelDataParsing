#Flips two splits
def flip(entry):
    splitEntry = entry.split()
    concat = ' '.join(splitEntry[1:] + [splitEntry[0]])
    return concat.strip()
