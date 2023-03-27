is_running = True

while is_running :
    user_choose = input("Do you want to work wich calc? y / n : ")

    if user_choose == "y" :
        operation = input("What math operation do you want to perform - '+' , '-' , '*' , '/' , '^' ? ")
        if operation in "+-*/^":
            from calcs import calcs
            print 
        else: 
            continue
    
    elif user_choose == "n" :
        is_running = False
    else :
        continue