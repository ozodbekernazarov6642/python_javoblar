davlatlar={
    "O'zbekiston":{'p_nomi':"Toshkent",
                   'hudud':449978,
                   'Aholisi':36000000,
                   'p_birligi':"so'm"
                   },
    'Rossiya':{
        'p_nomi':"Moskova",
        'hudud':17098246,
        'Aholisi':144000000,
        'p_birligi':"rubl"
    },
    "Aqsh":{
        'p_nomi':"Washington D.C",
        'hudud':9631418,
        'Aholisi':327000000,
        'p_birligi':"dollar"
    },
    'Malaziya':{
        'p_nomi':"Kuala-Lumpur",
        'hudud':329750,
        'Aholisi':25000000,
        'p_birligi':"rangit"
    }
}
davlat=input("Davlat nomini kiriting:")
for d_nom, v_davlat in davlatlar.items():
    if davlat.lower()==d_nom.lower():
        print(F"{d_nom.upper()}ning poytaxti {v_davlat['p_nomi']} shahri\n"
              F"Hududi-{v_davlat['hudud']} km kv\n"
              F"Aholisi-{v_davlat['Aholisi']} kishi\n"
              F"Pul birligi-{v_davlat['p_birligi']}\n")
else:
    print("Bu davlat haqida ma'lumot yo'q")