#  learning python is fun
impression = "learning pytho is fun"
print(impression)
isi = "" #variabel ada isi/ tanpa isi 
print(type(isi))
print(isinstance(isi, str))

# function buat cek isi dan menampilkannya
if isi:
    print("ada isinya "); print("jadinya ini "); print(True)
else:
    print("kosong, tidak ada isinya "); print("membuatnya menjadi "); print(False)

# kalkulator usia
UsiaSekarang = 50
print("My mom born in", 1925-UsiaSekarang)

"""
memem
jadi multiline string ini selama engga di pake buat variabel bakalan dibaca dan tidak di execute
"""

coba = "kita "

def makan():
    # "global coba" global function ini bakal membuat value coba di lokal menjadi global dan bisa dipakai diluar function jadi mending ku coment aja
    coba = "saya "
    print(coba + "makan buah")

makan()
print(f"{coba} makan buah")
# pengen coba unpack tuple,list,etc ke variable

data = ["dimas", 18, 168.5]
Nama , Umur, TinggiBadan = data

print(type(Nama), Nama)
print(type(Umur), Umur)
print(type(TinggiBadan), TinggiBadan)