harga = int (input('input harga Barang :'))
qty = int (input('Input Jumlah Barang :'))
total_harga = harga * qty
print('total harga = ', total_harga)
bayar = int(input('Input Pembayaran : '))
kembalian = bayar - total_harga
print('kembalian = ', kembalian)
