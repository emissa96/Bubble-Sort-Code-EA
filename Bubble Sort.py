def shortBubbleSort (blist):
    swap = True
    passnum = len(blist)-1
    while passnum > 0 and swap:
        swap = False
        for i in range(passnum):
            if blist[i]>blist[i+1]:
                swap = True
                temp = blist[i]
                blist[i] = blist[i+1]
                blist[i+1] = temp
        passnum = passnum -1
blist=[30,30,40,90,50,60,70,80,100,110]
shortBubbleSort(blist)
print(blist)