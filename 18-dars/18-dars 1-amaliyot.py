menyu={}
narh=[]
n=1
qiymat=True
while qiymat:
    mahsulot=input(f"{n}-mahsulot nomi:")
    narh=int(input(f"{mahsulot.title()}ni narhini kiriting:"))
    menyu[mahsulot]=narh
    n+=1
    mal=input("Yana ma'lumot qo'shasizmi (ha/yo'q):")
    if mal.lower()!='ha':
        qiymat=False
print("\nRestaran menyusi:")
for mah,narh in menyu.items():
    print(f"{mah}ning narhi {narh} so'm")