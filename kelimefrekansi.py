import requests
import operator
from bs4 import BeautifulSoup
def sozlukolustur(tumkelimeler):
   kelimesayisi = {}
   for kelime in tumkelimeler:
      if kelime in kelimesayisi:
         kelimesayisi[kelime] += 1
      else:
         kelimesayisi[kelime] = 1
   return kelimesayisi



def sembolleritemizle(tumkelimeler):
   sembolsuzkelimeler = []
   semboller = "!'^+%&/()<>.,'?""" + chr(775)
   for kelime in tumkelimeler:
      for sembol in semboller:
         if sembol in kelime:
            kelime = kelime.replace(sembol,"")
      if(len(kelime)>0):
         sembolsuzkelimeler.append(kelime)
   return  sembolsuzkelimeler
url ="https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

tumkelimeler=[]
r=requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

for kelimegrupları in soup.find_all("p"):
   içerik = kelimegrupları.text
   kelimeler = içerik.lower().split()


   for kelime in kelimeler:
      tumkelimeler.append(kelime)


tumkelimeler = sembolleritemizle(tumkelimeler)
kelimesayisi = sozlukolustur(tumkelimeler)

for anahtar,deger in sorted(kelimesayisi.items(),key = operator.itemgetter(1)):
   print(anahtar,deger)