#splits a string on blank spaces. Concatenates and returns everything except for the last entry

def dropLast(entry):
    splitEntry = entry.split()
    concat = ' '.join(splitEntry[:-1])
    return concat.strip()
    
dropLast(!streetname!)
    
#Removes the string found in Placename field from the FullAddress string
def removePname(fulladd, pname):
    update = fulladd.replace(pname, '')
    return update
 
#For loop on string stops at specified character/sign
def loopAt(entry):
    newEntry = []
    for x in entry:
        if x != '@':
            newEntry.append(x)
        else:
            break            
    return ''.join(newEntry).strip()
 
#Removes all whitespace and replaces with a single whitespace character
' '.join(mystring.split()) 