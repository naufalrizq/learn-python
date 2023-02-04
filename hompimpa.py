import random

user_wins = 0
computer_wins = 0

opsi = ["batu", "kertas", "gunting"]

while True:
    user_input = input("Pilih Batu/Kertas/Gunting atau Q untuk keluar: ").lower()
    if user_input == "q":
        break
    
    if user_input not in opsi:
        continue

    random_number = random.randint(0, 2)# batu: 0, kertas: 1, gunting: 2
    computer_pick = opsi[random_number]
    print("Komputer memilih:", computer_pick + ".")

    if user_input == "batu" and computer_pick == "gunting":
        print("Kamu menang!")
        user_wins += 1

    elif user_input == "kertas" and computer_pick == "batu":
        print("Kamu menang!")
        user_wins += 1

    elif user_input == "gunting" and computer_pick == "kertas":
        print("Kamu menang!")
        user_wins += 1
        
    elif user_input == "gunting" and computer_pick == "gunting":
        print("Seri!")
        user_wins += 0
        
    elif user_input == "kertas" and computer_pick == "kertas":
        print("Seri!")
        user_wins += 0
        
    elif user_input == "batu" and computer_pick == "batu":
        print("Seri!")
        user_wins += 0

    else:
        print("Kamu kalah!")
        computer_wins += 1

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Kamu menang", user_wins, "kali.")
print("Komputer menang", computer_wins, "kali.")
print("Dadah! Terima kasih sudah bermain:3")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")