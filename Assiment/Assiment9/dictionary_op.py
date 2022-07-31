dic={
    input("enter a key:"):input('enter a value')
}

while True:
    print(dic)
    print("1.add a key value","2.find a value","3.get a key:",sep='\n')
    match input('enter a number :'):
        case "1":
            d={input("enter a key:"):input('enter a value')}
            dic.update(d)
        case "2":
            print(dic[input("enter a key:")])
        case "3":
            print(dic.keys())
        case _:
            print("enter a valid number ")