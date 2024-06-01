def removeHouseNumber(streetname, housenum):
    if housenum is None:
        return streetname
    
    splitadd = streetname.split(maxsplit=1)
    if len(splitadd) == 1:
        return streetname
    
    return splitadd[1]
