#Program to show use of global variables in functions.
#creating function for displaying.
def show():
    print("Add: Adds three numbers")
    print("Subtract: Subtracts three numbers")
    print("Multiply: Multiplies three numbers")
#creating a function for accepting choice by user.
def choice():
    return input("A)dd S)ubtract M)ultiply: ")
#creating function for accepting input.
def get_var():
    global val1,val2,val3
    val1 = int(input("first number"))
    val2 = int(input("second number"))
    val3 = int(input("third number"))
def add():
    global ans
    ans=val1+val2+val3
def subtract():
    global ans
    ans=val1-val2-val3
def multiply():
    global ans
    ans=val1*val2*val3
def output():
    print("The total: is : ",ans)

#Creating the main function
def main():
    show()
    userchoice=choice()
    if userchoice== "A" or userchoice =="a":
        get_var()
        add()
        output()
    elif userchoice== "S" or userchoice =="s":
        get_var()
        subtract()
        output()
    elif userchoice== "M" or userchoice =="m":
        get_var()
        multiply()
        output()
    else:
        print("invalid choice.")
main()
    
    

    
    