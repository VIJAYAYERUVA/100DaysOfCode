def ArrayChallenge(strArr):
    mytup = [eval(t) for t in strArr]
    i2List = []
    for i1, i2 in mytup:
        i2List.append(i2)
    i2Set = set(i2List)

    i2Dic = {(i, i2List.count(i)) for i in i2Set}

    for key, value in i2Dic:
        if value > 2:
            return 'false'
        else:
            return 'true'

    # code goes here
    return strArr


# keep this function call here
print(ArrayChallenge(input()))
