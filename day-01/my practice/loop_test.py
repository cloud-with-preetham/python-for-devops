for i in range(3):
    env = input("Enter the Environment: ")  # Taking input from the user

    print("The user input environment is:", env)

    # Conditional statemnet simple if else

    # == != > < >= <=
    if env == "prod":  # True or False
        print("Don't Deploy on Friday")
    elif env == "staging":  # True or False
        print("Take backup and proceed testing")
    else:  # False
        print("Safe to deploy any day...!")
