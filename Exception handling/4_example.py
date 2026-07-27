
print("Hello world")
try:
    print(10/5)
    a= 5+"AJay"
except ZeroDivisionError as msg:
    print(10/2)
except ValueError as msg:
    print("Value error Handles..")
except TypeError as msg:
    print("Type error Handles..")
finally:
    print("Clean up the code..")
print("LBEF")
