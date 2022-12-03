#!/usr/bin/env python
# coding: utf-8

# # Membuat Class Transaction beserta Methods

# In[13]:


# import library yg dibutuhkan
import pandas as pd


# In[14]:


class Transaction:
    def __init__(self):
        """
        fungsi menginisialisasi dictionary
        """
        
        self.data_item = dict()

        
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
    
    
    def reset_transaction(self):
        """
        fungsi untuk menghapus semua item
        """
        
        self.data_item.clear()
        print('Semua item berhasil di delete!')

        
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
        
    
    def show_order(self):
        """
        fungsi untuk menampilkan rekap data item belanja dalam bentuk tabel
        """
        
        print('Berikut adalah pesanan Anda :')
        data = pd.DataFrame(self.data_item).T
        data.columns = ['Jumlah Item', 'Harga Item', 'Total Harga']
        print(data.to_markdown())
        
        
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
   


# # Test Case

# ## Test 1:

# Customer ingin menambahkan dua item baru menggunakan method add_item(). Item yang ditambahkan adalah sebagai berikut : <br>
# <ul>
#     <li>Nama Item: Ayam Goreng, Qty: 2, Harga: 20000</li>
#     <li>Nama Item: Pasta Gigi, Qty: 3, Harga: 15000</li>
# </ul>

# In[15]:


print('TEST 1 :')
belanja = Transaction()
belanja.add_item('Ayam Goreng',2,20000)
belanja.add_item('Pasta Gigi',3,15000)
belanja.check_order()


# ## Test 2:

# Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method delete_item() untuk menghapus item. Item yang ingin dihapus adalah <b>Pasta Gigi</b>

# In[16]:


print('\n\nTEST 2 :')
belanja.delete_item('Pasta Gigi')
belanja.check_order()


# ## Test 3:

# Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan!<br>Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan.

# In[17]:


print('\n\nTEST 3 :')
belanja.reset_transaction()
belanja.check_order()


# ## Test 4:

# Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

# In[18]:


print('\n\nTEST 4 :')
belanja.add_item('Ayam Goreng',2,20000)
belanja.add_item('Pasta Gigi',3,15000)
belanja.add_item('Mainan Mobil',1,200000)
belanja.add_item('Mi Instan',5,3000)
belanja.total_price()


# In[ ]:




