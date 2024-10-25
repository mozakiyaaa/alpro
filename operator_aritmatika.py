#deklrasi Variabel 
bil1 = 0
bil2 = 0
jumlah = 0
kurang = 0 
kali = 0
bagi = 0
hsl_bagi = 0
sisa_bagi = 0
pangkat = 0

#input
bil1 = int(Input("Masukkan Bilangan 1 : "))
bil2 = int(Input("Masukkan Bilangan 1 : "))

#proses
jumlah = bil1 + bil2
kurang = bil1 - bil2
kali = bil1 * bil2
bagi = bil1 / bil2
hsl_bagi = bil1 // bil2
sisa_bagi = bil1 % bil2
pangkat = bil1 ** bil2

#output
print()
print(f"Hasil penjumlahan        : ", jumlah)
print(f"Hasil pengurangan        : ", kurang)
print(f"Hasil perkalian          : ", kali)
print(f"Hasil pembagian          : ", bagi)
print(f"Hasil pembagian genap    : ", hsl_genap)
print(f"Sisa hasil bagi          : ", sisa_bagi)
print(f"Hasil perpangkatan       : ", pangkat)
