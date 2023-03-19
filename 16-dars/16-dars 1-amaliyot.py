alisher_n={'ismi':"Alisher Navoiy",
           't_joyi':"Hirotda",
           'n_tugilgani':1441,
           'y_yili':60
           }
i_gaspirali={'ismi':"Ismail Gaspirali",
             't_joyi':"Qatar",
             'n_tugilgani':1851,
             'y_yili':63
             }

m_shaxslar=[alisher_n,i_gaspirali]
for b_shaxslar in m_shaxslar:
    print(f"{b_shaxslar['ismi']} {b_shaxslar['n_tugilgani']}-yili {b_shaxslar['t_joyi']}da tug'ilgan.{b_shaxslar['y_yili']}-yil yashagan")