try:
    num=int(input("enter a number:"))
    result=10/num
except (ZeroDivisionError,ValueError,TypeError,IOError) as e:
    print(e)
