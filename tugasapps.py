from os import system
import time
from datetime import datetime

def menu():
	system("cls")
	menu = """
		BOOKING HOTEL
	[A] . LOKASI & HARGA HOTEL
	[B] . BOOKING HOTEL
	[C] . PENCARIAN PESANAN
	[D] . SEMUA PESANAN
	[E] . CHECK-OUT KAMAR

	[Q] . KELUAR
		"""
	print(menu)

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def create_id_contact():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	counter = len(data_pemesanan)+1
	id_contact = str("%4d%02d%02d-Z%01d" % (year, month, hari, counter))
	return id_contact

def pemesanan():
	system("cls")
	print("-BOOKING HOTEL-")
	nama = input("NAMA\t: ")
	telp = input("TELP\t: ")
	kamar = input("KAMAR (A/B/C)\t: ")
	lokasi = input("LOKASI\t: ")
	
	user_ans = input("Apakah anda yakin untuk memesan? (Y/N) : ")

	if verify_ans(user_ans):
		id_contact = create_id_contact()
		print("Menyimpan Data ...")
		time.sleep(1)
		data_pemesanan[id_contact] = {
			"nama" : nama,
			"telp" : telp,
			"kamar" : kamar,
			"lokasi" : lokasi
		}
		print("Pemesanan Berhasil, Silakan Cek Ulang Pesanan untuk Mengetahui Kode Booking Anda")
	else:
		print("Pemesanan Gagal, Coba Lagi")
	input("Tekan ENTER untuk kembali ke MENU")

def daftar_kamar():
	system("cls")
	daftar = """
		LOKASI HOTEL 
	1. Palembang
	2. Bandung
	3. Jakarta
	4. Surabaya

		HARGA KAMAR
	[A] Standard	: Rp 750.000,-
	[B] Deluxe	: Rp 1.400.000,-
	[C] Superior	: Rp 1.950.000,-

		"""
	print(daftar)
	input("Tekan ENTER untuk kembali ke MENU")

def print_data_pemesanan(id_contact = None, all_fields = False, lokasi = True):
	if id_contact != None and all_fields == False:
		print(f"""
		-DATA DITEMUKAN-
	Kode \t: {id_contact}
	Nama \t:{data_pemesanan[id_contact]["nama"]}
	Telp \t:{data_pemesanan[id_contact]["telp"]}
	Kamar \t:{data_pemesanan[id_contact]["kamar"]}
	Lokasi \t:{data_pemesanan[id_contact]["lokasi"]}
			""")
	elif id_contact != None and lokasi == False:
		print(f"""
		-DATA DITEMUKAN-
	Kode \t: {id_contact}
	Nama \t:{data_pemesanan[id_contact]["nama"]}
	Telp \t:{data_pemesanan[id_contact]["telp"]}
	Kamar \t:{data_pemesanan[id_contact]["kamar"]}
			""")
	elif all_fields == True:
		for id_contact in data_pemesanan:
			nama = data_pemesanan[id_contact]["nama"]
			telp = data_pemesanan[id_contact]["telp"]
			kamar = data_pemesanan[id_contact]["kamar"]
			lokasi = data_pemesanan[id_contact]["lokasi"]
			print(f"""
				Kode:{id_contact}
				Nama:{nama}
				Telp:{telp}
				Kamar:{kamar}
				Lokasi:{lokasi}
				"""
				)

def searching_by_name(file):
	for id_contact in data_pemesanan:
		if data_pemesanan[id_contact]["nama"] == file:
			print_data_pemesanan(id_contact=id_contact)
			return id_contact
	else:
		print("-DATA TIDAK DITEMUKAN-")
		return False

def pencarian_pesanan():
	system("cls")
	print("- PENCARIAN PESANAN -")
	nama = input("Nama Kontak Yang Dicari : ")
	result = searching_by_name(nama)
	input("Tekan ENTER untuk kembali ke MENU")

def semua_pesanan():
	system("cls")
	print("-SEMUA PESANAN-")
	if len(data_pemesanan) == 0:
		print("BELUM ADA PEMESANAN")
	else:
		print_data_pemesanan(all_fields=True)
	input("Tekan ENTER untuk kembali ke MENU")

def check_out():
	system("cls")
	print("-CHECK OUT-")
	nama = input("Nama Pemesan yang ingin Check-Out Pesanan : ")
	id_contact = searching_by_name(nama)
	result = data_pemesanan[id_contact]
	if result:
		respon = input(f"Yakin ingkin Check-Out pesanan? (Y/N): ")
		if verify_ans(respon):
			del data_pemesanan[id_contact]
			print("Menyimpan Data ...")
			time.sleep(1)
			print("CHECK-OUT BERHASIL DILAKUKAN")
		else:
			print("CHECK-OUT GAGAL DILAKUKAN")
	input("Tekan ENTER untuk kembali ke MENU")

def check_input(char):
	char = char.upper()
	if char == "Q":
		return True
	elif char == "A":
		daftar_kamar()
	elif char == "B":
		pemesanan()
	elif char == "C":
		pencarian_pesanan()
	elif char == "D":
		semua_pesanan()
	elif char == "E":
		check_out()
		
data_pemesanan = {
	"20201020-A01" : {
		"nama"	: "Katarina",
		"telp" 	: "12345",
		"kamar" : "A",
		"lokasi": "Jakarta"
	},
	"20201020-C02" : {
		"nama" : "Sien",
		"telp" : "67890",
		"kamar": "C",
		"lokasi": "Surabaya"
	}
}
stop = False

while not stop:
	menu()
	user_input = input("Pilihan : ")
	stop = check_input(user_input)
