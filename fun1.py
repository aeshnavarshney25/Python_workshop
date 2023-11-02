def my_function():
    x=10                  #x is a local variable
    print(x)
my_function()



x=10                     #x is a global variable
def my_function():
    print(x)             # accessing the global variable
my_function()


x=10
def modify_global():
    global x
    x=20
    