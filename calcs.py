def calcs():
    from app import operation
    if operation == "+" :
        from sum import sum

    elif operation == "-" :
        from subtruct import subtruct

    elif operation == "*" :
        from multiply import multiply
    
    elif operation == "/" :
        from divide import divide
        