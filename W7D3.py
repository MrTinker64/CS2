def selectionSort(listIn: list):
    try:
        if len(listIn) < 2:
            return listIn
        else:
            return [earliestOrSmallestIn(listIn)] + selectionSort(allButItemOfList(earliestOrSmallestIn(listIn), listIn))
    except TypeError:
        return []
    
def earliestOrSmallestIn(listIn: list):
    if len(listIn) < 2:
        return ''.join(listIn)
    if listIn[0][0] < listIn[1][0]:
        return earliestOrSmallestIn([listIn[0]] + allButItemOfList(listIn[1], listIn[1:]))
    else:
        return earliestOrSmallestIn(listIn[1:])

def allButItemOfList(item, listIn: list):
    for i in listIn:
        if item == i:
            listIn.remove(i)
            return listIn


print(selectionSort(['a', 'c', 'b']))