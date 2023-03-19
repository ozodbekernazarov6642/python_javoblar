python_a={'intager':"Butun son",
          'string':'Satr',
          'float':"Haqiqiy son",
          'bool':"Mantiq",
          'if':"Agar",
          'else':'Boshqa',
          'del':"O'chirish",
          'remove':"Olib tashlash"
          }
k_soz=input("Kalit so'zni kiriting:")
if  k_soz.lower() in python_a:
    print(f"{k_soz} so'zi {python_a[k_soz.lower()]} deb tarjima qilinadi")
else:
    print("Bunday kalitsoz mavjud emas")