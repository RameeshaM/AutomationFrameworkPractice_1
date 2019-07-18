import inspect

def whoami():
    return inspect.stack()[1][3]

def Myfunc():
    x= whoami()
    print(x)

Myfunc()


