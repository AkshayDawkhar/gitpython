
# from cmath import pi
from formula import circle, rectangle, square, trangle

# print("find area of-","square","rectangle","circle","trangle","exit",sep='\n')
# while True:
#  match input('enter name of sape :'):
#     case "square":
#         print(float(input("enter side -"))*4,)
#     case "rectangle":
#         print(float(input("enter hight  -"))*float(input("enter width - ")))
#     case "trangle":
#         print(0.5*(float(input("enter base -"))*float(input("enter hight -"))))
#     case "circle":
#         r=float(input("enter radius -"))
#         print(pi*(r*r))
#     case "exit":
#         break
#     case _:
#         print("Enter valid number ")

print("find area of-","square","rectangle","circle","trangle","exit",sep='\n')
while True:
 match input('enter name of sape :'):
    case "square":
        print(square(float(input("enter side -"))))
    case "rectangle":
        print(rectangle(float(input("enter hight  -")),float(input("enter width - "))))
    case "trangle":
        print(trangle(float(input("enter base -")),float(input("enter hight -"))))
    case "circle":
        print(circle(float(input("enter radius -"))))
    case "exit":
        break
    case _:
        print("Enter valid number ")