a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))

if a > b:
    print("Katta son:", a)
else:
    print("Katta son:", b)
    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))
a=int(input("1-son"))
b=int(input("2-son"))
c=int(input("3-son"))
d=int(input("4-son"))
if a > b:
    if a > c:
        if a > d:
            print(a)
        else:
            print(d)
    else:
        if c > d:
            print(c)
        else:
            print(d)
else:
    if b > c:
        if b > d:
            print(b)
        else:
            print(d)
    else:
        if c > d:
            print(c)
        else:
            print(d)