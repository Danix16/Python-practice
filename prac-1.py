while True:
    a = input("Enter a word: ").lower()
    text = ("This is a group of words").lower()
    if a.isdigit():
        print(f"'{a}' is invalid")
    else:
        if a in text:
            print(f"Yes, '{a}' exists")
        else:
            print(f"No, '{a}' does not exist")
            
    cont = input("Exit? Yes or No?").lower()
    if cont == 'yes':
        print("Exiting...")
        break
    else:
        print("Continuing...")

