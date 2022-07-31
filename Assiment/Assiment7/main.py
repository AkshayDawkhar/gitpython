number = int(input("Please Enter any Number: "))
print("The List of Natural Numbers from 1 to {0} are".format(number)) 
for i in range(1, number + 1):
    print (i, end = '  ')

n=int(input("enter number: "))
ans=0
for i in range(n+1):
    ans+=i
print("sum of Natural numbers :",ans)

a=int(input("enter a number : "))
print(a,'CUBE',a*a*a)

n=int(input("enter a number: "))
for i in range(1,11):
    print(n*i)

n=int(input("enter a number: "))
on=0;
en=0;
for i in range(n):
    if i%2==0:
        on+=i
    else:
        en+=i
print("sum of even numbers :",on,"sum of odd numbers :",en)

for i in range(5):
    print('* '*i)


for i in range(5):
   for j in range(1,i+1):
    print(j,"",end='')
   print()

for iter in range(5000):
    numb=iter
    temp=numb
    total=0
    while temp>0:
        i=temp%10
        total+=i**3
        temp //= 10
    if total==numb:
        print(numb," is a armstrong number")

n=9
narr=0
for i in range(int(input("enter a number: "))):
    narr+=n
    n*=10
    n+=9
print(narr)

str=input('enter a string : ')
ans=0
for i in str:
    if i.isdigit():
        ans+=int(i)
print(ans)

str=int(input("enter number of inputs:"))
arr=[]
nig,pos=0,0
for i in range(str):
    arr.append(int(input("enter a number ")))
for i in arr:
    if i<0:
        nig+=1
    elif i>0:
        pos+=1
print(nig,"number of nigitive numbers")
print(pos,"number of positive numbers")
print(len(arr)-(nig+pos),"number of zeros")

for num in range(2,201):
    flag = False
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

L=[1,2,3,4]
for i in range(len(L)):
    for j in range(len(L)):
        for k in range(len(L)):
            for m in range(len(L)):
                if (i!=j and j!=k and i!=k and i!=m):
                    print(L[i], L[j], L[k],L[m])


str=input("enter a string :")
up,lp,nu=0,0,0
for i in str:
    if i.isupper():
        up+=1
    elif i.isdigit():
        nu+=1
    elif i.islower():
        lp+=1
print("upper case -",up,"\nlower case -",lp,"\nnumber -",nu)

str=input("enter a string:")
print(str.count(' '))

print(len(input("enter a string:")))

print(len(input("enter a string:").split()))

arr=input('enter a string:').split()
longest  = ''
for word in arr:
    if len(word) > len(longest ):
        longest  = word
shorted =longest 
for word in arr:
    if len(word) < len(longest ):
        shorted  = word
print("longest- ",longest)
print("shortest-",shorted)

strn=input("enter a string :")
strn= strn.replace(" ","")
print(strn)

st=input("enter a word :")
res = [ st[i: j] for i in range(len( st))
          for j in range(i + 1, len( st) + 1)]
print("All substrings of string are : " + str(res))

l=int(input("enter length :"))
r=int(l/2)
for i in range(r):
    for j in range((r-i)+1):
        print('* ',end="")
    if i+1==r:
        for ii in range(r+2):
            for ji in range(ii):
                print('* ',end="")
            print()
    print()
