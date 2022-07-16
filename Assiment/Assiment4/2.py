n=3
a=[None]*n
for i in range(n):
    a[i]=int(input(f"enter {i+1} number :"))
b=0
for i in range(n):
    b+=a[i]
print("Avrage\t-",b/n)
