davlat_p={'Uzbekiston':"Toshkent",
          'AQSH':"Washington D.C",
          'Qozog\'iston':"Astana",
          'Turkiya':"Anqara",
          'Buyuk Biritaniya':"London",
          'Rossiya':"Maskova",
          'Germanya':"Berlin"
          }
print("Dunyo davlatlari")
for key in sorted(davlat_p.keys()):
    print(key)
print("Dunyolarning poytaxti")
for value in davlat_p.values():
    print(value)