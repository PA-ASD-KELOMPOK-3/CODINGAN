from prettytable import PrettyTable
import os
import time
import getpass
import math
import sys
import json
import datetime
os.system("cls")

admin ={"User"  :["admin"],
        "Sandi" :["admin123"]}

userbiasa={"User"  :["haykal","intan","dinda"],
            "Sandi" :["111","222","123"]}

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

class bakery:
    def __init__(self):
        self.head = None
        #history sama dengan list kosong yang nantinya akan terisi
        self.history = []
        self.transactions = []

    #function menambah produk
    def add_product(self, cake):
        if self.head is None:
            self.head = cake
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = cake
        self.history.append(('add', cake.name, cake.price, cake.category, cake.flavour, cake.stock))

    #function menghapus Produk
    def remove_product(self, name):
        if self.head is None:
            print("Produk Tidak Ditemukan")
            return
        elif self.head.name == name:
            self.head = self.head.next
            self.history.append(('remove', name))
            print("Produk Telah Berhasil Dihapus")
            return
        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                self.history.append(('remove', name))
                print("Produk Telah Berhasil Dihapus")
                return
            current = current.next
            print("Produk Tidak Ditemukan")
            break
                
    #Function mengubah produk
    def edit_product(self, name):
        if self.head is None:
            print("Produk Tidak Ditemukan")
            return
        current = self.head
        while current is not None:
            if current.name.lower() == name.lower():
                print("Produk yang akan diubah:", current.name)
                field_name = input("Masukkan Jenis yang ingin diubah (harga/stok): ")
                new_value = int(input("Masukkan Data Baru: "))
                if field_name == "harga" : 
                    if len(new_value) > 1000000:
                        print("Inputan Harga Tidak Boleh Lebih dari 1 Juta dan Tidak boleh kosong")
                    else :
                        current.price = new_value
                if field_name == "stok" :
                    if len(new_value) > 100 or len(new_value) <=0 :
                        print("Inputan Stok Tidak Boleh Lebih dari 100 dan Tidak boleh kosong")
                    else :    
                        current.stock = new_value
                    
                print("Jenis yang dimasukan tidak sesuai")
                return
                self.history.append(('edit', name, field_name, new_value))
                cleardelay()
                print(40*"=")
                print("      Produk berhasil diubah")
                print(40*"=")
                return
            current = current.next
        print("Produk Tidak Ditemukan")

    #function menampilkan Produk
    def show_product(self):
        table = PrettyTable()
        table.title = "Produk Yang Tersedia"
        table.field_names = ["Nama Kue", "Harga", "Kategori", "Rasa", "Stok"]
        if self.head is None:
            print("Daftar Produk yang Tersedia Sedang Kosong")
        else:
            current = self.head
            while current is not None:
                table.add_row([current.name, current.price, current.category, current.flavour, current.stock])
                current = current.next
            print(table)

    #function menampilkan history
    def show_history(self):
        table = PrettyTable()
        table.title = "History"
        table.field_names = ["Keterangan", "Nama Produk", "Harga", "Kategori", "Rasa", "Stok"]
        if self.head is None:
            print("         History Masih Kosong           ")
        else:
            for item in self.history:
                if item[0] == 'add':
                    table.add_row(['Ditambahkan', item[1], item[2], item[3], item[4], item[5]])
                elif item[0] == 'remove':
                    table.add_row(['Dihapus', item[1], '-', '-', '-', '-'])
            print(table)
        
    def add_transaction(self, name, price): 
        now = datetime.datetime.now()
        transaction = {
            'name': name,
            'harga': price,
            # 'jumlah': jumlah_beli,
            # 'total' : total_harga,
            'date': now.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction)

    #JUMP SEARCH DESKRIPSI PRODUK
    def jump_search(self, name):
        if self.head is None:
            return None
        
        # hitung ukuran step yang akan digunakan
        n = 0
        current = self.head
        while current is not None:
            n += 1
            current = current.next
        step = int(math.sqrt(n))
        
        # lakukan jump search
        prev = None
        current = self.head
        while current is not None and current.name.lower() < name.lower():
            prev = current
            for i in range(step):
                current = current.next
                if current is None:
                    break
        
        # jika nama produk ditemukan, tampilkan deskripsinya
        if current is not None and current.name.lower() == name.lower():
            cleardelay()
            print(40*"=")
            print("Nama Kue : ", current.name)
            print("Harga    : ", current.price)
            print("Kategori : ", current.category)
            print("Rasa     : ", current.flavour)
            print("Stok     : ", current.stock)
        else:
            print("Produk tidak ditemukan.")

        
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
            if left_arr[i].name.lower() < right_arr[j].name.lower():
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



def merge_sort_wrapper_nama(store):
    product_list = []
    current = store.head
    while current is not None:
        product_list.append(current)
        current = current.next

    merge_sort_nama(product_list)

    store.head = product_list[0]
    current = store.head
    for i in range(1, len(product_list)):
        current.next = product_list[i]
        current = current.next
    current.next = None

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
            if int(left_arr[i].price) < int(right_arr[j].price):
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

def merge_sort_wrapper_harga(store):
    product_list = []
    current = store.head
    while current is not None:
        product_list.append(current)
        current = current.next

    merge_sort_harga(product_list)

    store.head = product_list[0]
    current = store.head
    for i in range(1, len(product_list)):
        current.next = product_list[i]
        current = current.next
    current.next = None


def ulang(): #Opsi Pengulangan
    if True:
        yt=input("Kembali ke Menu? (y/t): ")
        if yt=="y":
            pass
        elif yt=="t":   
            sys.exit("SEE YOU LATER~~")
        else:
            print("Maaf input tidak benar!")
            ulang()

store = bakery()
store.add_product(shop("Cheese Cake", 100000, "Kue Tart", "Keju", 7))
store.add_product(shop("Chiffon Cake", 120000, "Kue Tart", "Pandan", 4))
store.add_product(shop("Matcha Lava Cake", 190000, "Kue Tart", "Matcha", 2))
store.add_product(shop("Sponge Cake", 90000, "Kue Tart", "Vanilla", 10))
store.add_product(shop("Black Forest", 150000, "Kue Tart", "Cokelat", 5))        

def menu_urut():
    print("1. Urutkan Berdasarkan Nama")
    print("2. Urutkan Berdasarkan Harga")
    print("3. Cari Kue")

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
        username = input("Input Username Anda: ")
        password = getpass.getpass("Input Password Anda: ")
        # Validasi username dan password

    # Main program
        index = admin["User"].index(username)
        if username == admin["User"][index] and password == admin["Sandi"][index]:
            while True:
                cleardelay()
                print("<=><=><=><=> WELCOME ADMIN ^--^ <=><=><=><=>")
                menuadmin()
                choice = int(input("\nInput Opsi (1-6): "))
                if choice == 1:
                    cleardelay()
                    menu_urut()
                    urut = int(input("Pilih Opsi Urut Produk : "))
                    if urut == 1:
                        merge_sort_wrapper_nama(store)
                        cleardelay()
                        print("Produk telah diurutkan berdasarkan nama")
                        delayclear()
                        store.show_product()
                        input("Tekan Enter Untuk Lanjut...")
                    elif urut == 2:
                        merge_sort_wrapper_harga(store)
                        cleardelay()
                        print("Produk telah diurutkan berdasarkan harga!")
                        delayclear()
                        store.show_product()
                        input("Tekan Enter Untuk Lanjut...")
                    elif urut == 3:
                        cari = input("Masukan Nama Kue Yang Ingin Dicari : ")
                        store.jump_search(cari)
                        input("Tekan Enter Untuk Lanjut...")
                    else :
                        print("Invalid!")
                elif choice == 2:
                    name = input("Input Nama Produk Baru  : ")
                    price = int(input("Input Harga             : "))
                    category = input("Input Kategori Produk   : ")
                    flavour = input("Input Jenis Rasa Produk : ")
                    stock = int(input("Input Jumlah Stok       : "))
                    update = shop(name, price, category, flavour, stock)
                    store.add_product(update)
                    cleardelay()
                    print("Produk Baru Berhasil Ditambahkan")
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == 3:
                    name = input("Masukan Nama Produk yang Ingin Dihapus : ")
                    cleardelay()
                    store.remove_product(name)
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == 4:
                    cleardelay()
                    store.show_product()
                    upd = input("Masukan Nama Produk yang Ingin Diubah : ")
                    cleardelay()
                    store.edit_product(upd)
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == 5:
                    cleardelay()
                    store.show_history()
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == 6:
                    raise SystemExit
                else:
                    print("Pilihan Tidak Sesuai Mohon Coba Lagi")
                    time.sleep(0.8)
        else :
            print("Invalid Login")

def menupelanggan():
    print("<><><><><> Welcome To Sweet Bakery <><><><><>")
    print("  <><><><><>   Bakery  Menu   <><><><><>")
    print("1. Tampilkan Produk Yang Tersedia")
    print("2. Shopping")
    print("3. Exit")

def loginuser():
    usn = input("Input username anda: ")
    pasw = getpass.getpass("Input password anda: ")
    index = userbiasa["User"].index(usn)
    if usn == userbiasa["User"][index] and pasw == userbiasa["Sandi"][index]:
        cleardelay()
        print("<=><=><=><=> Selamat datang",usn,"<=><=><=><=>")
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
                        merge_sort_wrapper_nama(store)
                        cleardelay()
                        print("Produk telah diurutkan berdasarkan nama")
                        delayclear()
                        store.show_product()
                        input("Tekan Enter Untuk Lanjut...")
                    elif urut == 2:
                        merge_sort_wrapper_harga(store)
                        cleardelay()
                        print("Produk telah diurutkan berdasarkan harga!")
                        delayclear()
                        store.show_product()
                        input("Tekan Enter Untuk Lanjut...")
                    elif urut == 3:
                        cari = input("Masukan Nama Kue Yang Ingin Dicari : ")
                        store.jump_search(cari)
                        input("Tekan Enter Untuk Lanjut...")
                    else :
                        print("Invalid!")
                elif choice == 2:
                    store.show_product()
                    nama_kue = input("Masukkan Nama Kue         : ")
                    jumlah_beli = int(input("Masukkan Jumlah Pembelian : "))
                    cleardelay()
                    current = None
                    product_found = False
                    node = store.head
                    while node is not None:
                        if node.name == nama_kue:
                            current = node
                            product_found = True
                            break
                        node = node.next
                    if not product_found:
                        print(">> Kue Tidak Ditemukan <<\n\n")
                        input("Tekan Enter Untuk Lanjut...")
                    else:
                        if jumlah_beli > current.stock:
                            print(">> Maaf, stok kue tidak mencukupi <<\n\n")
                            input("Tekan Enter Untuk Lanjut...")
                        else:
                            total_harga = current.price * jumlah_beli
                            print("RINCIAN BELANJAAN".center(30)) #kalau bisa masukin pretty table aja
                            transaction = {"name": current.name,
                                        "price": current.price,
                                        "quantity": jumlah_beli,
                                        "total_price": total_harga,
                                        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                            print("Nama         : {}\nHarga Satuan : {} \nJumlah       : {} \nTotal Harga  : {} \nTanggal      : {}".format(
                                current.name, current.price, jumlah_beli, total_harga, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                            store.add_transaction(current.name, total_harga)
                            input("\n\nTekan Enter Untuk Lanjut...")
                            cleardelay()
                            tanya = input("Lanjutkan Pembayaran? [y/t]: ")
                            cleardelay()
                            if tanya == "y":
                                print("Membuat Struk Belanja..")
                                harganya = current.price
                                tanggal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                with open("transaction.txt", "a") as invoice:
                                    print("="*50, file=invoice)
                                    print(" STRUK BELANJA ".center(50,*"="), file=invoice)
                                    print("="*50, file=invoice)
                                    print(f"Nama Pelanggan: {usn}", file=invoice)
                                    print(f"Tanggal       : {tanggal}\n", file=invoice)
                                    print(f"   Nama Kue         : {nama_kue}", file=invoice)
                                    print(f"   Jumlah           : {jumlah_beli}", file=invoice)
                                    print(f"   Harga Satuan Kue : {harganya}", file=invoice)
                                    print(f"   Total Harga      : {total_harga}", file=invoice)
                                    print(f"   Tanggal          : {tanggal}\n", file=invoice) 
                                    print("="*50, file=invoice) 
                                    print(" TERIMA KASIH ".center(50,"="), file=invoice)
                                    print("="*50, "\n\n", file=invoice)
                                    delayclear()
                                    print(">> Transaksi berhasil")
                                    print("Terima kasih Berbelanja Di Toko Kami!\n\n")
                                    input("Tekan Enter Untuk Lanjut...")
                                    
                            elif tanya == "t":
                                print("Terima Kasih Sudah Berkunjung!\n\n")
                                input("Tekan Enter Untuk Lanjut...")
                elif choice == 3:
                    return
                else:
                    print("Pilihan Tidak Sesuai Mohon Coba Lagi")
                    time.sleep(0.8)
    else: 
        print("Username atau Password Salah")


def program():
    while True :
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
                regisUser = input("Input User Baru: ")
                regisPass = getpass.getpass("Input Password baru: ")
                if regisUser in admin["User"] or regisUser in userbiasa["User"]:
                    print("Maaf Username Dengan Nama Tersebut Sudah Ada")
                elif any(x.isalpha() for x in regisUser):
                    print ("Mohon Untuk Memasukan Angka Sebagai Password")
                elif any(x.isalpha() for x in regisUser) and any(x.isalpha() or x.isnumeric() for x in regisPass):
                    userbiasa["User"].append(regisUser)
                    userbiasa["Sandi"].append(regisPass)
                    cleardelay()
                    print ("Berhasil Melakukan Registrasi")
                    delayclear()
                else:
                    print("Tolong Masukan Input Dengan Benar")
            elif choice == 4 :
                raise SystemExit
            elif choice is not True or choice is str:
                cleardelay()
                print("Invalid Key1")
                delayclear()
        except ValueError :
            cleardelay()
            print("Invalid Key2")
            delayclear()
        except KeyboardInterrupt :
            cleardelay()
            print("Invalid Key3")
            delayclear()

program()
