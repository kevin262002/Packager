from calc import my_calc

print("Enter 1 for Addition.")
print("Enter 2 for Subtraction.")
print("Enter 3 for Multiplication.")
print("Enter 4 for Division.")
print("Enter 5 for Modulo.")

ch = input("Your Choise : ")

n1 = int(input("Enter 1st Number : "))
n2 = int(input("Enter 2nd Number : "))

if ch == '1':
    print(n1, "+",n2, "=",my_calc.add(n1,n2))

elif ch == '2':
    print(n1, "-",n2, "=",my_calc.sub(n1,n2))

elif ch == '3':
    print(n1, "*",n2, "=",my_calc.multi(n1,n2))

elif ch == '4':
    print(n1, "/",n2, "=",my_calc.division(n1,n2))

elif ch == '5':
    print(n1, "%",n2, "=",my_calc.modulo(n1,n2))

else:
    print("Error...!")
    
