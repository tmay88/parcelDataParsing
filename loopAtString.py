#for loop on string that takes a string value to loop against
def loopAt(entry):
    newEntry = []
    i = 0  # Counter to handle substring checking
    while i < len(entry):
        # Check for 'SCHOOL' starting at the current position
        if entry[i:i+len('SCHOOL')] == 'SCHOOL':
            break
        newEntry.append(entry[i])
        i += 1
            
    return ''.join(newEntry).strip()
