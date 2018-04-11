from bson import ObjectId


def serial(dct):
    for k in dct:
        if isinstance(dct[k], ObjectId):
            dct[k] = str(dct[k])   # dct[k] = "some text" if you don't want to show object id else dct[k] = str(dct[k])
    return dct
