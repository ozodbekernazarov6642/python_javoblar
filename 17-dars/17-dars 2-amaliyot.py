qiymat=True
while qiymat:
    yosh = input("Yoshingiz nechchida:").lower()
    if yosh == 'exit' or yosh=='quit':
        qiymat = False
    elif int(yosh)<=7:
        print("Sizning bilet narxingiz 2000 so'm")
    elif int(yosh)>7 and int(yosh)<18:
        print("Sizning bilet narxingiz 3000 so'm")
    elif int(yosh)>=18 and int(yosh)<65:
        print("Sizning bilet narxingiz 10000 so'm")
    else:
        print("Sizga bilet bepul")
print("Xayr")