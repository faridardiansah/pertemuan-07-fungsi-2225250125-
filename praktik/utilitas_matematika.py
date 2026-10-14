
def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif")

    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif")

    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("\n===== MENU UTILITAS MATEMATIKA =====")
    print("1. Luas Persegi Panjang")
    print("2. Luas Segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("0. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (ketik 1/2/3/4/0): ").strip()

        try:
            if pilihan == "1":
                print("\n--- Luas Persegi Panjang ---")
                p = float(input("Masukkan panjang: "))
                l = float(input("Masukkan lebar: "))
                print("Hasil:", luas_persegi_panjang(p, l))

            elif pilihan == "2":
                print("\n--- Luas Segitiga ---")
                a = float(input("Masukkan alas: "))
                t = float(input("Masukkan tinggi: "))
                print("Hasil:", luas_segitiga(a, t))

            elif pilihan == "3":
                print("\n--- Jumlah 1 sampai n ---")
                n = int(input("Masukkan bilangan bulat n: "))
                print("Hasil:", jumlah_n(n))

            elif pilihan == "4":
                print("\n--- Faktorial ---")
                n = int(input("Masukkan bilangan bulat n: "))
                print("Hasil:", faktorial(n))

            elif pilihan == "0":
                print("Program selesai.")
                break

            else:
                print("Pilihan tidak valid. Masukkan 1, 2, 3, 4, atau 0.")

        except ValueError as e:
            print("Input salah:", e)


if __name__ == "__main__":
    main()
