a = input()
b = input()
c = input()
d = input()

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
ismlar= ["Ali", "Vali", "Diyor","Elbek","Laziz","Asadbek","Bobur","Shahob","Jonibek","Eldor"]
print(ismlar)
for  i in ismlar:
    print(i,"oshga kel")





