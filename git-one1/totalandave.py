def total(tot):
    '''this calculates the total'''
    total=0
    totlist=tot.split(',')
    totallist=map(int,totlist)
    for a in totallist:
        total=total+a
    return(total)

def average(ave):
    '''this calculates the average'''
    total=0
    totlist=ave.split(',')
    totallist=map(int,totlist)
    y=list(totallist)
    for a in y:
        total=total+a
    count=len(y)
    average=total/count
    return(average)


total_=total("5,3,2")
print("Total:", total_)

average_=average("5,3,2")
print("Average:", average_)

