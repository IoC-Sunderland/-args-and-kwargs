# *args enables arbitary number of arguments to a function
def args(*args):
    return type(args), args

# **kwargs enables arbitary number of keyword arguments to a function
def kwargs(**kwargs):
    return type(kwargs), kwargs

print(args(1,2,3,"Four","Five"))
print(kwargs(name="Gav", age=21))
