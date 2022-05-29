def Clause(a , b):
    try:
        c = ((a+b) / (a-b))

    except ZeroDivisionError:
        print ("a/b result in 0")

    else:
        print (c)
 
x=float(input("enter 'x':"))
y=float(input("enter 'y':"))
Clause (x , y)