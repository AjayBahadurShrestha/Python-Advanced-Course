# # Nested try except
#   try:
#     try:
#         try:


#         except:
#     except:
#   except:


try:
    print("Outer try block")

    try:
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        result = num1 / num2
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except ValueError:
        print("Please enter a valid integer.")

except Exception as e:
    print("Outer exception caught:", e)

finally:
    print("Program finished.")