from prettytable import PrettyTable
import os
import time
import getpass
import sys
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

#CONTROLLER
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
        self.history = []
        self.transactions = []

        # Membuat linked list dari data di MongoDB
        for item in barang.find():
            cake = shop(item["name"], item["price"], item["category"], item["flavour"], item["stock"])
            if not self.head:
                self.head = cake
            else:
                current_shop = self.head
                while current_shop.next:
                    current_shop = current_shop.next
                current_shop.next = cake

    def add_product(self, cake):
        new_shop = shop(cake.name, cake.price, cake.category, cake.flavour, cake.stock)
        if not self.head:
            self.head = new_shop
        else:
            current_shop = self.head
            while current_shop.next:
                current_shop = current_shop.next
            current_shop.next = new_shop
        result = barang.insert_one(cake.to_dict())
        history_data = {
            "action": "add",
            "name": cake.name,
            "price": cake.price,
            "category": cake.category,
            "flavour": cake.flavour,
            "stock": cake.stock,
            "timestamp": datetime.datetime.now()
        }
        history.insert_one(history_data)

    def remove_product(self, name):
        current_shop = self.head
        prev_shop = None

        while current_shop and current_shop.name != name:
            prev_shop = current_shop
            current_shop = current_shop.next

        if current_shop is None:
            os.system("cls")
            loading_animation()
            os.system("cls")
            print(40*"=")
            print("Produk Tidak Ditemukan".center(40))
            print(40*"=")
            return

        result = barang.delete_one({"name": name})

        if result.deleted_count == 1:
            history_data = {
                "action": "remove",
                "name": name,
                "price": current_shop.price,
                "category": current_shop.category,
                "flavour": current_shop.flavour,
                "stock": current_shop.stock,
                "timestamp": datetime.datetime.now()
            }
            history.insert_one(history_data)

            if prev_shop is None:
                self.head = current_shop.next
            else:
                prev_shop.next = current_shop.next

            os.system("cls")
            loading_animation()
            os.system("cls")
            print(40*"=")
            print("Produk Berhasil Dihapus".center(40))
            print(40*"=")
        else:
            os.system("cls")
            loading_animation()
            os.system("cls")
            print(40*"=")
            print("Produk Tidak Ditemukan".center(40))
            print(40*"=")

    #function mengedit produk
    def edit_product(self, name):
        result = barang.find_one({"name": name})
        if result is not None:
            print("Produk yang akan diubah                      :", result["name"])
            field_name = input("Masukkan jenis yang ingin diubah [harga/stok]: ")
            new_value = int(input("Masukkan data baru                           : "))
            if field_name == "harga":
                if new_value > 1000000 or new_value <= 0:
                    print("Inputan Harga Tidak Boleh Lebih Dari 1 Juta dan Tidak Boleh Kosong")
                else:
                    result["price"] = new_value
                    barang.replace_one({"name": name}, result)
                    current_shop = self.head
                    while current_shop:
                        if current_shop.name == name:
                            current_shop.price = new_value
                            break
                        current_shop = current_shop.next
                    history_data = {
                        "action": "edit",
                        "name": name,
                        "field_name": "harga",
                        "new_value": new_value,
                        "timestamp": datetime.datetime.now()
                    }
                    history.insert_one(history_data)
                    os.system("cls")
                    loading_animation()
                    os.system("cls")
                    print(40*"=")
                    print("Produk Berhasil Diubah".center(40))
                    print(40*"=")
            elif field_name == "stok":
                if new_value > 100 or new_value <= 0:
                    print("Inputan Stok Tidak Boleh Lebih Dari 100 dan Tidak Boleh Kosong")
                else:
                    result["stock"] = new_value
                    barang.replace_one({"name": name}, result)
                    current_shop = self.head
                    while current_shop:
                        if current_shop.name == name:
                            current_shop.stock = new_value
                            break
                        current_shop = current_shop.next
                    history_data = {
                        "action": "edit",
                        "name": name,
                        "field_name": "stok",
                        "new_value": new_value,
                        "timestamp": datetime.datetime.now()
                    }
                    history.insert_one(history_data)
                    os.system("cls")
                    loading_animation()
                    os.system("cls")
                    print(40*"=")
                    print("Produk Berhasil Diubah".center(40))
                    print(40*"=")
        else:
            os.system("cls")
            loading_animation()
            os.system("cls")
            print(40*"=")
            print("Produk Tidak Ditemukan".center(40))
            print(40*"=")
                    
    #function menampilkan Produk
    def show_product(self):
        table = PrettyTable()
        table.title = "Produk yang Tersedia"
        table.field_names = ["Nama Kue", "Harga", "Kategori", "Rasa", "Stok"]
        current_shop = self.head
        while current_shop:
            table.add_row([current_shop.name, current_shop.price, current_shop.category, current_shop.flavour, current_shop.stock])
            current_shop = current_shop.next
        hasil = barang.find()
        if len(list(hasil)) == 0:
            print("Produk Masih Kosong")
        else:
            for result in barang.find():
                table.add_row([result["name"], result["price"], result["category"], result["flavour"], result["stock"]])
            print(table)

    #function biasa untuk menampilkan history
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
                    if result["field_name"] == "harga":
                        table.add_row(["Produk diubah (harga)", result["name"], result["new_value"], "-", "-", "-"]) 
                    elif result["field_name"] == "stok":
                        table.add_row(["Produk diubah (stok)", result["name"], "-", "-", "-", result["new_value"]])
            print(table)

    def belanja(self, usn):
        print("="*65)
        bakery().show_product()

        nama_kue = str(input("Masukkan nama kue         : ")).strip().lower().title()
        jumlah_beli = int(input("Masukkan jumlah pembelian : "))

        # Cari data barang yang sesuai dengan nama kue yang diinput
        current = barang.find_one({"name": nama_kue})
        ncurrent = pelanggan.find_one({"name" : usn})
        if not current:
            print(40*"=")
            print("Kue Tidak Ditemukan".center(40))
            print(40*"=")
            input("Tekan Enter Untuk Lanjut...")
        else:
            if jumlah_beli > current["stock"]:
                print(40*"=")
                print("Stok Kue Tidak Mencukupi")
                print(40*"=")
                input("Tekan Enter Untuk Lanjut...")
                delayclear()
            elif jumlah_beli < 1 :
                print(40*"=")
                print("Jumlah Kue Tidak Boleh Kosong")
                print(40*"=")
                input("Tekan Enter Untuk Lanjut...")
                delayclear()
            else:
                total_harga = current["price"] * jumlah_beli
                cleardelay()
                print("="*40)
                print("RINCIAN BELANJAAN".center(40))
                print("="*40)
                transaction = {"username": ncurrent["name"],
                               "name": current["name"],
                               "price": current["price"],
                               "quantity": jumlah_beli,
                               "total_price": total_harga,
                               "date": datetime.datetime.now().strftime("%H:%M %Y-%m-%d")}
                print("Nama         : {}\nHarga Satuan : {} \nJumlah       : {} \nTotal Harga  : {} \nTanggal      : {}".format(current["name"], current["price"], jumlah_beli, total_harga, datetime.datetime.now().strftime("%H:%M %Y-%m-%d")))
                print("="*40)
                input("\n\nTekan Enter Untuk Lanjut...")
                delayclear()
                tanya = input("Lanjutkan pembayaran? [y/t]: ")
                if tanya == "y":
                    cleardelay()
                    barang.update_one({"name": current["name"]}, {"$inc": {"stock": -jumlah_beli}})
                    print("Membuat Struk Belanja..".center(40))
                    harganya = current["price"]
                    tanggal = datetime.datetime.now().strftime("%H:%M %Y-%m-%d")
                    print("="*50)
                    print(" STRUK BELANJA ".center(50,"~"))
                    print("="*50)
                    print(f"   Nama Pelanggan   : {usn}")
                    print(f"   Tanggal          : {tanggal}\n")
                    print(f"   Nama Kue         : {nama_kue}")
                    print(f"   Jumlah           : {jumlah_beli}")
                    print(f"   Harga Satuan Kue : {harganya}")
                    transaksi.insert_one(transaction)
                    print("="*40)
                    input("Tekan Enter Untuk Lanjut...")
                    os.system("cls")
                    loading_animation()
                    os.system("cls")
                    print("="*50)
                    print("<..><..> Transaksi Berhasil Dilakukan <..><..>".center(50))
                    print("="*50)
                    input("Tekan Enter Untuk Lanjut...")
                    delayclear()
                else:
                    os.system("cls")
                    loading_animation()
                    os.system("cls")
                    print("="*50)
                    print("<..><..> Transaksi Dibatalkan <..><..>".center(50))
                    print("="*50)
                    input("Tekan Enter Untuk Lanjut...")

    def transaction_history(self, usn):
        os.system("cls")
        user = pelanggan.find_one({"name": usn})
        if user is None:
            print("Pengguna Tidak Ditemukan")
            return
        count = transaksi.count_documents({"username": usn})
        if count == 0:
            cleardelay()
            print(70*"=")
            print("Belum Ada Transaksi Yang Dilakukan Oleh Pengguna Ini".center(70))
            print(70*"=")
            input("Tekan Enter Untuk Lanjut...")
            delayclear()
        else:
            user_history = transaksi.find({"username": usn})
            for history_data in user_history:
                print(40*"=")
                print("Nama Pembeli      :", history_data["username"])
                print("Produk            :", history_data["name"])
                print("Harga             :", history_data["price"])
                print("Jumlah            :", history_data["quantity"])
                print("Total Harga       :", history_data["total_price"])
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
                print("Data Tidak Ditemukan!")
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
        print("="*40)
        print("Cari Produk".center(40))
        print("="*40)
        nama = str.title(input("Masukkan nama produk: "))
        os.system("cls")
        loading_animation()
        os.system("cls")
        result = self.jump_search(nama)
        if result is None:
            print(40*"=")
            print("Data Tidak Ditemukan".center(40))
            print(40*"=")
        else:
            table = PrettyTable()
            table.title = "Deskripsi Produk"
            table.field_names = ["Nama Kue", "Harga", "Kategori", "Rasa", "Stok"]
            table.add_row([result["name"], result["price"], result["category"], result["flavour"], result["stock"]])
            print(table)
        input("Tekan Enter Untuk Lanjut...")
        delayclear()
      
#Merge Sort Berdasarkan Nama
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
        
#Merge Sort Berdasarkan Harga
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

#Merge Sort Berdasarkan Kategori
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

#Merge Sort Berdasarkan Rasa
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

#VIEW
#TAMPILAN LOADING
def loading_animation(duration=2):
    start_time = time.time()
    animation = "|/-\\"
    idx = 0
    while time.time() - start_time < duration:
        sys.stdout.write('\r' + "<><><><><>    Loading " + animation[idx % len(animation)] + "    <><><><><>")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
        sys.stdout.write('\033[K')  # untuk membersihkan line di bawah cursor

#Function untuk memberikan delay sejenak 
def cleardelay():
    os.system("cls")
    time.sleep(0.8)
def delayclear():
    time.sleep(0.8) 
    os.system("cls")

def menu_urut():
    print("=============================================")
    print("==============   MENU URUTAN  ===============")
    print("=============================================")
    print("  1. Urutkan Berdasarkan Nama ")
    print("  2. Urutkan Berdasarkan Harga ")
    print("  3. Urutkan Berdasarkan Kategori ")
    print("  4. Urutkan Berdasarkan Rasa")
    print("  5. Cari Kue")
    print("=============================================")

def menuadmin():
    print("=============================================")
    print("========== Welcome To Sweet Bakery ==========")
    print("==============   MENU ADMIN   ===============")
    print("=============================================")
    print("  1. Tampilkan Produk ")
    print("  2. Tambahkan Produk ")
    print("  3. Hapus Produk ")
    print("  4. Edit Produk")
    print("  5. Tampilkan Riwayat Barang")
    print("  6. Keluar")
    print("=============================================")

def loginadmin():
    while True :
        os.system("cls")
        loading_animation()
        os.system("cls")
        print(40*"=")
        print("LOGIN ADMIN".center(40))
        print(40*"=")
        username = str.capitalize(input("Input username anda: "))
        password = getpass.getpass("Input password anda: ")
        # Validasi username dan password

    # Main program
        if username == "Admin" and password == "admin123":
            while True:
                cleardelay()
                menuadmin()
                choice = int(input("\t\t>> Input menu pilihan [1-6]: "))
                while True :
                    if choice == 1:
                        cleardelay()
                        menu_urut()
                        urut = int(input("\t\t>> Input menu pilihan [1-5]: "))
                        if urut == 1:
                            os.system("cls")
                            loading_animation()
                            os.system("cls")
                            print("Produk Telah Diurutkan Berdasarkan Nama")
                            delayclear()
                            merge_sort_wrapper_nama()
                            input("Tekan Enter Untuk Lanjut...")
                            break
                        elif urut == 2:
                            os.system("cls")
                            loading_animation()
                            os.system("cls")
                            print("Produk Telah Diurutkan Berdasarkan Harga")
                            delayclear()
                            merge_sort_wrapper_harga()
                            input("Tekan Enter Untuk Lanjut...")
                            break
                        elif urut == 3:
                            os.system("cls")
                            loading_animation()
                            os.system("cls")
                            print("Produk Telah Diurutkan Berdasarkan Kategori")
                            delayclear()
                            merge_sort_wrapper_kategori()
                            input("Tekan Enter Untuk Lanjut...")
                            break
                        elif urut == 4:
                            os.system("cls")
                            loading_animation()
                            os.system("cls")
                            print("Produk Telah Diurutkan Berdasarkan Rasa")
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
                        delayclear()
                        name = str.title(input("Input nama produk baru  : "))
                        check = barang.find_one({"name": name})
                        if check is not None:
                            print("Produk Sudah Tersedia")
                        elif check is None :
                            price = int(input("Input harga             : "))
                            if price > 1000000 or price <= 0:
                                delayclear()
                                print("Inputan Harga Tidak Boleh Lebih Dari 1000000 dan Tidak Boleh Kosong!")
                                input("Tekan Enter Untuk Lanjut...")
                            else:
                                category = str.title(input("Input kategori produk   : "))
                                if category.isnumeric():
                                    delayclear()
                                    print("="*40)
                                    print("Inputan Harus Berupa Huruf!".center(40))
                                    print("="*40)
                                    input("Tekan Enter Untuk Lanjut...")
                                else:
                                    flavour = str.title(input("Input rasa produk       : "))
                                    if flavour.isnumeric():
                                        delayclear()
                                        print("="*40)
                                        print("Inputan Harus Berupa Huruf!".center(40))
                                        print("="*40)
                                        input("Tekan Enter Untuk Lanjut...")
                                    else:
                                        stock = int(input("Input jumlah stok       : "))
                                        if stock > 100 or stock <= 0:
                                            print("Inputan Stok Tidak Boleh Lebih Dari 100 dan Tidak Boleh Kosong!")
                                            input("Tekan Enter Untuk Lanjut...")
                                        else:
                                            update = shop(name, price, category, flavour, stock)
                                            bakery().add_product(update)
                                            os.system("cls")
                                            loading_animation()
                                            os.system("cls")
                                            print("Produk Baru Berhasil Ditambahkan")
                                            input("\n\nTekan Enter Untuk Lanjut...")
                                            break
                        else :
                            print("")
                            
                    elif choice == 3:
                        delayclear()
                        name = str.title(input("Masukan nama produk yang ingin dihapus : "))
                        cleardelay()
                        bakery().remove_product(name)
                        input("Tekan Enter Untuk Lanjut...")
                        break
                    elif choice == 4:
                        cleardelay()
                        bakery().show_product()
                        upd = str.title(input("Masukan nama produk yang ingin diubah : "))
                        cleardelay()
                        bakery().edit_product(upd)
                        input("Tekan Enter Untuk Lanjut...")
                        break
                    elif choice == 5:
                        os.system("cls")
                        loading_animation()
                        os.system("cls")
                        bakery().show_history()
                        input("Tekan Enter Untuk Lanjut...")
                        break
                    elif choice == 6:
                        delayclear()
                        return
                    else:
                        print("Pilihan Tidak Sesuai Mohon Coba Lagi")
                        delayclear()
                        break
        else :
            cleardelay()
            print("Invalid Login")
            delayclear()
            return

def menupelanggan():
    print("=============================================")
    print("========== Welcome To Sweet Bakery ==========")
    print("============   MENU PELANGGAN   =============")
    print("=============================================")
    print("  1. Tampilkan Produk ")
    print("  2. Beli Kue ")
    print("  3. Lihat Riwayat Pembelian")
    print("  4. Keluar")
    print("=============================================")

def loginuser():
    while True :
        os.system("cls")
        loading_animation()
        os.system("cls")
        print(40*"=")
        print("LOGIN AKUN".center(40))
        print(40*"=")
        usn = str.capitalize(input("Masukkan nama pengguna : "))
        password = getpass.getpass("Masukkan kata sandi    : ")
        result = pelanggan.find_one({"name": usn})
        if result is None:
            print("Nama Pengguna Tidak Terdaftar.")
            delayclear()
            return
        elif result["password"] != password:
            print("Kata Sandi Salah.")
            delayclear()
            return
        else:
            cleardelay()
            print("="*50)
            print("Selamat datang",usn.center(50))
            print("="*50)
            delayclear()
            print("="*50)
            print("Selamat Berbelanja".center(50))
            print("="*50)
            delayclear()
            while True:
                    os.system("cls")
                    loading_animation()
                    os.system("cls")
                    menupelanggan()
                    choice = int(input("\t\t>> Input menu pilihan [1-4]: "))
                    if choice == 1:
                        cleardelay()
                        menu_urut()
                        urut = int(input(">> Input menu pilihan [1-5]: "))
                        if urut == 1:
                            os.system("cls")
                            loading_animation()
                            os.system("cls")
                            print("Produk Telah Diurutkan Berdasarkan Nama")
                            delayclear()
                            merge_sort_wrapper_nama()
                            input("Tekan Enter Untuk Lanjut...")

                        elif urut == 2:
                            os.system("cls")
                            loading_animation()
                            os.system("cls")
                            print("Produk Telah Diurutkan Berdasarkan Harga")
                            delayclear()
                            merge_sort_wrapper_harga()
                            input("Tekan Enter Untuk Lanjut...")

                        elif urut == 3:
                            os.system("cls")
                            loading_animation()
                            os.system("cls")
                            print("Produk Telah Diurutkan Berdasarkan Kategori")
                            delayclear()
                            merge_sort_wrapper_kategori()
                            input("Tekan Enter Untuk Lanjut...")
        
                        elif urut == 4:
                            os.system("cls")
                            loading_animation()
                            os.system("cls")
                            print("Produk Telah Diurutkan Berdasarkan Rasa")
                            delayclear()
                            merge_sort_wrapper_rasa()
                            input("Tekan Enter Untuk Lanjut...")
                            
                        elif urut == 5:
                            bakery().search()

                        else :
                            print("Invalid!")
                            
                    elif choice == 2:
                        os.system("cls")
                        loading_animation()
                        os.system("cls")
                        bakery().belanja(usn)
                    
                    elif choice == 3:
                        os.system("cls")
                        loading_animation()
                        os.system("cls")
                        bakery().transaction_history(usn)
                    elif choice == 4:
                        delayclear()
                        return
                    else:
                        print("Pilihan Tidak Sesuai, Mohon Coba Lagi")
                        delayclear()

def program():
    while True :
        os.system("cls")
        print("=============================================")
        print("================= MENU LOGIN ================")
        print("=============================================")
        print("  1. Login Admin ")
        print("  2. Login Pelanggan ")
        print("  3. Registrasi Pelanggan")
        print("  4. Keluar")
        print("=============================================")
        try : 
            choice = int(input("\t\t>> Input Menu Pilihan [1-4]: "))
            if choice == 1:
                loginadmin()
            elif choice == 2:
                loginuser()
            elif choice == 3:
                os.system("cls")
                loading_animation()
                os.system("cls")
                print(40*"=")
                print("REGISTRASI AKUN".center(40))
                print(40*"=")
                regisUser = str.capitalize(input("Masukkan nama pengguna baru : "))
                regisPass = getpass.getpass("Masukkan Kata sandi baru    : ")
                result = pelanggan.find_one({"name": regisUser})
                if not regisUser.strip() or not regisPass.strip():
                    print("Nama Pengguna atau Kata Sandi Tidak Boleh Kosong")
                    delayclear()
                elif result is not None:
                    print("Nama Pengguna Sudah Terdaftar")
                    delayclear()
                elif not regisUser.isalnum():
                    print("Nama Pengguna Hanya Boleh Terdiri Dari Huruf dan Angka")
                    delayclear()
                elif not regisPass.isnumeric():
                    print("Kata Sandi Hanya Boleh Terdiri Dari Angka")
                    delayclear()
                else:
                    user_data = {
                        "name": regisUser,
                        "password": regisPass
                    }
                    pelanggan.insert_one(user_data)
                    print(40*"=")
                    print("Registrasi Akun Pembeli Berhasil Dilakukan")
                    print(40*"=")
                    input("Tekan Enter Untuk Lanjut...")
            elif choice == 4 :
                cleardelay()
                print(60*"=")
                print(" Terimakasih Sudah Menggunakan Layanan Kami :) ".center(60))
                print(60*"=")
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
            print("Key yang Diinput Tidak Sesuai, Anda Dialihkan Ke Menu Utama!")
            delayclear()
program()
