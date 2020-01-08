def BubbleSort(alist):
    """
    Sorts a collection using bubble sort.
    :param alist: A list
    :return: A sorted list using bubble sort
    """
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
    return alist


