# 1-AMALIYOT
def yil_his(ism,yosh):
    print(f"Hurmatli {ism.title()},siz {2023-yosh}-yili tug'ilgansiz!")
ismi=input("Ismingiz nima-")
yoshi=int(input("Yoshingiz nechchida-"))
yil_his(ismi,yoshi)
# 2-AMALIYOT
def daraja(son):
    print(f"{son} ning kvadrati {son**2} ga teng\n"
          f"{son} ning kubi {son**3} ga teng")
son=int(input("Sonni kiriting:"))
daraja(sonlar)
# 3-AMALIYOT
def s_turi(son):
    if son%2==0:
        print(f"{son} juft son!")
    else:
        print(f"{son} toq son!")
son=int(input("Sonni kiriting:"))
s_turi(son)
# 4-AMALIYOT
def taqqoslash(a_son,b_son):
    if a_son > b_son:
        print(a_son)
    elif a_son < b_son:
        print(b_son)
    else:
        print("Sonlar teng")
a_son=int(input("Birinchi sonni kiriting:"))
b_son=int(input("Birinchi sonni kiriting:"))
taqqoslash(a_son,b_son)
# 5-AMALIYOT
def _daraja(x,y):
    print(x**y)
x=int(input("Sonni kiriting:"))
y=int(input("Sonning darajasini kiriting:"))
_daraja(x,y)
# 6-AMALIYOT
def daraja_(x,y=2):
    print(f"{x} ning kvadrati {x**y} ga teng")
x=int(input("Sonni kiriting:"))
daraja_(x)
# 7-AMALIYOT
def b_son(a):
    for i in range(2,11):
        if a%i==0:
            print(F"{a} {i} ga qoldiqsiz bo'linadi!")
a=int(input("Ixtiyoriy son kiriting:"))
b_son(a)