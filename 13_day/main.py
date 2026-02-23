def greet(x):
    def fx(*args,**fwargs):
        print("Good Morning")
        x(*args,**fwargs)
        print("Thanks for using this function")
    return fx
@greet
def sum(a,b):
   print(a+b)
sum(1,2)