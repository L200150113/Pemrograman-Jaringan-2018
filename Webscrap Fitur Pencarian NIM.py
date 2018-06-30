import urllib3
from bs4 import BeautifulSoup as bs
from tabulate import tabulate
import re

print ("Pencarian Data Forlap Mahasiswa Informatika Semester Ganjil 2017")
print ("Hanya NIM yang terdaftar tahun ajaran 2017 termasuk data ini")

nim = input("Masukkan NIM anda(tambahkan tanda petik) : ")
http = urllib3.PoolManager()
def_link = "https://forlap.ristekdikti.go.id/mahasiswa/detailsemester/RUVDMDAxMkEtMEU2Qy00MjY3LTk1RjYtREUxQkE2NzVDOEI1/20171/"
page = 0
data_full = [["\tNo", "\tNIM", "\tNAMA", "\tLINK"]]
urllib3.disable_warnings()
print ("Mendapatkan Data")
for i in range(50):
	full_link = def_link+str(page)

	l = http.request('GET',full_link)
	if l.status == 200:
		s = bs(l.data,"html.parser")
		T2 = s.select("table")[0]
		data =[]
		link = []
		for i in range(len(T2.select("tr"))):
			data.append([])
		for i in range(len(T2.select("tr"))):
			link.append([])
		for th in range(len(T2.select("tr")[0].select("th"))):
			 data[0].append(T2.select("tr")[0].select("th")[th].string)
		for row in range(1,len(T2.select("tr"))):
			for isi in range(len(T2.select("tr")[1].select("td"))):
				link[row].append((T2.select("tr")[row].find("a").get("href")))
				data[row].append(T2.select("tr")[row].select("td")[isi].string.strip())
		data[0].append("Link")
		for i in range (1,len(data)):
			data[i].append(link[i][0])
		for i in range(1,len(data)):
			data_full.append(data[i])
	page = page+20		
		
		

	link.pop()
# print (tabulate(data_full))

def cari(nim):
	for i in range(len(data_full)):
		if data_full[i][1] == nim:
			return data_full[i][3]

def data_forlap(link_forlap):
	import urllib3
	from bs4 import BeautifulSoup as bs
	from tabulate import tabulate
	http = urllib3.PoolManager()
	urllib3.disable_warnings()
	l = http.request('GET',link_forlap)
	# print (l.status)
	if l.status == 200:
		print ("Getting Data")
		print ("clear")
		# Data Table 1 Profil
		s = bs(l.data,'html.parser')
		datat1_kiri = []
		datat1_kanan = []
		datat1 = []
		T1 = s.select('table')[0]
		for i in range(9):
			datat1.append([])
			if i != 2:
				for j in range(3):
					datat1[i].append(T1.select('tr')[i].select('td')[j].string.strip())
		print("\n\n\n\tProfil Data Mahasiswa")
		print (tabulate(datat1))

		# Data Table 2 Riwayat Status Kuliah
		print ('\n\tRiwayat Status Kuliah')
		T2 = s.select('table')[1]
		datat2 = []
		for i in range(len(T2.select('tr'))):
			datat2.append([]) ##Untuk membuat list kosong dengan jumlah array sesuai dengan isi tr
		for th in range(len(T2.select('tr')[0].select('th'))): ##Mengambil data TH
			datat2[0].append(T2.select('tr')[0].select('th')[th].string)
		for i in range(1, len(T2.select('tr'))): ##Mengulang dari 1 hingga jumlah table, untuk mengambil isi semua td
			for isi in range(len(T2.select('tr')[1].select('td'))):
				datat2[i].append(T2.select('tr')[i].select('td')[isi].string.strip())
		
		print (tabulate(datat2))
		
		# Data Table 3 Riwayat Studi
		print ("Riwayat Studi")
		T3 = s.select('table')[2]
		datat3 = []
		for i in range(len(T3.select('tr'))):
			datat3.append([]) ##Untuk membuat list kosong dengan jumlah array sesuai dengan isi tr
		for th in range(len(T3.select('tr')[0].select('th'))): ##Mengambil data TH
			datat3[0].append(T3.select('tr')[0].select('th')[th].string)
		for i in range(1, len(T3.select('tr'))): ##Mengulang dari 1 hingga jumlah table, untuk mengambil isi semua td
			for isi in range(len(T3.select('tr')[1].select('td'))):
				datat3[i].append(T3.select('tr')[i].select('td')[isi].string.strip())

		print (tabulate(datat3))

link_cari = cari(nim)
data_forlap(link_cari)
