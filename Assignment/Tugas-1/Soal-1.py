'''
Buatlah sebuah program yang menerima 3 input dari user. 
Input tersebut berupa:
1. Nama bertipe data string
2. Umur bertipe data integer
3. Tinggi bertipe data float 

Lalu tampilkan ke layar dengan format:
Nama saya [Nama], umur saya [Umur] tahun dan tinggi saya [Tinggi] cm.

Contoh:
Nama saya Farhan, umur saya 23 tahun dan tinggi saya 167.5 cm.
'''
name = str(input("Masukan nama anda : "))
age = int(input("Masukan umur anda : "))
tall = float(input ("Masukan tinggi anda : "))

txt = f"Nama saya {name}, umur saya {age} tahun dan tinggi saya {tall} cm."
print (txt)