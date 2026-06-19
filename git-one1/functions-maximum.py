def maximum(*number):
    '''this shows the maximum number'''
    my_list=number
    maximum=0
    for i in my_list:
        if i>maximum:
            maximum=i
    return(maximum)

result=maximum(6,8,21,53)
print(result)
   