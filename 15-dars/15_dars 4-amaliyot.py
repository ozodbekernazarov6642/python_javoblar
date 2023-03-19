r_taom={'osh':25000,
        'sho\'rva':22000,
        'lavash':20000,
        'somsa':7000,
        'burger':30000,
        'salat':12000,
        'non':5000,
        'choy':3000,
        'coffe':18000
        }
t_nomi=[]
print("3ta taom buyurtma bering")
for i in range(3):
        t_nomi.append(input(f'{i+1}-taom:').lower())
for i in range(3):
        if t_nomi[i] in r_taom.keys():
                print(f"{t_nomi[i].title()} {r_taom[t_nomi[i]]} so'm")
        else:
                print(f"Bizda {t_nomi[i].title()} yo'q")
