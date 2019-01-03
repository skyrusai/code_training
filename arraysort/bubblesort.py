
def bubblesort(arr):
    """
    基本思想：在要排序的一组数中，对当前还未排好序的范围内的全部数，
    自上而下对相邻的两个数依次进行比较和调整，让较大的数往下沉，较小的往上冒。
    即：每当两相邻的数比较后发现它们的排序与排序要求相反时，就将它们互换。
    implementation of bubble sort
    """
    length=len(arr)
    unsorted=True 
    kk=0  #类似j
    while unsorted:
        unsorted=False
        i=0
        while i<length-1-kk:
            if arr[i]>arr[i+1]:
                unsorted=True
                arr[i],arr[i+1]=arr[i+1],arr[i]
            i+=1        
        kk+=1
    return arr
