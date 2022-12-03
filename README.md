# python-supercashier

# Latar Belakang Problems
Andi adalah seorang pemilik supertmarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan ekspansi bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli,dan harga yang dibeli dan fitur yang lain
Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan programmer untuk membuatkan fitur-fitur agar system kasir slef-service di supermarket itu bisa berjalan dengan lancar

# Objective dan Requirement Project
Membuat sebuah program kasir sederhana yang dapat melakukan aktivitas
<ul>
  <li>Memasukkan item yang dibeli, termasuk jumlah item dan harga satuan item</li>
  <li>Mengupdate nama item, jumlah item, atau harga item</li>
  <li>Menghapus item tertentu maupun hapus keseluruhan</li>
  <li>Melakukan pengecekan data yang diinput</li>
  <li>Menampilkan daftar item yang dibeli</li>
  <li>Menampilkan jumlah yang harus dibayar</li>
</ul>

Berikut kurang lebih flowchart aktivitas program
![image](https://user-images.githubusercontent.com/115354118/205451812-e928e11e-0299-4208-ad37-274f4c87cdca.png)

Beberapa method yang dibuat untuk requirement tersebut adalah
<ul>
  <li>add_item(nama_item,jumlah_item,harga_item) --> Memasukkan item yang dibeli, termasuk jumlah item dan harga satuan item</li>
  <li>update_item_name(nama_item, update_nama_item) --> Mengupdate nama item</li>
  <li>update_item_qty(nama_item, update_jumlah_item) --> Mengupdate jumlah item</li>
  <li>update_item_price(nama_item, update_harga_item) --> Mengupdate harga item</li>
  <li>delete_item(nama_item) --> Menghapus item tertentu maupun hapus keseluruhan</li>
  <li>reset_transaction() --> Menghapus seluruh item</li>
  <li>check_order() --> Melakukan pengecekan data yang diinput</li>
  <li>show_order() --> Menampilkan daftar item yang dibeli</li>
  <li>total_price() --> Menampilkan jumlah yang harus dibayar</li>
</ul>

# Potongan Code
## Method add_item
<img width="488" alt="image" src="https://user-images.githubusercontent.com/115354118/205452017-2a469fdf-a990-4af6-8dbe-db32ed1f148a.png">

## Method update_item_name
<img width="449" alt="image" src="https://user-images.githubusercontent.com/115354118/205452118-370034c6-df11-409a-bc98-52465887014c.png">

## Method update_item_qty
<img width="666" alt="image" src="https://user-images.githubusercontent.com/115354118/205452312-dd5694b6-4421-482b-87b9-921eed3a1019.png">

## Method update_item_price
<img width="567" alt="image" src="https://user-images.githubusercontent.com/115354118/205452349-11c8e551-6589-46d8-8d5e-7bf62324391d.png">

## Method delete_item
<img width="448" alt="image" src="https://user-images.githubusercontent.com/115354118/205452407-95290afc-b90d-4032-8390-61a7354ead8c.png">

## Method reset_transaction
<img width="269" alt="image" src="https://user-images.githubusercontent.com/115354118/205452452-693d5da5-ef88-47e0-991a-ac3f2c05161e.png">

## Method check_order
<img width="517" alt="image" src="https://user-images.githubusercontent.com/115354118/205452528-624c84ef-cbb8-4d73-b110-fa398428779c.png">
<img width="472" alt="image" src="https://user-images.githubusercontent.com/115354118/205452564-898656c9-5cf0-4d29-a9a1-2ee79fc0e544.png">

## Method show_order
<img width="425" alt="image" src="https://user-images.githubusercontent.com/115354118/205452584-3142e6d3-7bc0-4f25-bf75-806e9a55b54f.png">

## Method total_price
<img width="614" alt="image" src="https://user-images.githubusercontent.com/115354118/205452628-7e74a250-4870-46c6-b4e6-0c3ee5303023.png">
<img width="705" alt="image" src="https://user-images.githubusercontent.com/115354118/205452660-1b8c32fb-acdb-4b0c-99b9-48bc57ee5725.png">

# Test Case
<img width="535" alt="image" src="https://user-images.githubusercontent.com/115354118/205452817-6d1ef46e-f4c2-4600-88b7-6a5f9c09eaa9.png">
<img width="532" alt="image" src="https://user-images.githubusercontent.com/115354118/205452844-87a6da41-e855-45e4-a3c6-7cfe20b87ff3.png">
<img width="529" alt="image" src="https://user-images.githubusercontent.com/115354118/205452864-dee30694-0d6e-489d-a2ba-2429436362fa.png">
<img width="658" alt="image" src="https://user-images.githubusercontent.com/115354118/205452935-a3906d1a-331c-463d-9c05-c281c196020b.png">

