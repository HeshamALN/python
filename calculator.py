first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))

#while first == str:
method= input("choose the operation (+,-,*,/))")
if method == "+":
        result = first + second
        print("The anser is " + str(result))
elif method == "-":
        result = first - second
        print("The anser is " + str(result))
elif method == "*":
        result = first * second
        print("The anser is " + str(result))
elif method == "/":
        result = first / second
        print("The anser is " + str(result))
else:
        print("invalid entry")