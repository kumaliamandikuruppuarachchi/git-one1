def minimum(*number):
    '''this shows the minimum number'''
    my_list=number
    minimum=my_list[0]
    for i in my_list:
        if i<minimum:
            minimum=i
    return(minimum)

result=minimum(6,8,21,53)
print(result)
   