def main():
    x = int(input("what's X? "))
    print("x squared is", square(x)) #we are asking print to output whatever the return value of 
                                    #square is.


def square(n):
    return (n ** 2) #with a return statement - the output of this function can be used in another
                    #function as we are doing in main's print statement. it will return the pow of n
                    #and that output is then accepted by the main function and used

main()