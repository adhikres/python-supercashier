#!/usr/bin/env python
# coding: utf-8

# In[10]:


# import library yg dibutuhkan
import pandas as pd


# In[11]:


# membuat class Transaction beserta beberapa method nya
class Transaction:
    def __init__():
        """
        fungsi menginisialisasi dictionary
        """
        
        data_item = dict()

        
    def add_item(nama_item, jumlah_item, harga_per_item):
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
            
        data_item.update({nama_item: [jumlah_item, harga_per_item, total_harga]})
        
        
    def update_item_name(nama_item, update_nama_item):
        """
        fungsi untuk memperbarui nama item

        parameters
        nama_item         : str   nama item yang ingin diperbarui
        update_nama_item  : str   nama baru untuk item
        """
        
        try:
            temp = data_item[nama_item]
            data_item.pop(nama_item)
            data_item.update({update_nama_item: temp})
        except KeyError:
            print(f'Terdapat exception : nama item {nama_item} tidak ditemukan')

        
    def update_item_qty(nama_item, update_jumlah_item):
        """
        fungsi untuk memperbarui jumlah item

        parameters
        nama_item         : str   nama item yang ingin diperbarui
        update_jumlah_item: float   jumlah baru untuk item
        """
        
        try:
            data_item[nama_item][0] = update_jumlah_item
            data_item[nama_item][2] = (float)(data_item[nama_item][0])*(float)(data_item[nama_item][1])
        except KeyError:
            print(f'Terdapat exception : nama item {nama_item} tidak ditemukan')
        except ValueError:
            print(f'Terdapat exception : jumlah item harus berupa angka')
    
    def update_item_price(nama_item, update_harga_item):
        """
        fungsi untuk memperbarui harga item

        parameters
        nama_item         : str   nama item yang ingin diperbarui
        update_harga_item : float   harga baru untuk item
        """
        
        try:
            data_item[nama_item][1] = update_harga_item
            data_item[nama_item][2] = data_item[nama_item][0]*data_item[nama_item][1]
        except KeyError:
            print(f'Terdapat exception : nama item {nama_item} tidak ditemukan')
        except ValueError:
            print(f'Terdapat exception : harga item harus berupa angka')
        
        
    def delete_item(nama_item):
        """
        fungsi untuk menghapus item

        parameters
        nama_item         : str   nama item yang ingin dihapus
        """
        
        try:
            data_item.pop(nama_item)
        except KeyError:
            print(f'Terdapat exception : nama item {nama_item} tidak ditemukan')
    
    
    def reset_transaction():
        """
        fungsi untuk menghapus semua item
        """
        
        data_item.clear()
        print('Semua item berhasil di delete!')

        
    def check_order():
        """
        fungsi untuk melakukan pengecekan input data dan mengeluarkan output tabel transaksi
        """
        
        # variabel untuk menampung jumlah kesalahan data
        jml_kesalahan = 0
        
        # memeriksa nilai negatif di setiap data 
        for x in data_item:
            
            # memeriksa nilai negatif di parameter jumlah item
            if data_item[x][0]<0:
                jml_kesalahan = jml_kesalahan+1
                print(f'Terjadi kesalahan input data yaitu jumlah item {x} negatif')
            
            # memeriksa nilai negatif di parameter harga item
            if data_item[x][1]<0:
                jml_kesalahan = jml_kesalahan+1
                print(f'Terjadi kesalahan input data yaitu harga item {x} negatif')
        
        # menampilkan pesan sesuai jumlah kesalahan
        if len(data_item)==0:
            print('Tidak ada pesanan')
        elif jml_kesalahan==0:
            print('Pemesanan sudah benar')
            show_order()
        else:
            print('Mohon perbaiki data Anda')
            show_order()
        
        # jumlah kesalahan menjadi nilai pengembalian fungsi
        return jml_kesalahan
        
    
    def show_order():
        """
        fungsi untuk menampilkan rekap data item belanja dalam bentuk tabel
        """
        
        print('Berikut adalah pesanan Anda :')
        data = pd.DataFrame(data_item).T
        data.columns = ['Jumlah Item', 'Harga Item', 'Total Harga']
        print(data.to_markdown())
        
        
    def total_price():
        """
        fungsi untuk menghitung total belanja dan total yang harus dibayar
        """
        
        # menghitung jumlah kesalahan data
        jml_kesalahan = check_order()
                
        if jml_kesalahan>0:
            print('Perhitungan total belanja ditangguhkan karena masih terdapat kesalahan input data')
            
        else:
            total_belanja = 0
            total_bayar = 0
            
            # menampung total harga semua item ke dalam variabel total_belanja
            for x in data_item:
                total_belanja = total_belanja+data_item[x][2]
            
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
   

