kitoblar=[]
_kitoblar=[]
while kitoblar!='stop':
    kitoblar=input("\nYoqtirgan kitobingizni kiriting:")
    _kitoblar.append(kitoblar)
print("\nSizning yoqtirgan kitoblaringiz:")
for kitob in _kitoblar:
    print(kitob)