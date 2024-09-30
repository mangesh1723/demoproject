class NegNumError(Exception):
    pass
def checkposno(num):
    if num<0:
        raise NegNumError("negative numbers are not allowed")
try:
    num=int(input("enter a number"))
    checkposno(num)
except NegNumError as e:
   print(e)
   