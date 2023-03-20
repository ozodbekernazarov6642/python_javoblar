e_bozor={
    'miller':1000,
    'zi zi':500,
    'sityx':3000,
    "o'rbit":7000,
    'ruchka':4000,
    'un':8000,
    'shakar':18000,
    'olma':15000,
    'banan':20000,
    'makaron':12000,
}
mah=list(map(str,input("Mahsulotlar kiriting:").lower().split()))
while mah:
    mahsulot=mah.pop()
    if mahsulot in e_bozor:
        print(f"{mahsulot} narhi {e_bozor[mahsulot]} so'm")
    else:
        print(f"Bizda {mahsulot.title()} yo'q")