print("Let's solve this equation: ax + b = 0")
print("To find the value of x you have to enter the value of a and b.")

while True:

    try:
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))

        if a == 0:
            print("If you put a = 0, The equation has no unique solution.")
            continue

        x = -b / a
        print(f"The value of x is: {x:.2f}")
        break
    except ValueError:
        print("You have to input a numeric number!") 
           
