import requests
import random
import time
import os
from colorama import Fore

print("   ____          ____       _                    ")
print("  | __ )  __ _  |  _ \ __ _| |_ ___ _ __   __ _  ")
print("  |  _ \ / _' | | |_) / _' | __/ _ \ '_ \ / _' | ")
print("  | |_) | (_| | |  __/ (_| | ||  __/ | | | (_| | ")
print("  |____/ \__, | |_|   \__,_|\__\___|_| |_|\__, | ")
print("         |___/                            |___/  \n")
print("=================================================")
author = "Bg.Pateng"
print("Author: " + author)
script = "Push Rank Discord"
print("Script: " + script)
telegram = "@bangpateng_group"
print("Telegram: " + telegram)
youtube = "Bang Pateng"
print("Youtube: " + youtube)
print("===========================================")
print('PERINGATAN : TIDAK UNTUK DI PERJUAL-BELIKAN | TOLONG HARGAI PEMBUAT')
print("===========================================\n")

# Menu 1
def menu1():
    print("Menu 1")
    print("Installing...")
    os.system("apt upgrade && update")
    os.system("apt install openssl")
    os.system("pkg install python")
    os.system("pkg install git")
    os.system("git clone https://github.com/bangpateng/Push-Level-Discord-On-Termux")
    os.chdir("Push-Level-Discord-On-Termux")
    os.system("pip install -r requirements.txt")
    print("Installed! Selesai Lanjut ke Nomer 2")

time.sleep(1)

# Menu 2
def menu2():
    channel_id = input("Masukkan ID channel: ")
    waktu1 = int(input("Set Waktu Hapus Pesan: "))
    waktu2 = int(input("Set Waktu Kirim Pesan: "))
    
    os.system('cls' if os.name == 'nt' else 'clear')

    with open("pesan.txt", "r") as f:
        words = f.readlines()

    with open("token.txt", "r") as f:
        authorization = f.readline().strip()

    while True:
            channel_id = channel_id.strip()

            payload = {
                'content': random.choice(words).strip()
            }

            headers = {
                'Authorization': authorization
            }

            r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
            print(Fore.WHITE + "Sent message: ")
            print(Fore.YELLOW + payload['content'])

            response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

            if response.status_code == 200:
                messages = response.json()
                if len(messages) == 0:
                    is_running = False
                    break
                else:
                    time.sleep(waktu1)

                    message_id = messages[0]['id']
                    response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
                    if response.status_code == 204:
                        print(Fore.GREEN + f'Pesan dengan ID {message_id} berhasil dihapus')
                    else:
                     print(Fore.RED + f'Gagal menghapus pesan dengan ID {message_id}: {response.status_code}')
            else:
                print(f'Gagal mendapatkan pesan di channel: {response.status_code}')

            time.sleep(waktu2)

# Pemanggilan menu
while True:
    print("Menu Nya bang Siapkan Kopi Rokonya:\n")
    print("1. Instal Python & Clone Git")
    print("2. Jalankan Program")
    print("3. Keluar\n")
    choice = int(input("Masukkan pilihan: \n"))
    if choice == 1:
        menu1()
    elif choice == 2:
        menu2()
    elif choice == 3:
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
