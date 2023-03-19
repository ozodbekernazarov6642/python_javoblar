davlat_p={'Uzbekiston':"Toshkent",
          'Aqsh':"Washington D.C",
          'Qozog\'iston':"Astana",
          'Turkiya':"Anqara",
          'Buyuk Biritaniya':"London",
          'Rossiya':"Maskova",
          'Germanya':"Berlin"
          }
davlat_n=input("Istagan Davlatingizni kiriting:")
mal=davlat_p.get(davlat_n.title())
if mal!=None:
    print(f"{davlat_n.upper()}ning poytaxti {davlat_p[davlat_n.title()]} shahri")
else:
    print("Bizda bunaqa ma'lumot yo'q")