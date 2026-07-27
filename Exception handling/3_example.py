
print("Hello world")
try:
    print(10/5)
    a= 5+"AJay"
except (Exception,ValueError, TypeError) as msg:
    print(f"Occures Exception Handled: {msg}")

except:
    print("Unknown error handled..")
print("LBEF")
