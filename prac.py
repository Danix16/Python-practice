while True:
    try:
        num = int(input("Enter a number: "))

        if num > 0:
            print(f"{num} is a Positive number")
        elif num < 0:
            print(f"{num} is a Negative number")
        else:
            print(f"{num} is Zero")

        #input can only be y/Y or n/N to be readable
        restart = input("Restart? (y/n)")
        if restart.lower() != "y": #Specific input(if restart.lower() in ["y", "yes"]:)
            break  #else:
                    #break

    except ValueError:
        print(f"{input} is an Invalid input")