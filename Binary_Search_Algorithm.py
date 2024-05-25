def binarysearch(ls,element):
    mid =0
    start =0
    end =len(ls)
    step =0

    while(start<=end):
        print("Steps",step,":",str(ls[start:end+1]))
        step = step+1
        mid=(start+end)//2

        if element == ls[mid]:
            return mid
        if element< ls[mid]:
            end = mid-1
        else:
            start = mid + 1

    return -1
ls = [1,2,3,4,5,6,7,8,9]
target = 4
binarysearch(ls,target)
