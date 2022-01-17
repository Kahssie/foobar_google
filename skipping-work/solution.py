def solution(x, y):
    # Your code here: use dicts
    
    # convert array to dict for lower search time
    dictX = dict() 
    dictY = dict()
    
    for element_X in x:
        idx_X = x.index(element_X)
        dictX[element_X] = idx_X
    for element_Y in y:
        idx_Y = y.index(element_Y)
        dictY[element_Y] = idx_Y
    
    lenX = len(x)
    lenY = len(y)
    
    if (lenX>lenY):
        for element_X in x:
            if element_X not in dictY:
                print(element_X)
                return element_X
    elif (lenX<lenY):
        for element_Y in y:
            if element_Y not in dictX:
                print(element_Y)
                return element_Y
    else:
        print("nothing returned")
        return None
    
    
if __name__ == "__main__":
    x = [13, 5, 6, 2, 5]
    y = [5, 2, 5, 13]
    print(solution(x,y))