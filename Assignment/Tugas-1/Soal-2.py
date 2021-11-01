'''
Buatlah sebuah program yang dapat menghitung luas lingkaran.
Program meminta input dari user berupa angka sebagai jari-jari lingkaran.
Program menghitung luas lingkaran dengan rumus πr² 
Π = 22/7
r = jari - jari lingkaran 
Lalu tampilkan ke layar dengan format:
Hint: untuk menampilkan tanda kuadrat gunakan print(“\u00b2”)

Luas lingkaran dengan jari-jari [jari-jari lingkaran] cm adalah [luas lingkaran] cm².

Contoh:
Luas lingkaran dengan jari-jari 7 cm adalah 154.0 cm².
Luas lingkaran dengan jari-jari 10 cm adalah 314.2857142857143 cm².
'''
pi = 22/7
r = int(input("Masukan jari-jari : "))
l = pi * (r ** 2) 
txt = f"Luas lingkaran dengan jari-jari {r} cm adalah {l:.2f} cm²."
print (txt)