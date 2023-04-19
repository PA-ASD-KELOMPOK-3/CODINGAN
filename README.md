# Program Penjualan Toko Roti

## 🧶Disusun oleh
### KELOMPOK: 3 / A / 2022
  - M. Haykal Fajjar Aulia (2209116018)
  - Dinda Nur Aini (2209116023)
  - Intan Melani Sukma (2209116028)

## 🎐Program Description
Program ini merupakan program penjualan yang dibangun untuk mempermudah pengelolaan toko roti. Program ini dapat mendata mulai dari pendataan stok hingga pendataan riwayat penjualan roti.
- Adapun tujuan dari program ini yaitu:
1. Memudahkan pelaku bisnis untuk melakukan pendataan.
2. Memudahkan pelaku bisnis untuk mendata stok produk dan mencatat transaksi pembelian.
3. Mempermudah konsumen dalam proses melakukan pembelian.
4. Menambah keterampilan dalam penerapan materi yang telah diajarkan selama praktikum berlangsung.

## ⚙️Structure

### Database
[MongoDB](https://www.mongodb.com/cloud/atlas/lp/try4?utm_source=bing&utm_campaign=search_bs_pl_evergreen_atlas_core_prosp-brand_gic-null_apac-id_ps-all_desktop_eng_lead&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=415204525&adgroup=1212761794897445&msclkid=510029f330dd1bc5c99a4dccbb44d6e5)

### Library

> [PrettyTable](https://pypi.org/project/prettytable/),
[os](https://docs.python.org/3/library/os.html),
[time](https://docs.python.org/3/library/time.html),
[getpass](https://docs.python.org/3/library/getpass.html),
[math](https://docs.python.org/3/library/math.html),
[sys](https://docs.python.org/3/library/sys.html),
[datetime](https://docs.python.org/3/library/datetime.html)

### Dict
- admin
- user biasa

### Linked List
- shop
- bakery

**Fungsi dalam class bakery:**

add product,
remove product,
edit product,
show product,
show history,
add transaction,
search,
sort,
ulang

### - Fungsi
- def cleardelay
- def menu urut
- def menu admin
- def login admin
- def menu pelanggan
- def login user
- def program

## 🍞Features🍞
- Pembeli
  - Registrasi Pelanggan
  - Login Pelanggan
  - Show Produk
  - Ambil Antrean
  - Belanja

- Admin
  - Login Admin
  - Show Produk
  - Tambah produk
  - Hapus produk
  - Tampilkan History

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

Pada awal program di run, program akan menampilkan menu awal yang berisi 4 pilihan yaitu Login Admin, Login Pelanggan, Registrasi Pelanggan, dan Exit.

![image](https://user-images.githubusercontent.com/127454468/232953396-cd507db7-d551-401a-9a55-c40fe4e44618.png)

### 🥨**User**🥨
#### Registrasi Pelanggan

Jika pelanggan belum memiliki akun, maka dapat memilih menu awal `opsi ke-3` untuk registrasi akun. Di menu registrasi, pelanggan akan diminta untuk memasukkan username dan password baru.
![Screenshot 2023-04-19 110721](https://user-images.githubusercontent.com/127454468/232958807-0ea18d5d-75dc-4620-90fe-58b076b5445a.png)

Setelah registrasi maka program akan kembali ke menu awal dan pelanggan dapat memasukkan username dan password yang telah didaftarkan di menu login pelanggan.
####  Login Pelanggan

Di menu ini, pelanggan harus memilih menu awal `opsi ke-2` dan memasukkan username dan password untuk bisa masuk ke dalam program.
![Screenshot 2023-04-19 110733](https://user-images.githubusercontent.com/127454468/232958790-28e83f6c-c744-4365-a8a6-dcda75ccbb77.png)

- Menu Pelanggan

Jika login berhasil, maka program akan memunculkan menu pelanggan yang terdiri dari 3 pilihan, yaitu Tampilkan Produk Yang Tersedia, Shopping, dan Exit.

![image](https://user-images.githubusercontent.com/127454468/232956243-f7be77c5-9b46-4c78-96f2-82f4b554ed55.png)

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

##### Program menampilkan produk yang dicari

![image](https://user-images.githubusercontent.com/127454468/232954091-b506f574-2c9b-48ab-b61b-fcf3ac384e54.png)

2. Beli Kue





![Screenshot 2023-04-19 110822](https://user-images.githubusercontent.com/127454468/232958223-03b7cc5d-07de-4c4c-8947-ae302b925954.png)


![Screenshot 2023-04-19 110521](https://user-images.githubusercontent.com/127454468/232958175-557c64a4-4d1b-4280-8872-a8e2132bf749.png)


![Screenshot 2023-04-19 110531](https://user-images.githubusercontent.com/127454468/232958142-a410ce66-45ed-4c23-99eb-e59550fdf836.png)


![Screenshot 2023-04-19 111254](https://user-images.githubusercontent.com/127454468/232958039-301b70fe-1558-457a-98c3-ffaae6865cd9.png)

![Screenshot 2023-04-19 110838](https://user-images.githubusercontent.com/127454468/232958687-ae40835b-d751-4c49-8eb8-7b92b79ce687.png)

3. Lihat Riwayat Pembelian

![Screenshot 2023-04-19 111031](https://user-images.githubusercontent.com/127454468/232990869-3c72f397-39be-41f5-90c0-1165b01313a6.png)

4. Keluar

Jika pelanggan telah selesai berbelanja, maka pelanggan dapat keluar program dengan memilih menu `Keluar`.



### 🥐**Admin**🥐
#### Login Admin

Setelah program di run, admin harus memilih menu awal `opsi ke-1` lalu memasukkan username dan password yang benar untuk bisa masuk ke dalam program.

![image](https://user-images.githubusercontent.com/127454468/232953524-aae17784-5c12-4b01-aa6d-e87de2b092fa.png)

- Menu Admin

Jika login berhasil, maka program akan memunculkan menu admin yang terdiri dari 6 pilihan, yaitu Tampilkan Produk Yang Tersedia, Tambahkan Produk Baru ke dalam List, Hapus Produk Dari List, Tampilkan History dan Exit.

![Screenshot 2023-04-19 104307](https://user-images.githubusercontent.com/127454468/232959845-a4a9029e-66f0-47fa-a78e-02f1cb897f6c.png)

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

##### Program menampilkan produk yang dicari

![image](https://user-images.githubusercontent.com/127454468/232954091-b506f574-2c9b-48ab-b61b-fcf3ac384e54.png)

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

3. Hapus Produk

Untuk menghapus produk yang telah ada maka admin dapat memilih `menu admin ke-3`, setelah memilih menu, admin akan diminta untuk menginput nama produk yang ingin dihapus.

![image](https://user-images.githubusercontent.com/127454468/232955155-2055f8af-6afc-4f0d-8535-18c589289eee.png)
```
Tampilan jika produk berhasil dihapus
```
![image](https://user-images.githubusercontent.com/127454468/232955200-9e33177c-149a-40dd-8136-70457def4bc7.png)

4. Edit Produk

![image](https://user-images.githubusercontent.com/127454468/232955474-b36a3b14-d7fb-454d-a118-9349e667a1fd.png)
![Screenshot 2023-04-19 105931](https://user-images.githubusercontent.com/127454468/232955843-f2c95d27-e960-40c9-a78f-9bb770128656.png)

![Screenshot 2023-04-19 105938](https://user-images.githubusercontent.com/127454468/232955815-64bebad8-4ff6-4ba6-a57c-01e6439a8e47.png)

![Screenshot 2023-04-19 144114](https://user-images.githubusercontent.com/127454468/232988414-80fdcce9-9884-43a8-a805-02368cdce008.png)

![Screenshot 2023-04-19 144143](https://user-images.githubusercontent.com/127454468/232988351-5dbf7fd4-6f30-4b00-8114-28078167a964.png)

![Screenshot 2023-04-19 144038](https://user-images.githubusercontent.com/127454468/232988373-57c9e7b5-3d13-4394-b4c1-39678581b7a8.png)

4. Tampilkan Riwayat

Jika ingin melihat history produk maka admin dapat memilih `menu admin ke-4`, maka program akan menampilkan history produk yang telah ditambahkan dan dihapus.

![Screenshot 2023-04-19 110009](https://user-images.githubusercontent.com/127454468/232955777-c75e3cce-1b41-44a5-8db3-cba393324c90.png)

5. Keluar

Jika admin telah selesai menggunakan program, maka admin dapat keluar program dengan memilih menu `Keluar`. Menu ini akan mengembalikan admin ke Menu Awal'.

#### Keluar
Jika ingin keluar dari program maka admin dan pelanggan dapat memilih `menu awal ke-4` untuk dapat keluar dari program.

![image](https://user-images.githubusercontent.com/127454468/232956070-7fbfbca9-5888-493f-8fa8-af487896efd7.png)
