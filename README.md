# Python-SuperCashier

# Latar Belakang Problems
Andi adalah seorang pemilik supertmarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan ekspansi bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli,dan harga yang dibeli dan fitur yang lain
Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan programmer untuk membuatkan fitur-fitur agar system kasir slef-service di supermarket itu bisa berjalan dengan lancar

# Objective dan Requirement Project
Membuat sebuah program kasir sederhana yang dapat melakukan aktivitas
- Memasukkan item yang dibeli, termasuk jumlah item dan harga satuan item
- Mengupdate nama item, jumlah item, atau harga item
- Menghapus item tertentu maupun hapus keseluruhan
- Melakukan pengecekan data yang diinput
- Menampilkan daftar item yang dibeli
- Menampilkan jumlah yang harus dibayar

Berikut flowchart cara penggunaan program
![image](https://user-images.githubusercontent.com/115354118/205471517-0e080673-fc0c-4dc6-b182-269f6f0dd922.png)

Beberapa method yang dibuat untuk requirement tersebut adalah
- `add_item(nama_item,jumlah_item,harga_item)` memasukkan item yang dibeli, termasuk jumlah item dan harga satuan item
- `update_item_name(nama_item, update_nama_item)` mengupdate nama item
- `update_item_qty(nama_item, update_jumlah_item)` mengupdate jumlah item
- `update_item_price(nama_item, update_harga_item)` mengupdate harga item
- `delete_item(nama_item)` menghapus item tertentu maupun hapus keseluruhan
- `reset_transaction()` menghapus seluruh item
- `check_order()` melakukan pengecekan data yang diinput
- `show_order()` menampilkan daftar item yang dibeli
- `total_price()` menampilkan jumlah yang harus dibayar


# Penjelasan Code
Code ditulis menggunakan python menggunakan jupyter notebook. Untuk implementasi solusi project ini digunakan composite data structure `dictionary`. Class yang didefinisikan bernama `Transaction`, yang didalamnya didefinisikan beberapa method sesuai requirement project ini. Berikut beberapa potongan code untuk beberapa method yang digunakan di project ini.

## Method `add_item`
Ketika customer butuh menambah item belanja ke dalam keranjangnya maka diperlukan fitur penambahan item di dalam program. Method ini digunakan untuk fitur tersebut.
```python
def add_item(self, nama_item, jumlah_item, harga_per_item):
        """
        fungsi menambahkan data item

        parameters
        nama_item      : str   nama item yang akan dibeli
        jumlah_item    : float   banyak item yang akan dibeli
        harga_per_item : float   harga satuan item yang akan dibeli
        """
        
        try:
            total_harga = float(jumlah_item)*float(harga_per_item)
        except ValueError:
            print('Terdapat exception : parameter kedua dan ketiga harus berupa angka')
            
        self.data_item.update({nama_item: [jumlah_item, harga_per_item, total_harga]})
```
Terdapat `try` dan `except` untuk menangkap kemungkinan adanya kesalahan tipe data yang dimasukkan user. Disini tidak dilakukan pengecekan tipe data menggunakan fungsi `type` untuk penulisan code yang lebih efisien.

## Method `update_item_name`
Ketika customer butuh mengubah nama item belanja di dalam keranjangnya maka diperlukan fitur edit nama item di dalam program. Method ini digunakan untuk fitur tersebut.
```python
def update_item_name(self, nama_item, update_nama_item):
        """
        fungsi untuk memperbarui nama item

        parameters
        nama_item         : str   nama item yang ingin diperbarui
        update_nama_item  : str   nama baru untuk item
        """
        
        try:
            temp = self.data_item[nama_item]
            self.data_item.pop(nama_item)
            self.data_item.update({update_nama_item: temp})
        except KeyError:
            print(f'Terdapat exception : nama item {nama_item} tidak ditemukan')
```
Terdapat `try` dan `except` untuk menangkap kemungkinan adanya kesalahan penulisan nama item yang dimasukkan user, sehingga nama item tidak ditemukan. 

## Method `update_item_qty`
Ketika customer butuh mengubah jumlah salah satu item belanja di dalam keranjangnya maka diperlukan fitur edit jumlah item di dalam program. Method ini digunakan untuk fitur tersebut.
```python
def update_item_qty(self, nama_item, update_jumlah_item):
        """
        fungsi untuk memperbarui jumlah item

        parameters
        nama_item         : str   nama item yang ingin diperbarui
        update_jumlah_item: float   jumlah baru untuk item
        """
        
        try:
            self.data_item[nama_item][0] = update_jumlah_item
            self.data_item[nama_item][2] = (float)(self.data_item[nama_item][0])*(float)(self.data_item[nama_item][1])
        except KeyError:
            print(f'Terdapat exception : nama item {nama_item} tidak ditemukan')
        except ValueError:
            print(f'Terdapat exception : jumlah item harus berupa angka')
```
Terdapat `try` dan `except` untuk menangkap kemungkinan adanya kesalahan penulisan nama item yang dimasukkan user, sehingga nama item tidak ditemukan. Serta terdapat juga `except` untuk menangkap kemungkinan adanya kesalahan tipe data yang dimasukkan user.

## Method `update_item_price`
Ketika customer butuh mengubah harga satuan salah satu item belanja di dalam keranjangnya maka diperlukan fitur edit harga satuan item di dalam program. Method ini digunakan untuk fitur tersebut.
```python
def update_item_price(self, nama_item, update_harga_item):
        """
        fungsi untuk memperbarui harga item

        parameters
        nama_item         : str   nama item yang ingin diperbarui
        update_harga_item : float   harga baru untuk item
        """
        
        try:
            self.data_item[nama_item][1] = update_harga_item
            self.data_item[nama_item][2] = self.data_item[nama_item][0]*self.data_item[nama_item][1]
        except KeyError:
            print(f'Terdapat exception : nama item {nama_item} tidak ditemukan')
        except ValueError:
            print(f'Terdapat exception : harga item harus berupa angka')
```
Terdapat `try` dan `except` untuk menangkap kemungkinan adanya kesalahan penulisan nama item yang dimasukkan user, sehingga nama item tidak ditemukan. Serta terdapat juga `except` untuk menangkap kemungkinan adanya kesalahan tipe data yang dimasukkan user.

## Method `delete_item`
Ketika customer butuh menghapus salah satu item belanja di dalam keranjangnya maka diperlukan fitur penghapusan sebuah item di dalam program. Method ini digunakan untuk fitur tersebut.
```python
def delete_item(self, nama_item):
        """
        fungsi untuk menghapus item

        parameters
        nama_item         : str   nama item yang ingin dihapus
        """
        
        try:
            self.data_item.pop(nama_item)
        except KeyError:
            print(f'Terdapat exception : nama item {nama_item} tidak ditemukan')
```
Terdapat `try` dan `except` untuk menangkap kemungkinan adanya kesalahan penulisan nama item yang dimasukkan user, sehingga nama item tidak ditemukan. 

## Method `reset_transaction`
Ketika customer butuh menghapus semua item belanja di dalam keranjangnya maka diperlukan fitur penghapusan seluruh item di dalam program. Method ini digunakan untuk fitur tersebut.
```python
def reset_transaction(self):
        """
        fungsi untuk menghapus semua item
        """
        
        self.data_item.clear()
        print('Semua item berhasil di delete!')
```

## Method `check_order`
Ketika customer butuh memeriksa semua item belanja yang telah dimasukkan ke dalam keranjangnya maka diperlukan fitur cek order di dalam program. Method ini digunakan untuk fitur tersebut. Method ini akan mengecek kemungkinan input jumlah item atau harga item yang negatif serta akan menampilkan hasil input seluruh item dengan memanggil method `show_order`. Selain itu method ini juga akan memberikan nilai pengembalian berupa jumlah kesalahan. Nilai pengembalian ini nantinya dapat digunakan oleh method `total_price` sebelum menghitung total yang harus dibayar customer.

```python
def check_order(self):
        """
        fungsi untuk melakukan pengecekan input data dan mengeluarkan output tabel transaksi
        """
        
        # variabel untuk menampung jumlah kesalahan data
        jml_kesalahan = 0
        
        # memeriksa nilai negatif di setiap data 
        for x in self.data_item:
            
            # memeriksa nilai negatif di parameter jumlah item
            if self.data_item[x][0]<0:
                jml_kesalahan = jml_kesalahan+1
                print(f'Terjadi kesalahan input data yaitu jumlah item {x} negatif')
            
            # memeriksa nilai negatif di parameter harga item
            if self.data_item[x][1]<0:
                jml_kesalahan = jml_kesalahan+1
                print(f'Terjadi kesalahan input data yaitu harga item {x} negatif')
        
        # menampilkan pesan sesuai jumlah kesalahan
        if len(self.data_item)==0:
            print('Tidak ada pesanan')
        elif jml_kesalahan==0:
            print('Pemesanan sudah benar')
            self.show_order()
        else:
            print('Mohon perbaiki data Anda')
            self.show_order()
        
        # jumlah kesalahan menjadi nilai pengembalian fungsi
        return jml_kesalahan
```

## Method `show_order`
Method ini digunakan untuk menampilkan seluruh item belanja dalam bentuk tabel
```python
def show_order(self):
        """
        fungsi untuk menampilkan rekap data item belanja dalam bentuk tabel
        """
        
        print('Berikut adalah pesanan Anda :')
        data = pd.DataFrame(self.data_item).T
        data.columns = ['Jumlah Item', 'Harga Item', 'Total Harga']
        print(data.to_markdown())
```

## Method `total_price`
Ketika customer butuh menghitung total belanja dan total yang harus dibayar maka diperlukan fitur untuk melakukan perhitungannya di dalam program. Terdapat ketentuan untuk setiap customer bahwa 
- jika total belanja melebihi Rp. 200.000, maka akan mendapatkan diskon 5%
- jika total belanja melebihi Rp. 300.000, maka akan mendapatkan diskon 8%
- jika total belanja melebihi Rp. 500.000, maka akan mendapatkan diskon 10%

```python
def total_price(self):
        """
        fungsi untuk menghitung total belanja dan total yang harus dibayar
        """
        
        # menghitung jumlah kesalahan data
        jml_kesalahan = self.check_order()
                
        if jml_kesalahan>0:
            print('Perhitungan total belanja ditangguhkan karena masih terdapat kesalahan input data')
            
        else:
            total_belanja = 0
            total_bayar = 0
            
            # menampung total harga semua item ke dalam variabel total_belanja
            for x in self.data_item:
                total_belanja = total_belanja+self.data_item[x][2]
            
            print(f'Total belanja Anda adalah sebesar Rp. {total_belanja}\n')
            
            # menghitung total bayar sesuai dengan total belanja dan diskon
            if total_belanja>500000:
                total_bayar = total_belanja-(0.1*total_belanja)
                print('Karena total belanja Anda diatas Rp. 500000, maka Anda mendapatkan diskon 10%')
            elif total_belanja>300000:
                total_bayar = total_belanja-(0.08*total_belanja)
                print('Karena total belanja Anda diatas Rp. 300000, maka Anda mendapatkan diskon 8%')
            elif total_belanja>200000:
                total_bayar = total_belanja-(0.05*total_belanja)
                print('Karena total belanja Anda diatas Rp. 200000, maka Anda mendapatkan diskon 5%')
            else:
                total_bayar = total_belanja
                
            print(f'Silakan lakukan pembayaran sebesar Rp. {total_bayar}.\nTerima kasih telah berbelanja di supermarket kami.')
```
Method ini akan memanggil method `check_order` untuk memeriksa apakah sudah tidak ada angka negatif pada jumlah item dan harga satuan. Jika sudah tidak ada maka proses perhitungan total belanja dan total yang harus dibayar akan dilakukan. Karena method ini memanggil method `check_order` (sedangkan method `check_order` akan memanggil method `show_order`), maka method ini juga akan menampilkan seluruh item belanja dalam bentuk tabel (jika ada item yang ditambahkan).

# Test Case
Untuk memastikan code yang ditulis telah benar dan sesuai, maka perlu dilakukan pengujian dengan beberapa skenario. Untuk project kali ini terdapat 4 skenario pengujian yaitu Test 1, Test 2, Test 3, dan Test 4.

## Test 1
Customer ingin menambahkan dua item baru menggunakan method `add_item()`. Item yang ditambahkan adalah sebagai berikut :
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

Berikut adalah code untuk test tersebut
```python
print('TEST 1 :')
belanja = Transaction()
belanja.add_item('Ayam Goreng',2,20000)
belanja.add_item('Pasta Gigi',3,15000)
belanja.check_order()
```
Hasil yang didapat adalah sebagai berikut
```
TEST 1 :
Pemesanan sudah benar
Berikut adalah pesanan Anda :
|             |   Jumlah Item |   Harga Item |   Total Harga |
|:------------|--------------:|-------------:|--------------:|
| Ayam Goreng |             2 |        20000 |         40000 |
| Pasta Gigi  |             3 |        15000 |         45000 |
```

## Test 2
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method `delete_item()` untuk menghapus item. Item yang ingin dihapus adalah **Pasta Gigi**

Berikut adalah code untuk test tersebut
```python
print('\n\nTEST 2 :')
belanja.delete_item('Pasta Gigi')
belanja.check_order()
```
Hasil yang didapat adalah sebagai berikut
```
TEST 2 :
Pemesanan sudah benar
Berikut adalah pesanan Anda :
|             |   Jumlah Item |   Harga Item |   Total Harga |
|:------------|--------------:|-------------:|--------------:|
| Ayam Goreng |             2 |        20000 |         40000 |
```

## Test 3
Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan!
Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.

Berikut adalah code untuk test tersebut
```python
print('\n\nTEST 3 :')
belanja.reset_transaction()
belanja.check_order()
```
Hasil yang didapat adalah sebagai berikut
```
TEST 3 :
Semua item berhasil di delete!
Tidak ada pesanan
```

## Test 4
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method `total_price()`. Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

Berikut adalah code untuk test tersebut
```python
print('TEST 4 :')
belanja.add_item('Ayam Goreng',2,20000)
belanja.add_item('Pasta Gigi',3,15000)
belanja.add_item('Mainan Mobil',1,200000)
belanja.add_item('Mi Instan',5,3000)
belanja.total_price()
```
Hasil yang didapat adalah sebagai berikut
```
TEST 4 :
Pemesanan sudah benar
Berikut adalah pesanan Anda :
|              |   Jumlah Item |   Harga Item |   Total Harga |
|:-------------|--------------:|-------------:|--------------:|
| Ayam Goreng  |             2 |        20000 |         40000 |
| Pasta Gigi   |             3 |        15000 |         45000 |
| Mainan Mobil |             1 |       200000 |        200000 |
| Mi Instan    |             5 |         3000 |         15000 |
Total belanja Anda adalah sebesar Rp. 300000.0

Karena total belanja Anda diatas Rp. 200000, maka Anda mendapatkan diskon 5%
Silakan lakukan pembayaran sebesar Rp. 285000.0.
Terima kasih telah berbelanja di supermarket kami.
```
