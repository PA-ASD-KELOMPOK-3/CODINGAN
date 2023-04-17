from prettytable import PrettyTable
import os
import time
import getpass
import math
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
os.system("cls")

load_dotenv()

cluster = MongoClient(os.getenv("MONGO_URI"))

database = cluster["PA_ASD_KEL3"]
barang = database["data_barang"]
pelanggan = database["akun_pembeli"]
history = database["history"]
transaksi = database["transaksi"]

#Ini function untuk memberikan delay sejenak 
def cleardelay():
    os.system("cls")
    time.sleep(0.8)
def delayclear():
    time.sleep(0.8) 
    os.system("cls")

class shop:
    def __init__(self, name, price, category, flavour, stock):
        self.name = name
        self.price = price
        self.category = category
        self.flavour = flavour
        self.stock = stock
        self.next = None
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "flavour": self.flavour,
            "stock": self.stock,
            "timestamp": datetime.datetime.now()
        }

class bakery:
    def __init__(self):
        self.head = None
        #history sama dengan list kosong yang nantinya akan terisi
        self.history = []
        self.transactions = []

    #function menambah produk
    def add_product(self, cake):
        barang.insert_one(cake.to_dict())
        result = barang.find_one({"name": cake.name})
        history_data = {
            "action": "add",
            "name": result["name"],
            "price": result["price"],
            "category": result["category"],
            "flavour": result["flavour"],
            "stock": result["stock"],
            "timestamp": datetime.datetime.now()
        }
        history.insert_one(history_data)

    def remove_product(self, name):
        result = barang.delete_one({"name": name})
        if result.deleted_count == 1:
            history_data = {
                "action": "remove",
                "name": name,
                "price": "-",
                "category": "-",
                "flavour": "-",
                "stock": "-",
                "timestamp": datetime.datetime.now()
            }
            history.insert_one(history_data)
            print("Produk berhasil dihapus\n\n")
        else:
            print("Produk tidak ditemukan\n\n")

    def edit_product(self, name):
        result = barang.find_one({"name": name})
        if result is not None:
            print("Produk yang akan diubah:", result["name"])
            field_name = input("Masukkan jenis yang ingin diubah (harga/stok): ")
            new_value = int(input("Masukkan data baru: "))
            if field_name == "harga":
                if new_value > 1000000 or new_value <= 0:
                    print("Inputan harga tidak boleh lebih dari 1 juta dan tidak boleh kosong")
                else:
                    result["price"] = new_value
                    barang.replace_one({"name": name}, result)
                    history_data = {
                        "action": "edit",
                        "name": name,
                        "field_name": "harga",
                        "new_value": new_value,
                        "timestamp": datetime.datetime.now()
                    }
                    history.insert_one(history_data)
                    print(40*"=")
                    print("      Produk berhasil diubah")
                    print(40*"=")
            elif field_name == "stok":
                if new_value > 100 or new_value <= 0:
                    print("Inputan stok tidak boleh lebih dari 100 dan tidak boleh kosong")
                else:
                    result["stock"] = new_value
                    barang.replace_one({"name": name}, result)
                    history_data = {
                        "action": "edit",
                        "name": name,
                        "field_name": "stok",
                        "new_value": new_value,
                        "timestamp": datetime.datetime.now()
                    }
                    history.insert_one(history_data)
                    print(40*"=")
                    print("      Produk berhasil diubah")
                    print(40*"=")
            else:
                print("Jenis yang dimasukkan tidak sesuai")
        else:
            print("Produk tidak ditemukan\n\n")
                    
    #function menampilkan Produk
    def show_product(self):
        table = PrettyTable()
        table.title = "Produk yang Tersedia"
        table.field_names = ["Nama Kue", "Harga", "Kategori", "Rasa", "Stok"]
        hasil = barang.find()
        if len(list(hasil)) == 0:
            print("Produk Masih Kosong")
        else :
            hasil = barang.find()
            for result in barang.find():
                table.add_row([result["name"], result["price"], result["category"], result["flavour"], result["stock"]])
            print(table)

    #function menampilkan history
    def show_history(self):
        table = PrettyTable()
        table.title = "History"
        table.field_names = ["Keterangan", "Nama Produk", "Harga", "Kategori", "Rasa", "Stok"]
        hasil = history.find()
        if len(list(hasil)) == 0:
            print("History Masih Kosong")
        else :
            hasil = history.find()
            for result in hasil:
                if result["action"] == "add":
                    table.add_row(["Produk ditambahkan", result["name"], result["price"], result["category"], result["flavour"], result["stock"]])
                elif result["action"] == "remove":
                    table.add_row(["Produk dihapus", result["name"], result["price"], result["category"], result["flavour"], result["stock"]])
                elif result["action"] == "edit":
                    table.add_row(["Produk diubah (" + result["field_name"] + ")", result["name"], result["new_value"], "-", "-", "-"])
            print(table)

    def belanja(self, usn):
        print("="*54)
        print("Daftar Kue yang Tersedia".center(54))
        print("="*54)
        bakery().show_product()

        nama_kue = str(input("Masukkan Nama Kue : ")).strip().lower().title()
        jumlah_beli = int(input("Masukkan Jumlah Pembelian : "))

        # Cari data barang yang sesuai dengan nama kue yang diinput
        current = barang.find_one({"name": nama_kue})
        ncurrent = pelanggan.find_one({"name" : usn})

        if not current:
            print(">> Kue Tidak Ditemukan <<\n\n")
            input("Tekan Enter Untuk Lanjut...")
        else:
            if jumlah_beli > current["stock"]:
                print(">> Maaf, stok kue tidak mencukupi <<\n\n")
                input("Tekan Enter Untuk Lanjut...")
                delayclear()
            else:
                total_harga = current["price"] * jumlah_beli
                cleardelay()
                print("="*30)
                print("RINCIAN BELANJAAN".center(30))
                print("="*30)
                transaction = {"username": ncurrent["name"],
                               "name": current["name"],
                               "price": current["price"],
                               "quantity": jumlah_beli,
                               "total_price": total_harga,
                               "date": datetime.datetime.now().strftime("%H:%M %Y-%m-%d")}
                print("Nama         : {}\nHarga Satuan : {} \nJumlah       : {} \nTotal Harga  : {} \nTanggal      : {}".format(current["name"], current["price"], jumlah_beli, total_harga, datetime.datetime.now().strftime("%H:%M %Y-%m-%d")))
                print("="*30)
                input("\n\nTekan Enter Untuk Lanjut...")
                tanya = input("Lanjutkan Pembayaran? [y/t]: ")
                if tanya == "y":
                    cleardelay()
                    print("="*50)
                    barang.update_one({"name": current["name"]}, {"$inc": {"stock": -jumlah_beli}})
                    print("         Membuat Struk Belanja..")
                    delayclear
                    harganya = current["price"]
                    tanggal = datetime.datetime.now().strftime("%H:%M %Y-%m-%d")
                    print("="*50)
                    print("<>><<><>><<>>< STRUK BELANJA ><<>><<><>><<>")
                    print("="*50)
                    print(f"   Nama Pelanggan   : {usn}")
                    print(f"   Tanggal          : {tanggal}\n")
                    print(f"   Nama Kue         : {nama_kue}")
                    print(f"   Jumlah           : {jumlah_beli}")
                    print(f"   Harga Satuan Kue : {harganya}")
                    transaksi.insert_one(transaction)
                    print("="*50)
                    print("\n<..><..> Transaksi Berhasil Dilakukan <..><..>\n")
                    input("Tekan Enter Untuk Lanjut...")
                    delayclear()
                else:
                    print("\n<..><..> Transaksi Dibatalkan <..><..>\n")
                    input("Tekan Enter Untuk Lanjut...")

    def transaction_history(self, usn):
        os.system("cls")
        user = pelanggan.find_one({"name": usn})
        if user is None:
            print("Maaf, pengguna tidak ditemukan.")
            return
        user_history = transaksi.find({"username": user["name"]})
        if len(list(user_history)) == 0:
            cleardelay()
            print(70*"=")
            print("Belum ada riwayat pembelian yang dilakukan oleh pengguna ini.")
            print(70*"=")
            input("Tekan Enter Untuk Lanjut...")
            delayclear()
        else:
            for history_data in transaksi.find():
                print(40*"=")
                print("Nama Pembeli :", history_data["username"])
                print("Produk :", history_data["name"])
                print("Harga :", history_data["price"])
                print("Jumlah:", history_data["quantity"])
                print("Total Harga :", history_data["total_price"])
                print("Tanggal Transaksi :", history_data["date"])
                print(40*"=")
                print("\n")
            input("Tekan Enter Untuk Lanjut...")
            delayclear()

    #JUMP SEARCH DESKRIPSI PRODUK
    def jump_search(self, key):
            data = []
            hasil = barang.find({})
            for i in hasil:
                data.append(i)
            merge_sort_nama(data)

            if not data:
                print("Data tidak ditemukan!")
                return None

            n = len(data)
            step = int(n ** 0.5)
            prev = 0
        
            while prev < n and data[prev]['name'] < key:
                prev += step
            prev -= step
            while prev < n:
                if data[prev]['name'] == key:
                    return data[prev]
                prev += 1
            return None
                
    def search(self):
        os.system("cls")
        print("=" * 30)
        print("Cari Produk".center(30))
        print("=" * 30)
        nama = str.title(input("Masukkan nama produk: "))
        result = self.jump_search(nama)
        if result is not None:
            table = PrettyTable()
            table.title = "Deskripsi Produk"
            table.field_names = ["Nama Kue", "Harga", "Kategori", "Rasa", "Stok"]
            table.add_row([result["name"], result["price"], result["category"], result["flavour"], result["stock"]])
            print(table)
        input("Tekan Enter Untuk Lanjut...")
        delayclear()
      
#MERGE SORT berdasarkan nama
def merge_sort_nama(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort_nama(left_arr)
        merge_sort_nama(right_arr)
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i]["name"].lower() < right_arr[j]["name"].lower():
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def merge_sort_wrapper_nama():
    product_list = []
    hasil = barang.find()
    if len(list(hasil)) == 0:
        print("Produk Masih Kosong")
    else :
        for x in barang.find({}):
            product_list.append(x)
        merge_sort_nama(product_list)
        table = PrettyTable()
        table.field_names = ["Nama Kue", "Harga", "Kategori", "Rasa", "Stok"]
        for z in product_list:
            table.add_row([z["name"], z["price"], z["category"], z["flavour"], z["stock"]])
        table.sortby = "Nama Kue"
        print(table)
        
#MERGE SORT berdasarkan harga
def merge_sort_harga(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort_harga(left_arr)
        merge_sort_harga(right_arr)
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i]["price"] < right_arr[j]["price"]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def merge_sort_wrapper_harga():
    product_list = []
    hasil = barang.find()
    if len(list(hasil)) == 0:
        print("Produk Masih Kosong")
    else :
        for x in barang.find({}):
            product_list.append(x)
        merge_sort_harga(product_list)
        table = PrettyTable()
        table.field_names = ["Nama Kue", "Harga", "Kategori", "Rasa", "Stok"]
        for z in product_list:
            table.add_row([z["name"], z["price"], z["category"], z["flavour"], z["stock"]])
        table.sortby = "Harga"
        print(table)

#MERGE SORT berdasarkan kategori
def merge_sort_kategori(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort_kategori(left_arr)
        merge_sort_kategori(right_arr)
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i]["category"].lower() < right_arr[j]["category"].lower():
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def merge_sort_wrapper_kategori():
    product_list = []
    hasil = barang.find()
    if len(list(hasil)) == 0:
        print("Produk Masih Kosong")
    else :
        for x in barang.find({}):
            product_list.append(x)
        merge_sort_kategori(product_list)
        table = PrettyTable()
        table.field_names = ["Nama Kue", "Harga", "Kategori", "Rasa", "Stok"]
        for z in product_list:
            table.add_row([z["name"], z["price"], z["category"], z["flavour"], z["stock"]])
        table.sortby = "Kategori"
        print(table)

#MERGE SORT berdasarkan rasa
def merge_sort_rasa(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort_rasa(left_arr)
        merge_sort_rasa(right_arr)
        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i]["flavour"].lower() < right_arr[j]["flavour"].lower():
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def merge_sort_wrapper_rasa():
    product_list = []
    hasil = barang.find()
    if len(list(hasil)) == 0:
        print("Produk Masih Kosong")
    else :
        for x in barang.find({}):
            product_list.append(x)
        merge_sort_rasa(product_list)
        table = PrettyTable()
        table.field_names = ["Nama Kue", "Harga", "Kategori", "Rasa", "Stok"]
        for z in product_list:
            table.add_row([z["name"], z["price"], z["category"], z["flavour"], z["stock"]])
        table.sortby = "Rasa"
        print(table)

def menu_urut():
    print("1. Urutkan Berdasarkan Nama")
    print("2. Urutkan Berdasarkan Harga")
    print("3. Urutkan Berdasarkan Kategori")
    print("4. Urutkan Berdasarkan Rasa")
    print("5. Cari Kue")

def menuadmin():
    print("<><><><><> Welcome To Sweet Bakery <><><><><>")
    print("  <><><><><>   Bakery  Menu   <><><><><>")
    print("1. Tampilkan Produk Yang Tersedia")
    print("2. Tambahkan Produk Baru ke dalam List")
    print("3. Hapus Produk Dari List")
    print("4. Update Produk")
    print("5. Tampilkan History")
    print("6. Exit")

def loginadmin():
    while True :
        os.system("cls")
        print(40*"=")
        print("              LOGIN ADMIN   ")
        print(40*"=")
        username = str.capitalize(input("Input Username Anda: "))
        password = getpass.getpass("Input Password Anda: ")
        # Validasi username dan password

    # Main program
        if username == "Admin" and password == "admin123":
            while True:
                cleardelay()
                print("<=><=><=><=> WELCOME ADMIN ^--^ <=><=><=><=>")
                menuadmin()
                choice = int(input("\nInput Opsi (1-6): "))
                while True :
                    if choice == 1:
                        cleardelay()
                        menu_urut()
                        urut = int(input("Pilih Opsi Urut Produk : "))
                        if urut == 1:
                            cleardelay()
                            print("Produk telah diurutkan berdasarkan nama")
                            delayclear()
                            merge_sort_wrapper_nama()
                            input("Tekan Enter Untuk Lanjut...")
                            break
                        elif urut == 2:
                            cleardelay()
                            print("Produk telah diurutkan berdasarkan harga")
                            delayclear()
                            merge_sort_wrapper_harga()
                            input("Tekan Enter Untuk Lanjut...")
                            break
                        elif urut == 3:
                            cleardelay()
                            print("Produk telah diurutkan berdasarkan kategori")
                            delayclear()
                            merge_sort_wrapper_kategori()
                            input("Tekan Enter Untuk Lanjut...")
                            break
                        elif urut == 4:
                            cleardelay()
                            print("Produk telah diurutkan berdasarkan rasa")
                            delayclear()
                            merge_sort_wrapper_rasa()
                            input("Tekan Enter Untuk Lanjut...")
                            break
                        elif urut == 5:
                            bakery().search()
                            break
                        else :
                            print("Invalid!")
                            break
                    elif choice == 2:
                        name = str.title(input("Input Nama Produk Baru  : "))
                        check = barang.find_one({"name": name})
                        if check is not None:
                            print("Produk sudah ada di menu")
                        elif check is None :
                            price = int(input("Input Harga             : "))
                            if price > 1000000 or price <= 0:
                                print("Inputan harga tidak boleh lebih dari 1 juta dan tidak boleh kosong")
                            else:
                                category = str.title(input("Input Kategori Produk   : "))
                                flavour = str.title(input("Input Jenis Rasa Produk  : "))
                                stock = int(input("Input Jumlah Stok       : "))
                                if stock > 100 or stock <= 0:
                                    print("Inputan stok tidak boleh lebih dari 100 dan tidak boleh kosong")
                                else:
                                    update = shop(name, price, category, flavour, stock)
                                    bakery().add_product(update)
                                    cleardelay()
                                    print("Produk Baru Berhasil Ditambahkan")
                                    input("Tekan Enter Untuk Lanjut...")
                                    break
                        else :
                            print("")
                            
                    elif choice == 3:
                        name = str.title(input("Masukan Nama Produk yang Ingin Dihapus : "))
                        cleardelay()
                        bakery().remove_product(name)
                        input("Tekan Enter Untuk Lanjut...")
                        break
                    elif choice == 4:
                        cleardelay()
                        bakery().show_product()
                        upd = str.title(input("Masukan Nama Produk yang Ingin Diubah : "))
                        cleardelay()
                        bakery().edit_product(upd)
                        input("Tekan Enter Untuk Lanjut...")
                        break
                    elif choice == 5:
                        cleardelay()
                        bakery().show_history()
                        input("Tekan Enter Untuk Lanjut...")
                        break
                    elif choice == 6:
                        delayclear()
                        return
                    else:
                        print("Pilihan Tidak Sesuai Mohon Coba Lagi")
                        time.sleep(0.8)
                        break
        else :
            cleardelay()
            print("Invalid Login")
            delayclear()

def menupelanggan():
    print("<><><><><> Welcome To Sweet Bakery <><><><><>")
    print("  <><><><><>   Bakery  Menu   <><><><><>")
    print("1. Tampilkan Produk Yang Tersedia")
    print("2. Shopping")
    print("3. Check History Belanja")
    print("4. Exit")

def loginuser():
    while True :
        os.system("cls")
        print(40*"=")
        print("              LOGIN AKUN   ")
        print(40*"=")
        usn = str.capitalize(input("Masukkan nama pengguna: "))
        password = getpass.getpass("Masukkan kata sandi: ")
        result = pelanggan.find_one({"name": usn})
        if result is None:
            print("Maaf, nama pengguna tidak terdaftar.")
        elif result["password"] != password:
            print("Maaf, kata sandi salah.")
        else:
            cleardelay()
            print("<=><=><=><=> Selamat datang",usn,"<=><=><=><=>")
            delayclear()
            print("<=><=><=><=> Selamat Berbelanja <=><=><=><=>")
            delayclear()
            while True:
                    os.system("cls")
                    menupelanggan()
                    choice = int(input("\nInput Opsi (1-3): "))
                    if choice == 1:
                        cleardelay()
                        menu_urut()
                        urut = int(input("Pilih Opsi Urut Produk : "))
                        if urut == 1:
                            cleardelay()
                            print("Produk telah diurutkan berdasarkan nama")
                            delayclear()
                            merge_sort_wrapper_nama()
                            input("Tekan Enter Untuk Lanjut...")

                        elif urut == 2:
                            cleardelay()
                            print("Produk telah diurutkan berdasarkan harga")
                            delayclear()
                            merge_sort_wrapper_harga()
                            input("Tekan Enter Untuk Lanjut...")

                        elif urut == 3:
                            cleardelay()
                            print("Produk telah diurutkan berdasarkan kategori")
                            delayclear()
                            merge_sort_wrapper_kategori()
                            input("Tekan Enter Untuk Lanjut...")
        
                        elif urut == 4:
                            cleardelay()
                            print("Produk telah diurutkan berdasarkan rasa")
                            delayclear()
                            merge_sort_wrapper_rasa()
                            input("Tekan Enter Untuk Lanjut...")
                            
                        elif urut == 5:
                            bakery().search()

                        else :
                            print("Invalid!")
                            
                    elif choice == 2:
                        cleardelay()
                        bakery().belanja(usn)
                    
                    elif choice == 3:
                        bakery().transaction_history(usn)
                        
                    elif choice == 4:
                        delayclear()
                        return
                    else:
                        print("Pilihan Tidak Sesuai Mohon Coba Lagi")
                        time.sleep(0.8)

def program():
    while True :
        os.system("cls")
        print(". . . . . .<><><><><>. . . . . .<><><><><>. . . . . .")
        print("1. Login Admin")
        print("2. Login Pelanggan")
        print("3. Registrasi Pelanggan")
        print("4. Exit")
        print(". . . . . .<><><><><>. . . . . .<><><><><>. . . . . .")
        try : 
            choice = int(input("Input Opsi (1-4): "))
            if choice == 1:
                loginadmin()
            elif choice == 2:
                loginuser()
            elif choice == 3:
                os.system("cls")
                print(40*"=")
                print("           REGISTRASI AKUN      ")
                print(40*"=")
                regisUser = str.capitalize(input("Masukkan nama pengguna baru: "))
                regisPass = getpass.getpass("Masukkan kata sandi baru: ")
                result = pelanggan.find_one({"name": regisUser})
                if not regisUser.strip() or not regisPass.strip():
                    print("Maaf, nama pengguna atau kata sandi tidak boleh kosong")
                    delayclear()
                elif result is not None:
                    print("Maaf, nama pengguna sudah terdaftar")
                    delayclear()
                elif not regisUser.isalnum():
                    print("Nama pengguna hanya boleh terdiri dari huruf dan angka.")
                    delayclear()
                elif not regisPass.isnumeric():
                    print("Kata sandi hanya boleh terdiri dari angka.")
                    delayclear()
                else:
                    user_data = {
                        "name": regisUser,
                        "password": regisPass
                    }
                    pelanggan.insert_one(user_data)
                    print(40*"=")
                    print("Registrasi akun pembeli berhasil dilakukan.\n")
                    input("Tekan Enter Untuk Lanjut...")
            elif choice == 4 :
                cleardelay()
                print(40*"<>")
                print("|               Terimakasih sudah menggunakan layanan kami :)                  |".center(70))
                print(40*"<>")
                raise SystemExit
            elif choice is not True or choice is str:
                cleardelay()
                print("Terjadi Kesalahan Opsi")
                delayclear()
        except ValueError :
            cleardelay()
            print("Terjadi Kesalahan")
            delayclear()
        except KeyboardInterrupt :
            cleardelay()
            print("Key yang Diinput Tidak Sesuai, Anda Dialihkan ke menu utama!")
            delayclear()

program()
