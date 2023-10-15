class Calculator:
    def tambah(self, angka1, angka2):
        return angka1 + angka2

    def kurang(self, angka1, angka2):
        return angka1 - angka2

    def kali(self, angka1, angka2):
        return angka1 * angka2

    def bagi(self, angka1, angka2):
        if angka2 == 0:
            return "Not Defined"
        return angka1 / angka2

    def pangkat(self, angka, eksponen):
        return angka ** eksponen

def main():
    calculator = Calculator()

    print("Pilih operasi yang ingin Anda lakukan:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Pangkat")

    pilihan = input("Masukkan nomor operasi (1/2/3/4/5): ")

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == "1":
        hasil = calculator.tambah(angka1, angka2)
    elif pilihan == "2":
        hasil = calculator.kurang(angka1, angka2)
    elif pilihan == "3":
        hasil = calculator.kali(angka1, angka2)
    elif pilihan == "4":
        hasil = calculator.bagi(angka1, angka2)
    elif pilihan == "5":
        eksponen = int(input("Masukkan eksponen untuk perhitungan pangkat: "))
        hasil = calculator.pangkat(angka1, eksponen)
    else:
        hasil = "Pilihan tidak valid"

    print(f"Hasil: {hasil}")



if __name__ == "__main__":
    main()
