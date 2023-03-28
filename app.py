is_running = True

while is_running :
    user_choose = input("Do you want to work wich calc? y / n : ")

    if user_choose == "y" :
        operation = input("What math operation do you want to perform - '+' , '-' , '*' , '/' , '^' ? ")
        if operation in ("+-*/^"):
            try:
                a = int(input("Enter first number : "))
                b = int(input("Enter second number : "))
        
      
                if operation == "+":
                    from func_tools.sum import sum
                    resalt = sum(a , b)
                    print(a , "+" , b , "=" , resalt)

                if operation == "-":
                    from func_tools.subtruct import subtract
                    resalt = subtract(a , b)
                    print(a , "-" , b , "=" , resalt)
                if operation == "*":
                    from func_tools.multiply import multiply
                    resalt = multiply(a , b)
                    print(a , "*" , b , "=" , resalt)
                if operation == "/":
                    from func_tools.divide import divide
                    resalt = divide(a , b)
                    print(a , "/" , b , "=" , resalt)
                if operation == "^":
                    from func_tools.square import square
                    from func_tools.degree import degree
                    resalt_a = square(a , 2)
                    resalt_b = square(b , 2)
                    resalt = degree(a, b)
                    print(a , "^2" , "=" , resalt_a)
                    print(b , "^2" , "=" , resalt_b)
                    print(a , "^" , b , "=" , resalt)

            except ValueError:
                print("Wrong namber")

            except NameError:
                print("Wrong namber")
        
        else:
            continue
     
    elif user_choose == "n" :
        is_running = False
    else :
        continue