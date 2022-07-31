s=set(input("enter the elemetns : ").split(' '))
while True:
    print(s)
    print("1.add","2.remove","3.clear",sep='\n')
    match input('enter a number :'):
        case "1":
            s.add(input("enter the elemetns : "))
        case "2":
            s.remove(input("enter the elemet : "))
        case "3":
            s.clear()
        case _:
            print("enter a valid number ")