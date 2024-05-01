#Bagian A
n = int(input("Masukkan nilai n: "))
print("Hasil Bagian A:")
for i in range(n):
    print(i**2)

#Bagian B
print("\nHasil Bagian B:")
for i in range(n):
    if i % 2 != 0:  # Jika ganjil
        print(i**2)
