def k_harf(katta_harf):
    ismlar=[]
    for ism in katta_harf:
        ismlar.append(ism.title())
    return ismlar
_ismlar = ['ali', 'vali', 'hasan', 'husan']
print(_ismlar)
print(k_harf(_ismlar[:]))