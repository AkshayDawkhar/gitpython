li=[1,2,1,2]
li.append(12)
print(li,)
li.clear()
print(li,)
li.extend("akshay")
print(li)

i=[1,2,1,2]
s=set(i)
print(s)

li=[]
for i in range(11):
    li.append(i*i*i)

import collections
ist = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
frequency = collections.Counter(ist)
print(dict(frequency))

t=('a','b','c')
print(t)
print(t.index('c'),t.count('c'))

li=[12,13]
lii=[1,2,3]
s=set(li+lii)
print(s)

st=str(s)
l=list(s)

x = (2, 4, 6)
result = reversed(x)
result = tuple(result)
print(result)

dic={
    "name":"akshay",
    "id":1234567
}
print(dic.values())
print(dic.keys())
print(dic.get('name'))

dic={
    "name":"akshay",
    "id":1234567
}
dic1={
    "name1":"akshay",
    "id1":1234567
}
dic2={
    "name2":"akshay",
    "id2":1234567
}
dic.update(dic1)
print(dic)
dic3={**dic,**dic1,**dic2}
print(dic3)

dic={}
for i in range(1,int(input("enter a number :"))):
    d={i:i*i*i}
    dic.update(d)
print(dic)

dic={'value1':1,'value2':2,'value3':3,'value4':4,'value5':5,'value6':6,'value7':7,'value8':8,'value9':9,}
ans=1
for i in dic:
    ans*=dic[i]
#
print(len(dic.values()))
#
key_max = max(dic.keys(), key=(lambda k: dic[k]))
key_min = min(dic.keys(), key=(lambda k: dic[k]))
print('Maximum Value: ',dic[key_max])
print('Minimum Value: ',dic[key_min])

arr=[1,2,3,4,5,6]
arr=["1","2","3","4","5","6"]
dic={}
for i in range(len(arr)):
    d={arr[i]:int(arr[i])}
    dic.update(d)

s={12,21,13}
print(s)
s.clear()
print(s)
s.add(12)
print(s)
s.pop()

s=set()
s1=set()
for i in range(10,41):
    s.add(i)
for i in range(20,61):
    s1.add(i)
print(s.difference(s1))
print(s1.difference(s))

s={12,13,14}
s1={34,14,15}
print(s.isdisjoint(s1))

l=[1,2,3]
t=(12,13,14)
s=set(l)
d={1:12,2:32}
print('\tlist','tupe','set','Dictionary',sep='\t\t')
print("list",list(l),tuple(l),set(l),"X",sep="\t")
print("tuple",list(t),tuple(t),set(t),"x",sep="\t")
print("set",list(s),tuple(s),set(s),"X",sep="\t")
print("Dict",list(d),tuple(d),set(d),dict(d),sep="  \t")
