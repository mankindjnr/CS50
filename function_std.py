def main():
    name = input("What's your name? ")
    hello(name)

# this function just prints an output but we can modify it to return a value to us using return
# in calculator_func.py we implment this value
def hello(to="world"):
    print("hello,", to)

# call main function so as to go back and call main, which will then call hello
main()