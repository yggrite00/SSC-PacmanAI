class transaction:
    def __init__(self):
        self.order_items={}
        
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
            
                
