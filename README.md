# Program Penjualan Toko Roti


## 🧶Disusun oleh
### KELOMPOK: 3 / A / 2022
  - M. Haykal Fajjar Aulia (2209116018)
  - Dinda Nur Aini (2209116023)
  - Intan Melani Sukma (2209116028)

## 🎐Program Description
Program ini merupakan program penjualan yang dibangun untuk mempermudah pengelolaan toko roti. Program ini dapat mendata mulai dari pendataan stok hingga pendataan riwayat penjualan roti. Program penjualan toko roti ini dibangun dengan menerapkan konsep MVC.
- Adapun tujuan dari program ini yaitu:
1. Memudahkan pelaku bisnis untuk melakukan pendataan.
2. Memudahkan pelaku bisnis untuk mendata stok produk dan mencatat transaksi pembelian.
3. Mempermudah konsumen dalam proses melakukan pembelian.
4. Memudahkan dalam pengembangan dan pemeliharaan kode dengan penerapan konsep MVC.
5. Menambah keterampilan dalam penerapan materi yang telah diajarkan selama praktikum berlangsung.

## ⚙️Structure

Program Toko Roti dibangun dengan konsep MVC. Konsep ini membagi program menjadi tiga bagian yang terpisah sehingga memudahkan dalam pengembangan dan pemeliharaan kode.

#### Library

> [PrettyTable](https://pypi.org/project/prettytable/),
[os](https://docs.python.org/3/library/os.html),
[time](https://docs.python.org/3/library/time.html),
[getpass](https://docs.python.org/3/library/getpass.html),
[math](https://docs.python.org/3/library/math.html),
[sys](https://docs.python.org/3/library/sys.html),
[datetime](https://docs.python.org/3/library/datetime.html)

### Model:

Database: [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try4?utm_source=bing&utm_campaign=search_bs_pl_evergreen_atlas_core_prosp-brand_gic-null_apac-id_ps-all_desktop_eng_lead&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=415204525&adgroup=1212761794897445&msclkid=510029f330dd1bc5c99a4dccbb44d6e5)

Linked List: shop, bakery

### Controller:

Linked List:
- shop
- bakery
  - add product
  - remove product
  - edit product
  - show product
  - show history
  - belanja
  - transaction history
  - search
    searching menggunakan jump search
Fungsi:
- def sort nama
  sorting menggunakan merge sort
- def sort harga
- def sort kategori
- def sort rasa

### View:

Fungsi:
- def cleardelay
- def delayclear
- def menu urut
- def menu admin
- def login admin
- def menu pelanggan
- def login user
- def program

#### Penjelasan

- **Model**: Berisi komponen yang berkaitan dengan data, yaitu database dan linked list.
- **Controller**: Berisi fungsi-fungsi yang mengontrol dan mengelola data, serta menjembatani antara model dan view.
- **View**: Berisi fungsi-fungsi yang menampilkan output program kepada admin dan pelanggan.

Database:
- Database MongoDB digunakan untuk menyimpan data dengan struktur dokumen.

Library:
- Library PrettyTable digunakan untuk membuat tabel yang mudah dibaca pada program. 
- Library os digunakan untuk membersihkan layar.
- Library time digunakan untuk mengakses waktu. 
- Library getpass digunakan untuk menerima input password tanpa menampilkannya. 
- Library math digunakan untuk melakukan operasi matematika.
- Library sys digunakan untuk mengakses argumen baris perintah dan variabel sistem.
- Library datetime digunakan untuk mengakses tanggal.

Linked List:

- shop: berisi deskripsi produk yang ditawarkan di toko.
- bakery: berisi semua fungsi dan fitur yang berkaitan dengan pengelolaan produk.
  - add product: menambahkan produk baru ke dalam daftar produk.
  - remove product: menghapus produk dari daftar produk.
  - edit product: mengedit deskripsi produk yang ada di toko.
  - show product: menampilkan semua produk yang tersedia di toko.
  - show history: menampilkan riwayat transaksi atau pembelian yang dilakukan di toko.
  - belanja: memungkinkan pengguna untuk memilih dan membeli produk dari toko/bakery.
  - transaction history: menampilkan semua transaksi atau pembelian yang dilakukan oleh pengguna.
  - search: mencari produk yang tersedia di toko/bakery berdasarkan nama produk.

Fungsi:
- def cleardelay: digunakan untuk membersihkan tampilan program dan menambahkan jeda dalam program.
- def delayclear: digunakan menambahkan jeda dalam kode dan membersihkan tampilan program.
- def sort nama: digunakan untuk mengurutkan produk berdasarkan nama.
- def sort harga: digunakan untuk mengurutkan produk berdasarkan harga.
- def sort kategori: digunakan untuk mengurutkan produk berdasarkan kategori atau jenis.
- def sort rasa: digunakan untuk mengurutkan produk berdasarkan rasa.
- def menu urut: digunakan untuk menampilkan menu pengurutan produk.
- def menu admin: digunakan untuk menampilkan menu pengelolaan produk bagi admin.
- def login admin: digunakan untuk proses login sebagai admin.
- def menu pelanggan: digunakan untuk menampilkan menu pembelian bagi pelanggan.
- def login user: digunakan untuk proses login sebagai pelanggan.
- def program: digunakan untuk menjalankan program aplikasi yang dibuat.

## 🍞Features🍞
- Pembeli
  - Registrasi Pelanggan
  - Login Pelanggan
  - Tampilkan Produk
  - Beli Kue
  - Lihat Riwayat Pembelian
  - Belanja

- Admin
  - Login Admin
  - Tampilkan Produk
  - Tambahkan Produk
  - Hapus Produk
  - Edit Produk
  - Tampilkan Riwayat
  - Keluar

### Fungsionalitas
- Pembeli dapat meregistrasi diri untuk mendapatkan akun untuk masuk ke dalam program.
- Pembeli dapat masuk ke program dengan melakukan login menggunakan akun yang dimiliki.
- Pembeli dapat melihat menu dan melakukan pembelian.
- Pembeli dapat melihat riwayat transaksi.
- Pembeli dan Admin dapat memilih mengurutkan menu berdasarkan nama dan harga.
- Admin memilikI akun yang dapat digunakan untuk masuk ke dalam program.
- Admin dapat melihat, menambah, menghapus, dan mengedit produk.
- Admin dapat melihat history produk yang ditambah dan dihapus.

## 📜Cara Penggunaan

#### Menu Awal

Pada awal program di run, program akan menampilkan menu awal yang berisi 4 pilihan yaitu Login Admin, Login Pelanggan, Registrasi Pelanggan, dan Keluar.

![image](https://user-images.githubusercontent.com/127454468/232953396-cd507db7-d551-401a-9a55-c40fe4e44618.png)

### 🥨**User**🥨
#### Registrasi Pelanggan

Jika pelanggan belum memiliki akun, maka dapat memilih menu awal `opsi ke-3` untuk registrasi akun. Di menu registrasi, pelanggan akan diminta untuk memasukkan username dan password baru.

![Screenshot 2023-04-19 110721](https://user-images.githubusercontent.com/127454468/232958807-0ea18d5d-75dc-4620-90fe-58b076b5445a.png)

Jika pelanggan memasukkan username yang sudah terdaftar

![regis nama udah ada](https://user-images.githubusercontent.com/126852536/234757415-c40b9215-9b46-4d68-ba34-72409aeac9f6.png)

Jika pelanggan masukkan username dengan menggunakan karakter

![regis pake karakter](https://user-images.githubusercontent.com/126852536/234757560-3c11d7c2-c241-41c9-865a-c7ccd7f11e9d.png)

Jika pelanggan memasukkan username atau sandi kosong

![regis kosong](https://user-images.githubusercontent.com/126852536/234757677-d80ef1a3-2464-4be9-a594-b7f37609c4b0.png)

Jika sandi yang dimasukkan bukan angka

![regis sandi bukan angka](https://user-images.githubusercontent.com/126852536/234761019-94ee4734-73fc-454a-8c7d-5549bcbb5fc0.png)


Setelah registrasi maka program akan kembali ke menu awal dan pelanggan dapat memasukkan username dan password yang telah didaftarkan di menu `login pelanggan`.
####  Login Pelanggan

Di menu ini, pelanggan harus memilih menu awal `opsi ke-2` dan memasukkan username dan password untuk bisa masuk ke dalam program.

![Screenshot 2023-04-19 110733](https://user-images.githubusercontent.com/127454468/232958790-28e83f6c-c744-4365-a8a6-dcda75ccbb77.png)

Jika username atau password yang dimasukan salah, maka login akan gagal dan program kembali ke `Menu Awal`.
```
Tampilan jika username salah
```
![image](https://user-images.githubusercontent.com/127454468/233548555-f143681c-aa7b-4db6-83a1-0a535576528f.png)
```
Tampilan jika password salah
```
![image](https://user-images.githubusercontent.com/127454468/233548604-8e03369e-ed35-4689-9599-6c419734d60b.png)

- Menu Pelanggan

Jika login berhasil, maka program akan memunculkan menu pelanggan yang terdiri dari 3 pilihan, yaitu Tampilkan Produk, Beli Kue, Lihat Riwayat Pembelian, dan Keluar.

![image](https://user-images.githubusercontent.com/127454468/232956243-f7be77c5-9b46-4c78-96f2-82f4b554ed55.png)

Untuk mengakses setiap menu, pelanggan akan diminta untuk menginputkan angka. Berikut tampilan jika salah menginputkan kode menu pelanggan

![salah input menu pelanggan](https://user-images.githubusercontent.com/126852536/234038176-c8ac8411-a306-4f9b-870b-fd7e3e5a7010.png)

1.Tampilkan Produk Yang Tersedia

Jika ingin melihat produk maka pelanggan dapat memilih `menu pelanggan ke-1`, setelah memilih menu, pelanggan dapat memilih apakah ingin melihat menu yang diurutkan berdasarkan nama atau diurutkan berdasarkan harga.

![image](https://user-images.githubusercontent.com/127454468/232958603-f2de33cc-cbe7-4f0b-97a3-d8cd72854ae9.png)
##### - Jika produk diurutkan berdasarkan nama
  
![image](https://user-images.githubusercontent.com/127454468/232953664-f1335b19-fe2a-45df-a305-52f3f4c1f3a3.png)

##### - Jika produk diurukan berdasarkan harga

![image](https://user-images.githubusercontent.com/127454468/232953764-b4c8fba5-9b06-42d1-9b1d-060f20d970c4.png)

##### - Jika produk diurukan berdasarkan kategori

![image](https://user-images.githubusercontent.com/127454468/232953832-7f1c310d-620d-4aba-b494-f65dc871e1dc.png)

##### - Jika produk diurukan berdasarkan rasa

![image](https://user-images.githubusercontent.com/127454468/232953911-0e5b5d43-7427-4602-a4af-47d1b928d3af.png)

##### - Jika ingin mencari produk

![Screenshot 2023-04-19 104918](https://user-images.githubusercontent.com/127454468/232954219-77203e39-1e68-49f7-978e-f5dc04edf80a.png)
```
Program menampilkan produk yang dicari
```
![image](https://user-images.githubusercontent.com/127454468/232954091-b506f574-2c9b-48ab-b61b-fcf3ac384e54.png)
```
Tampilan jika program tidak menemukan produk yang dicari
```
![image](https://user-images.githubusercontent.com/127454468/233255416-c4f77443-1577-4969-811c-22997812bcaa.png)

2. Beli Kue

Jika ingin membeli produk, maka pelanggan dapat memilih `menu pelanggan ke-2`, setelah memilih menu, pelanggan akan diminta untuk memasukan produk yang ingin dibeli dan jumlah produk yang ingin dibeli. Jumlah yang dibeli tidak boleh kosong atau berjumlah 0.

![Screenshot 2023-04-19 110822](https://user-images.githubusercontent.com/127454468/232958223-03b7cc5d-07de-4c4c-8947-ae302b925954.png)
```
Selanjutnya, program akan memberikan rincian produk dan jumlah yang akan dibayarkan
```
![Screenshot 2023-04-24 212011](https://user-images.githubusercontent.com/126852536/234008975-9707a6f1-78b7-4aad-bbe8-3cfb1e29410d.png)
```
Lalu, program akan menanyakan apakah pelanggan ingin lanjut atau membatalkan transaksi
```
![Screenshot 2023-04-19 110531](https://user-images.githubusercontent.com/127454468/232958142-a410ce66-45ed-4c23-99eb-e59550fdf836.png)
```
Jika ingin melanjutkan ke pembayaran, pelanggan dapat memilih `y` dan program akan memberikan invoice pembelian
```
![Screenshot 2023-04-19 111254](https://user-images.githubusercontent.com/127454468/232958039-301b70fe-1558-457a-98c3-ffaae6865cd9.png)
```
Jika ingin tidak ingin melanjutkan ke pembayaran, pelanggan dapat memilih `t` dan program akan membatalkan pembelian
```
![Screenshot 2023-04-19 110838](https://user-images.githubusercontent.com/127454468/232958687-ae40835b-d751-4c49-8eb8-7b92b79ce687.png)
```
Tampilan jika jumlah stok tidak mencukupi
```
![image](https://user-images.githubusercontent.com/127454468/233255670-f7495170-b8c5-4d27-a69b-e50a567fb608.png)
```
Tampilan jika jumlah pembelian 0
```
![image](https://user-images.githubusercontent.com/127454468/233547904-276c12bb-9799-44ef-ba58-ae5158c5fdcc.png)
```
Tampilan jika produk tidak ditemukan
```
![image](https://user-images.githubusercontent.com/127454468/233546841-73a4d6ad-ddea-4ff3-9092-111303ffec76.png)

3. Lihat Riwayat Pembelian

Jika ingin melihat history pembelian maka pelanggan dapat memilih `menu pelanggan ke-4`, maka program akan menampilkan history produk yang pernah dibeli oleh pelanggan tersebut.

![Screenshot 2023-04-19 111031](https://user-images.githubusercontent.com/127454468/232990869-3c72f397-39be-41f5-90c0-1165b01313a6.png)
```
Tampilan jika pelanggan belum pernah melakukan pembelian
```
![image](https://user-images.githubusercontent.com/127454468/233255262-01da49a1-99c8-4af8-ba8f-6f5d12ab698f.png)

4. Keluar

Jika pelanggan telah selesai berbelanja, maka pelanggan dapat keluar program dengan memilih menu `Keluar`. Menu ini akan mengembalikan pelanggan ke `Menu Awal`.

### 🥐**Admin**🥐
#### Login Admin

Setelah program di run, admin harus memilih menu awal `opsi ke-1` lalu memasukkan username dan password yang benar untuk bisa masuk ke dalam program.

![image](https://user-images.githubusercontent.com/127454468/232953524-aae17784-5c12-4b01-aa6d-e87de2b092fa.png)

- Menu Admin

Jika login berhasil, maka program akan memunculkan menu admin yang terdiri dari 6 pilihan, yaitu Tampilkan Produk, Tambahkan Produk, Hapus Produk, Edit Produk, Tampilkan Riwayat, dan Keluar.

![Screenshot 2023-04-19 104307](https://user-images.githubusercontent.com/127454468/232959845-a4a9029e-66f0-47fa-a78e-02f1cb897f6c.png)

Jika username atau password salah, maka login akan gagal dan program akan kembali ke menu awal.
```
Tampilan jika login gagal
```
![image](https://user-images.githubusercontent.com/127454468/233548314-7d64502b-ba58-4a80-9de8-dfc56b84a500.png)

Untuk mengakses menu admin, admin akan diminta untuk memasukkan angka yang mewakili setiap opsi program. Jika admin salah memasukkan opsi program maka akan muncul tampilan

![Screenshot 2023-04-27 115726](https://user-images.githubusercontent.com/126852536/234761772-912b91fd-de0c-44f0-adac-01bab5b01748.png)


1. Tampilkan Produk

Jika ingin melihat produk yang tersedia maka admin dapat memilih `menu admin ke-1`, setelah memilih menu, admin dapat memilih apakah ingin melihat menu yang diurutkan berdasarkan nama atau diurutkan berdasarkan harga.

![image](https://user-images.githubusercontent.com/127454468/232958639-da81a720-faac-4198-b831-f6ebcbc4831a.png)

##### - Jika produk diurutkan berdasarkan nama
  
![image](https://user-images.githubusercontent.com/127454468/232953664-f1335b19-fe2a-45df-a305-52f3f4c1f3a3.png)

##### - Jika produk diurukan berdasarkan harga

![image](https://user-images.githubusercontent.com/127454468/232953764-b4c8fba5-9b06-42d1-9b1d-060f20d970c4.png)

##### - Jika produk diurukan berdasarkan kategori

![image](https://user-images.githubusercontent.com/127454468/232953832-7f1c310d-620d-4aba-b494-f65dc871e1dc.png)

##### - Jika produk diurukan berdasarkan rasa

![image](https://user-images.githubusercontent.com/127454468/232953911-0e5b5d43-7427-4602-a4af-47d1b928d3af.png)

##### - Jika ingin mencari produk

![Screenshot 2023-04-19 104918](https://user-images.githubusercontent.com/127454468/232954219-77203e39-1e68-49f7-978e-f5dc04edf80a.png)
```
Program menampilkan produk yang dicari
```
![image](https://user-images.githubusercontent.com/127454468/232954091-b506f574-2c9b-48ab-b61b-fcf3ac384e54.png)
```
Tampilan jika program tidak menemukan produk yang dicari
```
![image](https://user-images.githubusercontent.com/127454468/233255416-c4f77443-1577-4969-811c-22997812bcaa.png)

2. Tambahkan Produk

Untuk menambahkan produk baru maka admin dapat memilih `menu admin ke-2`, setelah memilih menu, admin akan diminta untuk menginput Nama Produk, Harga, Kategori Produk, Jenis Rasa Produk, dan Jumlah Stok.

![Screenshot 2023-04-19 105326](https://user-images.githubusercontent.com/127454468/232954849-2699bf8e-1706-47a8-887c-850a5d1628b1.png)
```
Tampilan jika produk berhasil ditambahkan
```
![image](https://user-images.githubusercontent.com/127454468/232954795-359285d7-d570-4c5a-9620-3fd9765de33b.png)
```
Produk baru otomatis akan di urutkan di dalam list produk
```
![image](https://user-images.githubusercontent.com/127454468/232955008-2f683823-519c-4a44-810a-f7c8c53e4600.png)
```
Tampilan jika kue yang ditambahkan sudah ada didalam menu
```
![kue udah ada](https://user-images.githubusercontent.com/126852536/234040567-c9ae4443-396b-4f9e-8fdf-b0ee57708077.png)
```
Tampilan jika harga kue yang ditambahkan lebih dari 1000000 atau kosong
```
![salah harga](https://user-images.githubusercontent.com/126852536/234041186-7b0061de-b3e7-4f97-bcdf-09fbba8e5510.png)
```
Tampilan jika stok kue yang ditambahkan lebih dari 100 atau kosong
```
![salah stok](https://user-images.githubusercontent.com/126852536/234041238-326bc8a2-458e-4930-9003-c02d363abf6d.png)
```
Tampilan jika inputan kategori dan rasa kue berupa angka
```
![harus huruf](https://user-images.githubusercontent.com/126852536/234041291-01a018e9-7ad5-4ae0-b5bd-30ddc85b130e.png)

3. Hapus Produk

Untuk menghapus produk yang telah ada maka admin dapat memilih `menu admin ke-3`, setelah memilih menu, admin akan diminta untuk menginput nama produk yang ingin dihapus.

![image](https://user-images.githubusercontent.com/127454468/232955155-2055f8af-6afc-4f0d-8535-18c589289eee.png)
```
Tampilan jika produk berhasil dihapus
```
![image](https://user-images.githubusercontent.com/127454468/232955200-9e33177c-149a-40dd-8136-70457def4bc7.png)
```
Tampilan jika produk tidak ada di dalam menu
```
![hapus produk gada](https://user-images.githubusercontent.com/126852536/234761893-0842bd49-e482-40e0-aa2c-67e942104ff3.png)


4. Edit Produk

Jika ingin mengedit produk yang telah ada maka admin dapat memilih `menu admin ke-4`. Setelah memilih menu, admin akan diminta untuk memasukan nama produk yang ingin diubah lalu memilih apakah ingin mengubah stok atau harga produk.

![image](https://user-images.githubusercontent.com/127454468/232955474-b36a3b14-d7fb-454d-a118-9349e667a1fd.png)
```
Jika admin ingin mengubah stok
```
![Screenshot 2023-04-19 105931](https://user-images.githubusercontent.com/127454468/232955843-f2c95d27-e960-40c9-a78f-9bb770128656.png)
```
Tampilan jika produk berhasil diubah
```
![Screenshot 2023-04-19 105938](https://user-images.githubusercontent.com/127454468/232955815-64bebad8-4ff6-4ba6-a57c-01e6439a8e47.png)
```
Tampilan jika stok yang diubah lebih dari 100 atau kosong
```
![edit kelebihan stok](https://user-images.githubusercontent.com/126852536/234762054-8d21b502-d9e0-49ec-99b9-cce4a123acaa.png)
```
Jika admin ingin mengubah harga
```
![Screenshot 2023-04-19 144114](https://user-images.githubusercontent.com/127454468/232988414-80fdcce9-9884-43a8-a805-02368cdce008.png)
```
Tampilan jika harga yang diubah lebih dari 1000000 atau kosong
```
![edit harga kelebihan](https://user-images.githubusercontent.com/126852536/234762208-2c682bb1-f3d0-4a7a-8bce-3ece2a38956c.png)
```
Tampilan produk yang telah diubah stok dan harganya
```
![Screenshot 2023-04-19 144143](https://user-images.githubusercontent.com/127454468/232988351-5dbf7fd4-6f30-4b00-8114-28078167a964.png)
```
Tampilan jika produk yang di input tidak ditemukan
```
![Screenshot 2023-04-19 144038](https://user-images.githubusercontent.com/127454468/232988373-57c9e7b5-3d13-4394-b4c1-39678581b7a8.png)

5. Tampilkan Riwayat

Jika ingin melihat history produk maka admin dapat memilih `menu admin ke-4`, maka program akan menampilkan riwayat produk yang telah ditambahkan dan dihapus.

![Screenshot 2023-04-19 110009](https://user-images.githubusercontent.com/127454468/232955777-c75e3cce-1b41-44a5-8db3-cba393324c90.png)

6. Keluar

Jika admin telah selesai menggunakan program, maka admin dapat keluar program dengan memilih menu `Keluar`. Menu ini akan mengembalikan admin ke `Menu Awal`.

#### Keluar
Jika ingin keluar dari program maka admin dan pelanggan dapat memilih `menu awal ke-4` untuk dapat keluar dari program.

![image](https://user-images.githubusercontent.com/127454468/232956070-7fbfbca9-5888-493f-8fa8-af487896efd7.png)
