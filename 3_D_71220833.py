h_untuk_tinggi_diamond = int(input('Masukan Angka: '))

for i in range(1):
    print(' ')
    for i in range(h_untuk_tinggi_diamond):
        print(' '*(h_untuk_tinggi_diamond-i), '* '*(i+1))
    for i in range(h_untuk_tinggi_diamond-2, -1, -1):
        print(' '*(h_untuk_tinggi_diamond-i), '* '*(i+1))

print()