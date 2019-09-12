first = input("Enter the first number:")
second = input("Enter the second number:")

#while first == str:
method= input("choose the operation (+,-,/,*))")
if method == "+":
        print("The anser is" + (float(first) + float(second)))
elif method == "-":
        print("The anser is" + (float(first) - float (second)))
elif method == "*":
        print("The anser is" + (float(first) * float (second)))
elif method == "/":
        print("The anser is" + (float(first) / float (second)))
else:
        print("invalid entry")