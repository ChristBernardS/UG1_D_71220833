input_kalimat = str(input('Kalimat yang ingin diteliti :'))
input_kalimat = input_kalimat.lower()
kata_kunci = str(input('Kata yang dicari : '))
kata_kunci = kata_kunci.lower()
jumlahkata = 0
input_kalimat = input_kalimat.split(' ', -1)
n = 0

for i in range(len(input_kalimat)):
    if input_kalimat[n] == kata_kunci:
        jumlahkata += 1
        n += 1
    else:
        n += 1

print(f"Jumlah kata yang dicari : {jumlahkata}")