# 1-AMALIYOT
def kopaytma(*sonlar):
    kopaytma_=1
    for _son in sonlar:
        kopaytma_*=_son
    return kopaytma_
print(kopaytma(2,3,5,6,8))
# 2-AMALIYOT
def malumot(ism,familya,**malumotlar):
    malumotlar['ism']=ism
    malumotlar['familya']=familya
    return malumotlar
print(malumot("Ozodbek","Ernazarov",tugilgan_yil="2007",tugilgan_joy="Sirdaryo",yoshi=16))