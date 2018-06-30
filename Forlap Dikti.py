forlap = 'https://forlap.ristekdikti.go.id/mahasiswa/detail/NjFENzNGOTItNTM4Ri00QTQ4LUI2RkUtMzE3N0ZGRTRFQjQ0'


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

			
data_forlap(forlap)
