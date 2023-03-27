def calcs(a , b , operation):
#from func_tools.sum import sum
#from func_tools.subtruct import subtract
#from func_tools.multiply import multiply
#from func_tools.divide import divide


#    from app import operation
#    if operation == "+" :
#        from func_tools.sum import sum
#    elif operation == "-" :
#       from subtruct import subtruct
#    elif operation == "*" :
#        from multiply import multiply 
#    elif operation == "/" :
#        from divide import divide

    from app import operation
    from app import a
    from app import b

    if operation == "+":
        from func_tools.sum import sum
        resalt = sum
        print (resalt)
    
    