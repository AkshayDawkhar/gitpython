standard_input = 1
a=input("enter first number :")
o=input("enter oprater :")
b=input("enter second number :")


match o:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '/':
        print(a/b)
    case '*':
        print(a*b)