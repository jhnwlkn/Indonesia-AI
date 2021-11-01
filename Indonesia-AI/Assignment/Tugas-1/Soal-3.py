'''
Buatlah sebuah program untuk menentukan apakah seorang siswa lulus ujian atau tidak. Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktek minimal 70. 
Program menerima input berupa nilai ujian teori dan praktek, nilai ujian dapat berupa bilangan desimal.
Jika nilai ujian teori dan praktek minimal 70,  maka program akan menampilkan:
Selamat, anda lulus!

Jika nilai ujian teori minimal 70 dan nilai ujian praktek kurang dari 70:
Anda harus mengulang ujian praktek.

Jika nilai ujian teori kurang dari 70 dan nilai ujian praktek minimal 70:
Anda harus mengulang ujian teori.

Jika nilai ujian teori dan ujian praktek kurang dari 70:
Anda harus mengulang ujian teori dan praktek.
'''
nilai_teori = float(input("Masukan nilai ujian teori anda : "))
nilai_praktek = float(input("Masukan nilai ujian praktek anda : "))

if nilai_praktek >= 70 and nilai_teori >= 70:
    print("Selamat, anda lulus!")
elif nilai_teori >= 70 and nilai_praktek < 70:
    print("Anda harus mengulang ujian praktek.")
elif nilai_teori < 70 and nilai_praktek >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")