s=input("enter a string :")
while(True):
    print("1.add a string","2.find the length of string","3.get a sub-string","4.get deitis ","5.change the string",sep="\n")
    match input("enter a number "):
        case "1":
            s+=input("add :")
        case "2":
            print(len(s))
        case "3":
            (a,b)=(int,input("enter indexs :").split(' '))
            print(s[a:b])
        case "4":
            up,lp,nu=0,0,0
            for i in s:
                if i.isupper():
                    up+=1
                elif i.isdigit():
                    nu+=1
                elif i.islower():
                    lp+=1
            print("upper case -",up,"\nlower case -",lp,"\nnumber -",nu)
        case "5":
            s=input('enter a new string :')
        case _:
            print("enter a valid number")


