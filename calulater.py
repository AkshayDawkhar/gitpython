
a=int(input("enter first number :"))
o=str(input("enter oprater :"))
b=int(input("enter second number :"))

match o:
    case '+':
        print(f"{a} {o} {b} = {a+b}")
    case '-':
         print(f"{a} {o} {b} = {a-b}")
    case '/':
         print(f"{a} {o} {b} = {a/b}")
    case '*':
         print(f"{a} {o} {b} = {a*b}")
    case _:
        print('please enter valid oprater ')