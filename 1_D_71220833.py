print(f"{20*'='} KASIR {20*'='}")
print()
harga_barang1 = int(input('Harga Barang : '))
total_harga = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_harga[0] = harga_barang1
n = 1

while True:
    pilihan = str(input('Apakah anda membeli barang lagi? [yes/no] : '))
    total_belanja = sum(total_harga)
    if pilihan == 'yes':
        print()
        harga_barang2 = int(input('Harga Barang : '))
        total_harga[n] = harga_barang2
        n += 1
    if pilihan == 'no':
        print(f'\nTOTAL BELANJA : {total_belanja}')
        break