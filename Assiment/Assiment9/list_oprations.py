li=input("enter list elements").split(' ')
print(li)
while True:
    print("1.add a element","2.remove a element","3.find length of list","4.sort elements",sep="\n")
    match input("enter the number :"):
        case "1":
            li.append(input("add a element "))
        case "2":
            li.remove(int(input("enter the index :")))
        case "3":
            print(len(li))
        case "4":
            print(li.sort())
        case _:
            print('enter a valid oprater')