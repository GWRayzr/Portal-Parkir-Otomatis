# KAMUS 
  # found       : bool  -> Handle pencarian elemen
  # counter     : int   -> Penghitung
  # buka        : bool  -> Handle pembukaan portal

def menu(loop):                                     # Menu Program
# KAMUS
  # pilihan     : str   -> Input untuk mengakses percabangan simulasi
  # loop        : bool  -> Perulangan Menu

    # Tampilan Menu
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
def kapasitas(N, aktif):                           # Kapasitas Parkir
# KAMUS
  # parkir_penuh : bool
    
    for i in range(N):
        if '' not in aktif:
            parkir_penuh = True
        else:
            parkir_penuh = False
    return parkir_penuh
def operasi_portal(buka):                           # Mengendalikan buka-tutup palang
# KAMUS
  # kendaraan_ada : bool
  # ada           : str

    kendaraan_ada = True
    if buka:
        print('\n'+11*'<'+11*'>'+'\nPortal terbuka')
        while kendaraan_ada:
            ada = input('>> ')
            if ada == 'pergi':
                kendaraan_ada = False
                buka = False
                print('Portal tertutup\n'+11*'<'+11*'>'+'\n')
            else:
                kendaraan_ada = True
    return kendaraan_ada, buka
def daftar (ID):                                    # Pendaftaran ID
# KAMUS
  # new_id      : bool  -> Menyimpan ID baru untuk sementara
  # hapus       : bool  -> Penanda jika ingin menghapus kartu

# Antarmuka
    print(3*'='+' Pendaftaran Kartu '+ 23*'=')
    print('Hapus - Hapus kartu yang terdaftar')

# Inisialisasi  
    counter = 0

# Input & Proses
    if '' not in ID:
        print('Error: Jumlah akun maksimum telah tercapai')
    else:
        new_id = input('\nMasukkan ID Baru >> ')
    # Penghapusan ID
    if new_id == 'hapus':
        new_id = input('Masukkan ID yang akan dihapus >> ')
        hapus = True
    else:
        hapus = False
    if new_id in ID:
        print('Error: ID sudah terdaftar')
    # Memasukkan ID baru ke dalam list
    for i in range(N*3):
        if ID[i] == '' and counter < 1 and new_id not in ID and not hapus:
            ID[i] = new_id
            counter += 1
            print('\n'+26*'-' + '\n' + f'ID : {ID[i]}\nID Berhasil Terdaftar' + '\n' + 26*'-')
        elif hapus and ID[i] == new_id:
            ID[i] = ''
            counter += 1
            print('\n'+26*'-' + '\n' + f'ID : {new_id}\nID Berhasil Terhapus' + '\n' + 26*'-')
    return ID
def masuk (parkir_penuh, ID, plat, aktif, waktu):  # Simulasi Kendaraan Masuk
# KAMUS
  # ulang_masuk : bool  -> Perulangan simulasi masuk
  # kode_parkir : str
  # waktu_masuk : str
  # plat_no     : str

    
# Header
    print(3*'='+' Simulasi Kendaraan Masuk '+ 16*'=')

# Inisialisasi
    found = False
    counter = 0  
    ulang_masuk = True
    # Pesan jika parkir terisi penuh
    if parkir_penuh:
        print('\n'+22*'X' + '\n' + 'Parkir Terisi Penuh' + '\n' + 22*'X')
    else:
        # Antarmuka
        print()
        print(45*'-' + '\n' + '|' + 14*' ' + f'Selamat Datang!' + 14*' ' + '|' + '\n' + 45*'-')
        print()

# Input & Proses
    # Scan ID
    while ulang_masuk and not parkir_penuh:
        kode_parkir = input('Masukkan Kode Kartu\nUID >> ')
        if kode_parkir in aktif:
            found = False
            print('\nError : Kartu sedang aktif\n')
        elif kode_parkir in ID and kode_parkir not in aktif:     # Mengecek UID terdaftar atau tidak
            found = True
            ulang_masuk = False
        elif kode_parkir not in ID:     # Kode tidak terdaftar
            print('\nError : Kartu tidak terdaftar\n')
            found = False
        if kode_parkir == 'menu':   # Kembali ke menu
            ulang_masuk = False
        
            

    # Melanjutkan proses jika ID terdaftar
    if found and not parkir_penuh:
        waktu_masuk = input('Waktu Masuk >> ')
        plat_no = input('Plat Nomor >> ')
        # Memasukkan data ke dalam list
        for i in range(N):
            if aktif[i] == '' and counter < 1:
                aktif[i] = kode_parkir
                waktu[i] = waktu_masuk
                plat[i] = plat_no
                counter += 1
# Output
        print()
        print(22*'-' + '\n' + f'UID         : {kode_parkir}\nWaktu masuk : {waktu_masuk}\nPlat Nomor  : {plat_no}' + '\n' + 22*'-')
        buka = True
        operasi_portal(buka)

    return aktif,waktu,plat
def keluar (aktif,waktu,plat):                     # Simulasi Kendaraan Keluar
# KAMUS
  # ulang_keluar    :
  # kode_parkir     :
  # plat_no     

# Antarmuka
    print()
    print(3*'='+' Simulasi Kendaraan Keluar '+ 15*'=')
    print()

# Inisialisasi
    found = False
    ulang_keluar = True

# Input & Proses
    while ulang_keluar:
        kode_parkir = input('Masukkan kode kartu:\nUID >> ')
        if kode_parkir == 'menu':    # Mengakhiri sub-simulasi
            ulang_keluar = False
        elif kode_parkir not in aktif:
            print('\nError : Kode sedang tidak aktif\n')
            buka = False
        plat_no = input('Plat Nomor >>  ')
        if plat_no == 'menu':    # Mengakhiri sub-simulasi
            ulang_keluar = False
        elif plat_no not in plat:   # Plat berbeda dengan ID yang sedang aktif
            print('\nError : Plat nomor tidak sesuai\n')
        # Menghapus data dari list
        for i in range(N):
            if kode_parkir in aktif and plat_no in plat:
                aktif[i] = ''
                waktu[i] = ''
                plat[i] = ''
                ulang_keluar = False
                found = True
# Output
    if not ulang_keluar and found:
        buka = True
        operasi_portal(buka)
        print(45*'-' + '\n' + '|' + 14*' ' + f'Selamat Jalan!' + 14*' ' + '|' + '\n' + 45*'-')
    return aktif, waktu, plat
