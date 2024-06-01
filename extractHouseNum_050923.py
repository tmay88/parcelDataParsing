def extractHouseNum(address):
    numList = []
    for value in address:
        if not value.isdigit():
            break
        numList.append(value)

    addnum = ''.join(numList)

    if addnum == '':
        return None
    elif len(addnum) > 10:
        return addnum[:10]
    else:
        return addnum.strip()
