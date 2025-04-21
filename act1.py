def shutdown():
    input2 = input("Have you closed all apps?")
    input2 = input("Have you logged off your account?")
    if(input == "yes" and input2 == "yes"):
        print("shutting down")
    elif (input == "no" or input2 == "no"):
        print("almost shut down")
    else:
        print("sorry")