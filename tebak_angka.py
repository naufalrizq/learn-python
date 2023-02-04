import random

batas_angka = input("Masukkan batas angka yang akan ditebak: ")

if batas_angka.isdigit():
    batas_angka = int(batas_angka)

    if batas_angka <= 0:
        print('Tidak boleh memasukkan angka kurang dari 0!')
        quit()
else:
    print('Tidak boleh memasukkan angka 0!')
    quit()

angka_random = random.randint(0, batas_angka)
tebakan = 0

while True:
    tebakan += 1
    user_guess = input("Coba tebak angkanya: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Coba lagi!.')
        continue

    if user_guess == angka_random:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Selamat, kamu berhasil menebak angkanya!")
        break
    elif user_guess > angka_random:
        print("Angka tebakanmu terlalu tinggi!")
    else:
        print("Angka tebakanmu terlalu rendah!")

print("Kamu berhasil dalam", tebakan, " kali tebakan")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
