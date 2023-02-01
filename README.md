# Project-self-service-cashier-PacmanAI
tugas membuat self-sevice-cashier mengguanakan pyhton
# Tujuan Project
Customer dapat membuat ID transaksinya (class Transaction)
Customer bisa melakukan input nama, jumlah dan harga barang
Customer bisa merubah nama, jumlah dan harga barang
Customer dapat membatalkan  item yang dipilih atau menghapus semua pesanan 
Customer dapat melakukan pengecekan total harga
Customer dapat menghitung total belanja dan ada fitur diskon dengan syarat tertentu
# Flowchart
![Doc2](https://user-images.githubusercontent.com/56928272/216104942-19efd018-81fd-44c6-b65c-f35838174cc8.png)
# Deskripsi
1. Modul kasir3.py mempunyai class transaksi 
```
class transaction:
    def __init__(self):
        self.order_items={}
```
dengan menggunakan class transaction akan membuat dictionary yang siap diisi dengan informasi belanja customer.


2. add_item() method
method ini digunakan untuk input nama barang,jumlah, dan harganya dan memunculkan daftar barang yang telah diinput menggunakan self.order_items.
```
    def add_item(self, nama, jumlah, harga):
        self.nama=str(nama).title()
        try:
            self.jumlah=int(jumlah)
            self.harga=int(harga)
            try:
                assert self.jumlah > 0
                assert self.harga > 0
                self.order_items[self.nama]=[self.jumlah, self.harga]
            except:
                print('error, jumlah dan harga harus lebih dari 0')
        except:
            print("error, jumlah dan harga harus berupa angka")
 ```
 3. show_order_table()
 method ini digunakan untuk menampilkan barang yang telah diinput di dalam tabulate.
 ```
    def show_order_table(self):
        from tabulate import tabulate
        order_table=[]
        table_header=['No','Nama','Jumlah','Harga','Total']
        order_table.append(table_header)
        
        i = 0
        
        for key, value in self.order_items.items():
            i += 1
            table_no = i
            nama= key
            jumlah = value[0]
            harga = value[1]
            amount = jumlah*harga
            item_data=[table_no, nama, jumlah, harga, amount]
            
            order_table.append(item_data)
            
        print(tabulate(order_table, headers ="firstrow"))
```
4. update_item_name(),update_item_qty(),update_item_price(), delete_item(), dan reset()

method ini digunakan  untuk mengedit informasi barang yang telah di input.

update_item_name() untuk mengganti nama barang
update_item_qty() untuk mengganti jumlah barang
update_item_price() untuk mengganti harga barang
delete_item() untuk menghapus barang yang dipilih
reset() untuk mereset seluruh transaksi
```
    def update_item_name(self, nama, nama_baru):
        self.nama= str(nama)
        self.nama_baru= str (nama_baru)
        try:
            self.order_items[self.nama_baru]= self.order_items[self.nama]
            del self.order_items[self.nama]
        except:
            print('nama tidak ditemukan')
    def update_item_qty(self, nama, jumlah_baru):
        self.nama=str(nama)
        
        try:
            self.jumlah_baru=int(jumlah_baru)
            try:
                assert self.jumlah > 0
                try:
                    self.order_items[self.nama][0] = self.jumlah_baru
                except:
                    print('error nama barang tidak ada')
            except:
                print('jumlah harus lebih dari 0')
        except:
            print('jumlah harus berupa angka')
    
    def update_item_price(self, nama, harga_baru):
        self.nama=str(nama)
        
        try:
            self.harga_baru= int (harga_baru)
            try:
                assert self.harga > 0
                try:
                    self.order_items[self.nama][1]=self.harga_baru
                except:
                    print('error nama barang tidak ada')
            except:
                print('harga tidak boleh 0')
        except:
            print('harga harus berupa angka')
    
    def delete_item(self, nama):
        self.nama= str(nama)
        try:
            del self.order_items[self.nama]
        except:
            print('nama tidak ada')
    def reset(self):
        transaction ={}
        self.order_items = transaction
        print('semua barang telah dihapus')
 ```   
 5.check_order()
 method ini digunakan apakah tipe data yang dimasukan sudah sesuai.
 
 ```
    def check_order(self):
        for key, value in self.order_items.items():
            nama=key
            jumlah=value[0]
            harga=value[1]
            
            if type(nama)== str and type(jumlah)==int and type(harga)==int:
                print(f' [v] {nama:<12}: data sudah sesuai')
            elif type(nama)!= str:
                print(f' [x] {nama:<12}: nama harus berupa teks')
            else:
                pass
            if type(jumlah)!=int:
                print(f'[x] {nama:<12}: jumlah harus berupa angka')
            else:
                pass
            if type(harga)!= int:
                print(f'[x] {nama:<12}: harga harus berupa angka')
            else:
                pass
```     

6. total_harga() dan diskon()

method ini digunakan untuk perhitungan total harga yang harus dibayar customer dan apakah dia mendapat diskon jika iya maka method diskon()akan berjalan.

```
    def total_harga(self):
        self.total_harga = 0
        for value in self.order_items.values():
            jumlah = value[0]
            harga = value[1]
            self.total_harga += (jumlah*harga)
        diskon, discount = self.diskon(self.total_harga)
        self.harga_akhir = self.total_harga * (1-discount)
        
        if diskon == True:
            print(f'Total belanja Rp{self.total_harga}.')
            print(f'diskon {discount *100}%')
            print(f' jumlah yang perlu dibayar adalah Rp{self.harga_akhir}')
        else:
            print(f'Total belanja Rp{self.total_harga}.')
    def diskon(self, total_harga):
        self.total_harga= total_harga
        if self.total_harga < 200000:
            diskon = True
            discount = 0.0
        else:
            diskon= True
            if self.total_harga > 500000:
                discount = 0.1
            elif self.total_harga > 300000:
                discount = 0.08
            elif self.total_harga > 200000:
                discount = 0.05
        return diskon, discount
```        
