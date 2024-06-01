def removePredir(streetname, predir):
    if predir is None:
        return streetname
    
    splitStreetname = streetname.split(maxsplit=1)
    if len(splitStreetname) == 1:
        return streetname
    
    return splitStreetname[1]