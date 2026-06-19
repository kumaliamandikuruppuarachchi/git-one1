x=(10,25,15,8)
set_x=set(x)
target=18
for i in x:
    y=target-i
    if y in x:
        print(i,y)
        break
        set_x.remove(i)
