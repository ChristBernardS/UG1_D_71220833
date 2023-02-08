def total_nilai(a, b, c):
    total = ((a*30/100)+(b*30/100)+(c*40/100))
    print(f"Total nilai yang didapat : {total}")
    if total <= 19:
        print(f"Total Nilai Dalam Huruf : E")
    elif total > 19 and total <= 39:
        print(f"Total Nilai Dalam Huruf : D")
    elif total > 39 and total <= 59:
        print(f"Total Nilai Dalam Huruf : C")
    elif total > 59 and total <= 79:
        print(f"Total Nilai Dalam Huruf : B")
    elif total > 79 and total <= 100:
        print(f"Total Nilai Dalam Huruf : A")

# print(f"{8*'-'}Nilai ke 1 {8*'-'}")

for i in range(8):
    print('-', end='')
print(f"Nilai ke 1 {'-'*8}")

nilai1 = int(input('Nilai Harian : '))
nilai2 = int(input('Nilai UTS : '))
nilai3 = int(input('Nilai UAS : '))

for i in range(8):
    print('-', end='')
print(f"Nilai ke 2 {'-'*8}")
nilai4 = int(input('Nilai Harian : '))
nilai5 = int(input('Nilai UTS : '))
nilai6 = int(input('Nilai UAS : '))

total_tugas = (nilai1 + nilai4)/2
total_UTS = (nilai2 + nilai5)/2
total_UAS = (nilai3 + nilai6)/2

total_nilai(total_tugas, total_UTS, total_UAS)