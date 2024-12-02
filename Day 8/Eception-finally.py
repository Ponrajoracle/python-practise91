try:

    print(val)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("This is always executed")
