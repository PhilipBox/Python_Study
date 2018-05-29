while True:
    value = input("Enter the Integer [type q to quit]:")
    if value == "q":
        print("End program")
        break
    num = int(value)
    if num%2 == 0: # if even number
        continue
    print(num, "squared is ", num*num)