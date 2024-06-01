def fullAddressConcat(housenum, predir, street, ptype, stype, sufdir):
    address = [housenum, predir, street, ptype, stype, sufdir]
    updatedAddress = [value if value is not None else '' for value in address]
    fulladdress = ' '.join(updatedAddress).replace('  ', ' ').strip()
    return fulladdress if fulladdress != '' else None
    
    
#fullAddressConcat(!housenum!, !predir!, !streetname!, !pretype!, !streettype!, !sufdir!)


def fulladdnad(addnum, predir, pretype, streetname, postype, posdir):
    address = [addnum, predir, pretype, streetname, postype, posdir]
    updatedAddress = [value if value is not None else '' for value in address]
    fulladdress = ' '.join(updatedAddress).replace('  ', ' ').strip()
    return fulladdress if fulladdress != '' else None

#fulladdnad(!Add_Number!, !StN_PreDir!, !StN_PreTyp!, !StreetName!, !StN_PosTyp!, !StN_PosDir!)

def splitAddCo(AddNum, StPreDir, StPreType, StName, StType, StDir, UnitType, UnitName, BuildingType, BuildingUnit):
    address = [AddNum, StPreDir, StPreType, StName, StType, StDir, UnitType, UnitName, BuildingType, BuildingUnit]
    updatedAddress = [value if value is not None else '' for value in address]
    fulladdress = ' '.join(updatedAddress)
    return fulladdress if fulladdress != '' else None   

#splitAddCo(!AddNum!, !StPreDir!, !StPreType!, !StName!, !StType!, !StDir!, !UnitType!, !UnitName!, !BuildingType!, !BuildingUnit!)
