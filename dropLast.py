#splits a string on blank spaces. Concatenates and returns everything except for the last entry

def dropLast(entry):
    splitEntry = entry.split()
    concat = ' '.join(splitEntry[:-1])
    return concat.strip()

#dropLast(!streetname!)
