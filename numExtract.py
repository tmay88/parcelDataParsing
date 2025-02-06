#Take the numbers at start of string and apply to another field
def numExtract(entry):
    housenum = ''
    for x in entry:
        if x.isnumeric():
            housenum += x
        else:
            break
    return housenum
