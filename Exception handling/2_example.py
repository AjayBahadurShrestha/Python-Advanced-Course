
print("Hello world")
try:
    print(10/5)
    a= 5+"AJay"
except Exception as msg:
    print(10/2)
except ValueError as msg:
    print("Value error Handles..")
except:
    print("Unknown error handled..")
print("LBEF")
