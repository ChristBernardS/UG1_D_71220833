h = int(input('Masukan Angka: '))

for i in range(1):
    print(' ')
    for i in range(h):
        print(' '*(h-i), '* '*(i+1))
    for i in range(h-2, -1, -1):
        print(' '*(h-i), '* '*(i+1))

print()