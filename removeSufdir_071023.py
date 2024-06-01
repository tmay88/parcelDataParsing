def removeSufdir(streetname, sufdir):
    if sufdir is None:
        return streetname
    
    address = " ".join(streetname.split()[:-1])
    return address
