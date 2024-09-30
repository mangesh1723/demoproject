try:
    file=open("abc.txt","r")
    content=file.read()
    print(content)
except Exception as e:
    print(e)
finally:
    if 'file' in locals():
        file.close()
        print("file is closed")    