def malumot(ism,familya,t_yil,t_joy,e_manzil='',t_raqam=''):
    t_hol={
        'ismi':ism,
        'familyasi':familya,
        't_yili':t_yil,
        't_joyi':t_joy,
        'e_manzil':e_manzil,
        't_raqam':t_raqam
    }
    return t_hol
info=[]
print("Do'stingiz haqida ma'lumot to'playdigan dastur\n")
while True:
    ismi=input("Ismini kiriting:")
    familyasi=input("\nFamilyasini kiriting:")
    t_yili=(input("\nTug'ilgan yili:"))
    t_joyi=input("\nTug'ilgan joyi:")
    e_manzil=input("\nE-manzili (ixtiyoriy):")
    t_raqami=(input("\nTelefon raqami (ixtiyoriy):"))
    info.append(malumot(ismi, familyasi, t_yili, t_joyi, e_manzil, t_raqami))
    mal=input("\nYana do'st qo'shasizmi (ha/yo'q):")
    if mal!='ha':
        break
for infolar in info:
    if infolar['e_manzil']!='' and infolar['t_raqam']!='':
        print(F"Ismi-{infolar['ismi'].title()}\n"
              F"Familyasi-{infolar['familyasi'].title()}\n"
              F"Tug'ilgan yili-{infolar['t_yili']}\n"
              F"Tug'ilgan jo'yi-{infolar['t_joyi'].title()}\n"
              F"Telefon raqami-{infolar['t_raqam']}\n"
              F"E-manzili-{infolar['e_manzil'].lower()}")
    elif infolar['e_manzil']=='' and infolar['t_raqam']=='':
        print(F"Ismi-{infolar['ismi'].title()}\n"
              F"Familyasi-{infolar['familyasi']}\n"
              F"Tug'ilgan yili-{infolar['t_yili']}\n"
              F"Tug'ilgan jo'yi-{infolar['t_joyi'].title()}\n")
    elif not(infolar['e_manzil']):
        print(F"Ismi-{infolar['ismi'].title()}\n"
              F"Familyasi-{infolar['familyasi'].title()}\n"
              F"Tug'ilgan yili-{infolar['t_yili']}\n"
              F"Tug'ilgan jo'yi-{infolar['t_joyi'].title()}\n"
              F"Telefon raqami-{infolar['t_raqam']}\n")
    elif not(infolar['t_raqam']):
        print(F"Ismi-{infolar['ismi'].title()}\n"
              F"Familyasi-{infolar['familyasi'].title()}\n"
              F"Tug'ilgan yili-{infolar['t_yili']}\n"
              F"Tug'ilgan jo'yi-{infolar['t_joyi'].title()}\n"
              F"E-manzili-{infolar['e_manzil'].lower()}\n")