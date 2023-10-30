from fungsi import menu,kapasitas,operasi_portal,daftar,masuk,keluar
# Kelompok 14
# Simulasi Portal Parkir Otomatis

# Header
print('\n' + 44*'=')
print(6*' '+'SIMULASI PORTAL PARKIR OTOMATIS ')
print('\n'+ 14*' '+'KELOMPOK 14 ')
print(44*'='+'\n')
# KODE UTAMA
# KAMUS
  # N           : int          -> Jumlah Kapasitas Parkir
  # ID          : list of str
  # aktif      : list of str
  # waktu       : list of str
  # plat        : list of str
  # jalan       : bool          -> Master simulasi 
  # ke_menu     : bool          
  # simulasi    : str           -> Handle percabangan simulasi

# Inisialisasi
N = int(input('Masukkan jumlah lahan parkir >> '))
ID = ['' for i in range(N*3)]     # Menyimpan data UID yang terdaftar
aktif = ['' for i in range(N)] # UID yang sedang aktif (parkir)
waktu = ['' for i in range(N)]  # Menyimpan waktu masuk
plat = ['' for i in range(N)]
jalan = True
ke_menu = True    # Kembali ke menu jika True

while jalan:
    simulasi = menu(ke_menu) 
    parkir_penuh = kapasitas(N, aktif)

    # Mendaftarkan Kartu Baru
    if simulasi == 'Daftar' or simulasi == 'daftar':
        ID = daftar(N, ID)
  
    # Kendaraan Masuk
    elif simulasi == 'Masuk' or simulasi == 'masuk':
        aktif, waktu, plat = masuk(N, parkir_penuh, ID, plat, aktif, waktu)
          
    # Kendaraan Keluar
    elif simulasi == 'Keluar' or simulasi == 'keluar':
       aktif, waktu, plat = keluar(N, aktif,waktu,plat)
        
    # Mengecek Status Array
    elif simulasi == 'cek' or simulasi == 'cek':
        print('=== Data ====================================')
        print(f'Data ID : {ID}\nAktif   : {aktif}\nWaktu   : {waktu}\nPlat No : {plat}')
        ke_menu = True
    
    # Menghentikan Simulasi
    elif simulasi == 'end' or simulasi == 'terminate' or simulasi == 'End' or simulasi == 'Terminate' :
        jalan = False
    
    
    else:   # Input selain yang ditentukan
        print('Berikan input yang benar')
        ke_menu = True
print('Simulasi dihentikan')