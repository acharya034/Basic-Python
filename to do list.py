list = []
print("Hello World! This is my to do list")
ex = 0
while ex == 0:
    com = int(input("what to do 'add' , 'remove' , 'view' or 'edit' or to close it press other then those key. \n Answer your answer in 1,2,3,4 respectively >> " ))
    if com == 1:
        add = input("what to add >> ")
        list.append(add)
        print(add ," is sucessfuly added to your to do list.")
    elif com == 2:
        edit = input("what to remove >> ")
        if edit not in list:
            print("sorry, i can not find ",edit," can you please try again.")
        else:
            list.remove(edit)
        print(edit ," is sucessfuly added to your to do list.")
    elif com == 3:
        for task in list:
            print(task)  
    elif com == 4:
        edit = input("what to edit >> ")
        add = input("what to add after add >> ")
        if edit not in list:
            print("sorry i can not find ",edit)
        else:
            list.remove(edit)
        list.append(add)
        print(add ," is sucessfuly added after removing ",edit," on to do list.")
    else:
        print("Thank for using")
        ex = 1
