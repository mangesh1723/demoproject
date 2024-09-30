try:
    file=open("abc.txt","w")
    file.write("Hellow, This is aura of mr_king")
except Exception as e:
    print(e)
finally:
    if 'file' in locals():
        file.close()
        print("file is closed")