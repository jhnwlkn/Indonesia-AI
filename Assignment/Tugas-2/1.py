#daftar kontak yang sudah ada
nama = ['Fawwaz', 'John']
nomor = ['08123456789', '08987654321']

#fungsi menampilkan daftar kontak
def dk():
    print('Daftar kontak: ')
    for i in range(len(nama)):
        print(f'\nNama: {nama[i]}')
        print(f'No Telepon: {nomor[i]}\n')

#fungsi menambahkan kontak
def tk():
    print("Masukan nama Anda : ")
    nama.append(input())
    print("Masukan nomor Anda : ")
    nomor.append(input())
    print('\nKontak berhasil ditambahkan ')

#fungsi untuk print menu
def menu():
    print('--- Menu --- ')
    print('1. Daftar Kontak ')
    print('2. Tambah Kontak')
    print('3. Keluar ')

#fungsi main utama
menu()
mn = int(input('Pilih Menu : '))

while mn != 0:
    if (mn == 1):
        dk()
        break
    elif (mn == 2):
        tk()
        break
    elif (mn == 3):
        print('Program selesai, sampai jumpa!')
        break
    else:
        print('Menu tidak tersedia.')
        menu()
