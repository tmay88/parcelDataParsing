def removeStreetType(address, streetType):
    if streetType is None:
        return address
    else:
        splitAddress = address.rsplit(' ', 1)
        return splitAddress[0]