def mydecorator(fun):
    def myfun():
        print("something bofore function")
        fun()#original function
        print("after function")
    return myfun
@mydecorator
def say():
    print("hellow")
say()    
        



