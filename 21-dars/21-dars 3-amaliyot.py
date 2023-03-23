def bahola(ism):
    baholar= {}
    for ismlar in ism:
        baho=(input(F"{ismlar.title()}ning bahosini kiriting:"))
        baholar[ismlar]=baho
    return baholar
ismlar = ['ali', 'vali', 'hasan', 'husan']
baholar=bahola(ismlar)
print(baholar)
print(ismlar)