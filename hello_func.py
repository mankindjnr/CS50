# we are giving our function hello an argumnet to which will pass to the prototype
# we are passing a default argumnet if the hello function is called without an argumnet
def hello(to="world"):
    print("hello,", to) #saying hello "to" the person we a want to great

name = input("your name big guy: ")

#calling the function without passing an argumnet and it will result to a difault output
hello()

# passing te function hello a parameter name as defined by "to"
hello(name)
