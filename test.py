# name=input("ENTER NAME: ")
# print(f"hello {name}")


try:
    file_h=open("unkown.txt",'r')
    file_h.read()
    file_h.close()
except OSError as a:
    print(a.strerror)
finally:
    print("finally")    