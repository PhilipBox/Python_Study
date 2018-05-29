while True:
    stuff = input("String to capitalize [type q to quit]:")
    if stuff == "q":
        print("End program")
        break
    print(stuff.capitalize())