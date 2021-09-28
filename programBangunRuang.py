from time import sleep
import math
menuA = {}
menuA['== 1.']="Kubus"
menuA['== 2.']="Balok"
menuA['== 3.']="Tabung"
menuA['== 4.']="Kerucut"
menuA['== 5.']="Keluar"
bR = 0

def cetakMenuAwal():
    while True:
        options=menuA.keys()
        print("==== MENU KALKULATOR BANGUN RUANG ====")
        print("== -------------------------------- ==")
        for entry in options:
            print(entry, menuA[entry])
        print("== -------------------------------- ==")
        print("======================================")
        selection = input("Masukan pilihan : ")
        # Loop Menu Awal    
        if selection == '1':
            bR = 1
            break
        elif selection == '2':
            bR = 2
            break
        elif selection == '3':
            bR = 3
            break
        elif selection == '4':
            bR = 4
            break
        elif selection == '5':
            break
        else:
            print("Pilih angka yang tersedia!")
    cetakMenuHitung()
        

menuH = {}
menuH['== 1.']="Luas Permukaan"
menuH['== 2.']="Volume"
menuH['== 3.']="Kembali"
def cetakMenuHitung():
    while True:
        options=menuH.keys()
        print("==== MENU KALKULATOR BANGUN RUANG ====")
        print("== -------------------------------- ==")
        print("== Mau hitung apa?		    ==")
        for entry in options:
            print(entry, menuH[entry])
        print("== -------------------------------- ==")
        print("======================================")
        selection = input("Masukan pilihan : ")
        # Loop Menu Hitung
        if selection == '2':
            hitungLuasPermukaan(bR)
            break
        elif selection == '2':
            hitungVolume(bR)
            break
        else:
            print("Pilih angka yang tersedia!")

def hitungLuasPermukaan(brg):
    if brg == 1:
        rusukKubus = float(input("Masukan Nilai Rusuk Kubus (CM)= "))
        LPKubus = 6 * (rusukKubus * rusukKubus)
        print("Nilai Luas Permukaan Kubus= ", LPKubus, "CM")

    if brg == 2:
        p = int(input("Masukkan nilai panjang = "))
        l = int(input("Masukkan nilai lebar = "))
        t = int(input("Masukkan nilai tinggi = "))
        lpBalok = (2*p*l) + (2*p*t) + (2*l*t)
        print("Luas Permukaan Balok = ")
        print(int(lpBalok))
	if brg == 3:
        r = float(input("Jari - Jari Tabung = "))
        t = float(input("Tinggi Tabung = "))
        lpTabung = math.pi*2*r*(r+t)
        print("Luas Permukaan Tabung = ", lpTabung)
	elif brg == 4:

def hitungVolume(brg):
    if brg == 1:
        rusukKubus = float(input("Masukan Nilai Rusuk Kubus (CM)= "))
        volumeKubus = rusukKubus * rusukKubus * rusukKubus
        print("Nilai Volume Kubus= ", volumeKubus, "CM")
        
    if brg == 2:
        p = int(input("Masukkan nilai panjang = "))
        l = int(input("Masukkan nilai lebar = "))
        t = int(input("Masukkan nilai tinggi = "))
        volBalok = p*l*t
        print("Volume Balok = ")
        print(int(volBalok))
	elif brg == 3:
        r = float(input("Jari - Jari Tabung = "))
        t = float(input("Tinggi Tabung"))
        volTabung = math.pi*r*r*t
        print("Volume Tabung = ", volTabung)
	elif brg == 4:

## Execute
cetakMenuAwal()


