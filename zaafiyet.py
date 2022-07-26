import requests
import subprocess
from bs4 import BeautifulSoup

url = input("url giriniz : ")

response = requests.get(url)

print(response)

kütüphane_listesi = list()

html = response.content

icerik = BeautifulSoup(html , "html.parser")

for i in icerik.find_all("script"):

	sonuc = i.get("src")
	if ((sonuc != None) and (".js" in sonuc)):

		a = sonuc.split("/")
		
		for i in a:
			
			if ((i != "..") and (i != "js") and (i != "")):

				kütüphane_listesi.append(i)

print(kütüphane_listesi)

for i in kütüphane_listesi:

	sonuc2 = subprocess.check_output(["searchsploit" , i ])

	with open("sonuc.txt" , "ab" ) as dosya:

		dosya.write(sonuc2)




