def removeSufdir(address, sufdir):
    directionals = {
        ' S W': 4,
        ' S. W.': 5,
        ' N W': 4,
        ' N. W.': 5,
        ' S E': 4,
        ' S. E.': 5,
        ' N E': 4,
        ' N. E.': 5,
        ' S': 2,
        ' N': 2,
        ' E': 2,
        ' W': 2,
        ' SW': 3,
        ' NW': 3,
        ' SE': 3,
        ' NE': 3,
        ' SOUTH': 6,
        ' NORTH': 6,
        ' EAST': 5,
        ' WEST': 5
    }
    
    if sufdir is None:
        return address
        
    for key, value in directionals.items():
        if address.endswith(key):
            return address[:-value]
    return address