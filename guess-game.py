import random
three_digit = random.randrange(100, 999)
tries = 10
while tries >0 and tries <=10 :
    user_input = input("Enter three digit number: ")

    if len(user_input) == 3:
        tries = tries - 1
        if int(user_input) == three_digit:
            print("Correct guess")
            break
        else:
            print("Wrong guess", "tries left-", tries)
            for x in list(user_input):
                for y in str(three_digit):
                    print(x, y)
                    # print("Hint : interchange the values of x and y")
                    # if x[0] == y[0]:
                    # if x[1] == y[1]: 

    else:
        print(f"Enter three digit no {len(user_input)}")
        print("tries left-", tries)
        if tries == 0:
            print("guess over", "correct no-", three_digit)    
