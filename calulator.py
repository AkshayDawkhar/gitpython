
#meathod 1 
str='123-2+39-12+12*12+98+98+2'
incial=0
oprand=[]
oprater=[]
for i in range(len(str)):
 if str[i]=='+' or str[i]=='-' or str[i]=='/' or str[i]=='*':
    oprater.append(str[i])
    oprand.append(int(str[incial:i]))
    incial=i+1
 if  i+1== len(str):
    oprand.append(int(str[incial:i+1]))
ans=oprand[0]

for i in range(len(oprater)):

 match oprater[i]:
    case '+': 
        ans+=oprand[i+1]
    case '-': 
        ans-=oprand[i+1]
    case '/': 
        ans/=oprand[i+1]
    case '*': 
        ans*=oprand[i+1]
print(ans)

#meathod 2

'''''
ans=0
o=0
o2=None
o1=None
incial=0
oprand=[]
oprater=[]
for i in range(len(str)):
 if str[i]=='+' or str[i]=='-' or str[i]=='/' or str[i]=='*':
    oprater.append(str[i])
    o=str[i]
    oprand.append(int(str[incial:i]))
    if o1== None: o1=int(str[incial:i])
    else:
        o2=int(str[incial:i])
        print(o1+o2)
        match o:
         case '+': 
           print(o1+o2)
           o1+=o2
         case '-': 
          print(o1-o2)
          o1-=o2
         case '/': 
           print(o1/o2)
           o1/=o2
         case '*': 
           print(o1*o2)
           o1*=o2
        
    incial=i+1
 if  i+1== len(str):
    oprand.append(int(str[incial:i+1]))
   #  o1=int(str[incial:i+1])
   #  o2=int(str[incial:i])
    print(o1+o2)
    match o:
     case '+': 
      print(o1+o2)
      o1+=o2
     case '-': 
      print(o1-o2)
      o1-=o2
     case '/': 
      print(o1/o2)
      o1/=o2
     case '*': 
      print(o1*o2)
      o1*=o2
 
ans=oprand[0]'''


#meathod 3
# print(eval(str))
