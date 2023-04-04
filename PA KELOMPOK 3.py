from prettytable import PrettyTable
import os
import time
import getpass
import math
import sys
os.system("cls")

admin ={"User"  :["admin"],
        "Sandi" :["admin123"]}

userbiasa={"User"  :["haykal","intan","dinda"],
            "Sandi" :["111","222","123"],
            "NIM"   :["2209116018", "2209116028", "2209116023"]}

#Ini function untuk memberikan delay sejenak 
def cleardelay():
    os.system("cls")
    time.sleep(0.8)

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
            return
        elif self.head.name == name:
            self.head = self.head.next
            self.history.append(('remove', name))
            return
        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                self.history.append(('remove', name))
                return
            current = current.next

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
        
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        mid = self.get_mid(head)
        left = head
        right = mid.next
        mid.next = None
        left_sorted = self.merge_sort(left)
        right_sorted = self.merge_sort(right)
        return self.merge(left_sorted, right_sorted)

    def get_mid(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left
        elif left.price <= right.price:
            left.next = self.merge(left.next, right)
            return left
        else:
            right.next = self.merge(left, right.next)
            return right

    def sort_by_price(self):
        self.head = self.merge_sort(self.head)
        
def tampilkanproduk():
    b = bakery()
    b.add_product(shop("Black Forest", "150.000", "Kue Tart", "Cokelat", 5))
    b.add_product(shop("Cheese Cake", "100.000", "Kue Tart", "Keju", 7))
    b.add_product(shop("Chiffon Cake", "120.000", "Kue Tart", "Pandan", 4))
    b.add_product(shop("Sponge Cake", "90.000", "Kue Tart", "Vanilla", 10))
    b.add_product(shop("Matcha Lava Cake", "190.000", "Kue Tart", "Matcha", 2))
    b.sort_by_price()
    b.show_product()
    input("Tekan Enter Untuk Lanjut...")

#=====SEARCHING DATA====================================================
def jumpSearch( array , namaproduct , n ):
    x = namaproduct
    step = math.sqrt(n)
    prev = 0
    
    while array[int(min(step, n)-1)]["Nama Produk"].lower() < x.lower():
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while array[int(prev)]["Nama Produk"].lower() < x.lower():
        prev += 1
        if prev == min(step, n):
            return -1

    if array[int(prev)]["Nama Produk"].lower() == x.lower(): 
        return prev
     
    return -1

def tampilAnggota(): #Menampilkan Member
    z = PrettyTable
    z.clear()
    z.field_names = ["No","Nama","NIM"]
    z.reversesort = True
    for i in range(len(userbiasa["User"])):
        z.add_row([i+1,userbiasa["User"][i],regisuser["NIM"][i]])
    z.align["No"] = "l"
    z.align["Nama"] = "l"
    z.align["NIM"] = "l"

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

def regisuser():
    while True:
        regisUser = input("Input User Baru: ")
        regisPass = getpass.getpass("Input Password baru: ")
        if regisUser in admin["User"] or regisUser in userbiasa["User"]:
            print("Maaf Username Dengan Nama Tersebut Sudah Ada")
        elif any(x.isnumeric() for x in regisUser):
            print ("Mohon Untuk Memasukan Angka Sebagai Password")
        elif any(x.isalpha() for x in regisUser) and any(x.isalpha() or x.isnumeric() for x in regisPass):
            admin["User"].append(regisUser)
            admin["Sandi"].append(regisPass)
            break
        else:
            print("Tolong Masukan Input Dengan Benar")

def menuadmin():
    print("<><><><><> Welcome To Sweet Bakery <><><><><>")
    print("  <><><><><>   Bakery  Menu   <><><><><>")
    print("1. Tampilkan Produk Yang Tersedia")
    print("2. Tambahkan Produk Baru ke dalam List")
    print("3. Hapus Produk Dari List")
    print("4. Tampilkan History")
    print("5. Urutkan Harga")
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
                os.system("cls")
                menuadmin()
                choice = int(input("\nInput Opsi (1-6): "))
                if choice == 1:
                    cleardelay()
                    store.show_product()
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == 2:
                    name = input("Input Nama Produk Baru  : ")
                    price = input("Input Harga             : ")
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
                    store.remove_product(name)
                    cleardelay()
                    print("Produk Telah Berhasil Dihapus")
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == 4:
                    cleardelay()
                    store.show_history()
                    input("Tekan Enter Untuk Lanjut...")
                elif choice == 5:
                    tampilkanproduk()
                    # time.sleep(1)
                elif choice == 6:
                    raise SystemExit
                else:
                    print("Pilihan Tidak Sesuai Mohon Coba Lagi")
                    time.sleep(0.8)
        else :
            print("Invalid Login")
        
def loginuser():
    usn = input("Input username anda: ")
    pasw = getpass.getpass("Input password anda: ")
        index = userbiasa["User"].index(usn)
    if usn == userbiasa["User"][index] and pasw == userbiasa["Sandi"][index]:
        print("Selamat datang", usn)
        #cleardelay()
    else: 
        print("Username atau Password Salah")
def menupelanggan():
    print("<><><><><> Welcome To Sweet Bakery <><><><><>")
    print("  <><><><><>   Bakery  Menu   <><><><><>")
    print("1. Tampilkan Produk Yang Tersedia")
    print("2. Shopping")
    print("3. Exit")

print(". . . . . .<><><><><>. . . . . .<><><><><>. . . . . .")
print("1. Login Admin")
print("2. Login Pelanggan")
print("3. Registrasi Pelanggan")
print("4. Exit")
print(". . . . . .<><><><><>. . . . . .<><><><><>. . . . . .")
choice = int(input("Input Opsi (1-4): "))
while True :
    if choice == 1:
        loginadmin()
    elif choice == 2:
        loginuser()
    elif choice == 3:
        regisuser()
    elif choice == 4 :
        raise SystemExit
    else :
        print("Invalid Login")
