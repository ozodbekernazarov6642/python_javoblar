dost1={
    "Otabek":[
        "To'r3",
        "Birinchi Qasoskor",
        "Alhazar"
    ],
          'Samir':[
        "Himoyachi",
        "Chumoli odam 3",
        "Qora pantera",
        "Wensday"
    ],
          "Kamron":[
        "Qora liboslilar",
        "Jinoyat izi"
    ]
}
for dost_k,dost_v in dost1.items():
    print(f"\n{dost_k}ning sevimli kinolari:")
    for dost1_v in dost_v:
        print(dost1_v.upper())
