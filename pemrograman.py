#KAMUS
harga = 0
qty = 0
total_harga = 0
diskon_persen = 0
harga_setelah_diskon = 0
Pembayaran = 0
kembalian = 0

#ALGORITMA
print("JUAL BELI\n")
print("=========================")
harga = int(input('harga barang : '))
qty = int(input('jumlah barang : '))
total_harga = harga* qty
print (f'total_harga = {total_harga:,.2f}')
diskon_persen = float(input('diskon (diskon_dalam_persen): '))
diskon =total_harga * (diskon_persen /100)
harga_setelah_diskon = total_harga - diskon
print (f'harga_setelan_diskon = {harga_setelah_diskon:,.2f}')
Pembayaran = float(input('jumlah pembayaran :'))
kembalian = pembayaran - harga_setelah_diskon
print (f'kembalian = {kembalian:,.2f}')
print('===============================')
print("Terimakasih sudah berbelanja!\n")