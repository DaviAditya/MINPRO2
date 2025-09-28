
role = {
    "admin": {"password": "111", "role": "admin"},
    "user": {"password": "222", "role": "user"}
}

diecast = [
    {"Collection": 1, "Brand": "HotWheels", "Seri": "FERARRI"},
    {"Collection": 2, "Brand": "Tomica", "Seri": "Dream"},
    {"Collection": 3, "Brand": "MiniGT", "Seri": "LBWK"}
]

import pwinput

def login():    
        KESEMPATAN = 0
        while KESEMPATAN < 3:
            try:
                username = input("username: ")
                password = pwinput.pwinput("password: ")
                if username in role and role[username]["password"] == password:
                    posisi = role[username]["role"]
                    print(f"Welcome {username}")
                    return posisi
                else:
                    KESEMPATAN += 1
                    print(f"Maaf coba lagi ({KESEMPATAN}/3)")
            except ValueError:
                print("Masukkan angka saja")
            except KeyboardInterrupt:
                print("Jangan tekan CTRL+C!")
            except EOFError: 
                print("JANGAN TEKAN CTRL+Z")
                continue        
        print("Coba lagi lain kali. Percobaan habis")


def List_Collection():
    print("---====== Daftar Koleksi ======---")
    for item in diecast:
        print(f"Collection: {item['Collection']} | Brand: {item['Brand']}   | Seri: {item['Seri']}")
    print("=====================================\n")

def Tambah_Collection():
    try:
        Collection_baru = len(diecast) + 1
        brand = input("Brand: ")
        Seri = input("Seri: ")
        diecast.append({"Collection": Collection_baru, "Brand": brand, "Seri": Seri})
        print("Berhasil ditambahkan ygy!")
        print("-------------------------\n")
    except:
        print("TERJADI EROR")

def Update_Seri():
    try:
        brand_update = input("Brand yang ingin diupdate: ")
        seri_baru = input("Seri baru: ")

        for item in diecast:
            if item["Brand"].lower() == brand_update.lower():
                old_seri = item["Seri"]
                item["Seri"] = seri_baru
                print(f"Seri {brand_update} berhasil update menjadi {seri_baru}\n")
                return
        print(f"brand {brand_update} tidak ada\n")
    except:
        print("TERJADI EROR")


def Hapus_Collection():
    try:
        List_Collection()
        DC = int(input("Collection yang ingin dihapus: "))
        for item in diecast:
            if item["Collection"] == DC:
                diecast.remove(item)
                print(f"Collection {DC} BERHASIL DIHAPUS\n")
                return
        print("DC Tidak Ditemukan\n")
    except:
        print("terjadi eror")

def menu():
    
        sebagai = login()
        while True:
            try:
                if sebagai == "admin":
                    print("=====================")
                    print("Menu")
                    print("1. Lihat Collection")
                    print("2. Tambah Collection")
                    print("3. Update Collection")
                    print("4. Hapus Collection")
                    print("5. Out")
                    print("=====================\n")

                    pilih = input("Pilih Menu: ")
                    if pilih == "1":
                        List_Collection()
                    elif pilih == "2":
                        Tambah_Collection()
                    elif pilih == "3":
                        Update_Seri()
                    elif pilih == "4":
                        Hapus_Collection()
                    elif pilih =="5":
                        print("Out of program....")
                        break
                    else: 
                        print("Pilihan tidak tersedia\n")

                elif sebagai == "user":
                    print("Menu: ")
                    print("1. Lihat Collection")
                    print("2. Out")

                    pilih = input("Pilih Menu: ")
                    if pilih == "1":
                        List_Collection()
                    elif pilih == "2":
                        print("Out of program....")
                        break
                    else: 
                        print("Pilihan tidak tersedia\n")
            except KeyboardInterrupt:
                print("Jangan tekan CTRL+C")
            except EOFError:
                print("Jangan tekan ctrl+z")
            continue
menu()