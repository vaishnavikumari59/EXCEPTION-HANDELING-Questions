def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
a=int(input("enter 'a':"))
b=int(input("enter 'b':"))
divide(a, b)