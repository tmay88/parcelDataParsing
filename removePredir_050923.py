def removePredir(address):
    directionals = {
        'S W ': 4,
        'N W ': 4,
        'S E ': 4,
        'N E ': 4,
        'S ': 2,
        'S.': 2,
        'N ': 2,
        'N.': 2,
        'W ': 2,
        'W.': 2,
        'E ': 2,
        'E.': 2,
        'SW ': 3,
        'NW ': 3,
        'SE ': 3,
        'NE ': 3,
        'SOUTH ': 6,
        'NORTH ': 6,
        'WEST ': 5,
        'EAST ': 5
    }
    for key, value in directionals.items():
        if address.startswith(key):
            return address[value:]
    return address
