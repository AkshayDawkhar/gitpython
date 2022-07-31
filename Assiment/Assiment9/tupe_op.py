t=tuple(input('enter the elements : ').split(' '))
print(t)
while True:
    print("1.find index","2.find cout ","3.reassinge tuple",sep='\n')
    match input("enter a number : "):
        case "1":
            print(t.index(input('enter a element :')))
        case "2":
            print(t.count(input("enter a element :")))
        case "3":
            t=tuple(input('enter new elements :').split(' '))
        case _:
            print("enter a valid number ")