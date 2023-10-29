# Kelompok 14
# Simulasi Portal Parkir Otomatis

# Header
print('\n' + 44*'=')
print(6*' '+'SIMULASI PORTAL PARKIR OTOMATIS ')
print('\n'+ 14*' '+'KELOMPOK 14 ')
print(44*'='+'\n')

# PERNYATAAN FUNGSI
def menu(loop):     # Menu Program
    # KAMUS
    # pilihan : str
    # loop    : bool
    if loop:
        print()
        print(3*'='+' Menu Simulasi '+ 27*'=')
        print('Masuk  - Simulasi Kendaraan Masuk')
        print('Keluar - Simulasi Kendaraan Keluar')
        print('Daftar - Registrasi kartu baru')
        print('Cek    - Cek data ID, kode aktif, dan waktu masuk')
        print('End    - Akhiri Simulasi')
        pilihan = input('\n>> ')
        print()
        loop = False
    return  pilihan
def kapasitas(N, active):   # Kapasitas Parkir
    # KAMUS
      # N            : int
      # active       : list of str
      # parkir_penuh : bool
    
    for i in range(N):
        if '' not in active:
            parkir_penuh = True
        else:
            parkir_penuh = False
    return parkir_penuh
def operasi_portal(buka):   # Mengendalikan buka-tutup palang
    # KAMUS
      # kendaraan_ada : bool
      # ada           : str
      # buka          : bool
    kendaraan_ada = True
    if buka:
        print('\n'+11*'<'+11*'>'+'\nPortal terbuka')
        while kendaraan_ada:
            ada = input()
            if ada == 'pergi':
                kendaraan_ada = False
                buka = False
                print('Portal tertutup\n'+11*'<'+11*'>'+'\n')
            else:
                kendaraan_ada = True
    return kendaraan_ada, buka

# KODE UTAMA
# KAMUS
  # UMUM
   # N           : int
   # ID          : list of str
   # active      : list of str
   # waktu       : list of str
   # jalan       : bool          -> Master simulasi 
   # ke_menu     : bool          
   # simulasi    : str           -> Handle percabangan simulasi
   # counter     : int

  # DAFTAR
   # new_id      : str           -> Menyimpan ID baru sementara

  # MASUK & KELUAR
   # buka        : bool          -> Penanda terbukanya portal
   # found       : bool          -> Keluar - mencari uid
   # ulang_masuk : bool          -> Mengulang simulasi masuk
   # waktu_masuk : str
   # kode_parkir : str
   # ulang_keluar: bool
  
  
  


    

N = int(input('Masukkan jumlah lahan parkir: '))
ID = ['' for i in range(N*3)]     # Menyimpan data UID yang terdaftar
active = ['' for i in range(N)] # UID yang sedang aktif (parkir)
waktu = ['' for i in range(N)]  # Menyimpan waktu masuk
jalan = True
ke_menu = True    # Kembali ke menu jika True

while jalan:
    simulasi = menu(ke_menu) 
    parkir_penuh = kapasitas(N, active)

    # Mendaftarkan Kartu Baru
    if simulasi == 'Daftar' or simulasi == 'daftar':
        # Antarmuka
        print(3*'='+' Pendaftaran Kartu '+ 23*'=')
        print('Hapus - Hapus kartu yang terdaftar')
        
        counter = 0
        if '' not in ID:
            print('Error: Jumlah akun maksimum telah tercapai')
        else:
            new_id = input('\nMasukkan ID Baru: ')
        if new_id == 'hapus':
            new_id = input('Masukkan ID yang akan dihapus: ')
            hapus = True
        else:
            hapus = False
        if new_id in ID:
            print('Error: ID sudah terdaftar')
        for i in range(N*3):
            if ID[i] == '' and counter < 1 and new_id not in ID and not hapus:
                ID[i] = new_id
                counter += 1
                print('\n'+26*'-' + '\n' + f'ID : {ID[i]}\nID Berhasil Terdaftar' + '\n' + 26*'-')
            elif hapus and ID[i] == new_id:
                ID[i] = ''
                counter += 1
                print('\n'+26*'-' + '\n' + f'ID : {new_id}\nID Berhasil Terhapus' + '\n' + 26*'-')
        # Reset Var
        counter = 0
  
    # Kendaraan Masuk
    elif simulasi == 'Masuk' or simulasi == 'masuk':
        print(3*'='+' Simulasi Kendaraan Masuk '+ 16*'=')
        # Reset Var
        Found = False   
        ulang_masuk = True

        # Pesan jika parkir terisi penuh
        if parkir_penuh:
            print(22*'X' + '\n' + 'Parkir Terisi Penuh' + '\n' + 22*'X')
        else:
            # Header
            print()
            print(45*'-' + '\n' + '|' + 14*' ' + f'Selamat Datang!' + 14*' ' + '|' + '\n' + 45*'-')
            print()
        # Scan ID
        while ulang_masuk and not parkir_penuh:
            kode_parkir = input('Masukkan Kode Kartu & Waktu Masuk\nUID: ')
            if kode_parkir in active:
                found = False
                print('Error : Kartu sedang aktif\n')
            if kode_parkir in ID:     # Mengecek UID terdaftar atau tidak
                found = True
                ulang_masuk = False
            elif kode_parkir not in ID:
                found = False
            
            if kode_parkir == 'menu':   # Kembali ke menu
                ulang_masuk = False
            # Kode tidak terdaftar
            if not found and ulang_masuk:
                print('\nError : Kartu tidak terdaftar\n')

        # Melanjutkan proses jika ID terdaftar
        if found and not parkir_penuh:
            waktu_masuk = input('Waktu Masuk: ')
            for i in range(N):
                if active[i] == '' and counter < 1:
                    active[i] = kode_parkir
                    waktu[i] = waktu_masuk
                    counter += 1
            print(22*'-' + '\n' + f'UID         : {kode_parkir}\nWaktu masuk : {waktu_masuk}' + '\n' + 22*'-')
            buka = True
            Found = False 
            operasi_portal(buka)
        # Reset Var
        counter = 0  
            
    # Kendaraan Keluar
    elif simulasi == 'Keluar' or simulasi == 'keluar':
        # Header
        print()
        print(3*'='+' Simulasi Kendaraan Keluar '+ 15*'=')
        print()

        found = False   # Reset Variabel
        ulang_keluar = True
        while ulang_keluar:
            kode_parkir = input('Masukkan kode kartu:\nUID: ')
            if kode_parkir == 'menu':    # Mengakhiri sub-simulasi
                ulang_keluar = False
            elif kode_parkir not in active:
                print('\nError : Kode sedang tidak aktif\n')
                buka = False
            for i in range(N):
                if kode_parkir in active:
                    active[i] = ''
                    waktu[i] = ''
                    ulang_keluar = False
                    found = True

        if not ulang_keluar and found:
            buka = True
            operasi_portal(buka)
            print(45*'-' + '\n' + '|' + 14*' ' + f'Selamat Jalan!' + 14*' ' + '|' + '\n' + 45*'-')
        
    # Mengecek Status Array
    elif simulasi == 'cek' or simulasi == 'cek':
        print(f'Data ID : {ID}\nAktif   : {active}\nWaktu   : {waktu}')
        ke_menu = True
    
    # Menghentikan Simulasi
    elif simulasi == 'end' or simulasi == 'terminate' or simulasi == 'End' or simulasi == 'Terminate' :
        jalan = False

    # Cek status variabel
    elif simulasi == 'var' or kode_parkir == 'var' or waktu_masuk == 'var':
        print(f'kode_parkir = {kode_parkir}\nbuka = {buka}\nfound = {found}\nulang_masuk = {ulang_masuk}\nke_menu = {ke_menu}')
    
    
    else:   # simulasi terinput selain yang ditentukan
        print('Berikan input yang benar')
        ke_menu = True
print('Simulasi dihentikan')

