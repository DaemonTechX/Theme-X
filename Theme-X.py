import os
import time
import sys

def clear():
    os.system('clear')

def login_page():
    while True:
        clear()
        print("[\033[1;31m!\033[0m]\033[1;33m Masukkan PIN Untuk Akses Alat Ini\033[0m")
        print("[\033[1;31m!\033[0m]\033[1;33m Ketik\033[0m \033[1;31mgetpin\033[0m\033[1;33m Untuk Dapatkan PIN\33[0m")
        pin = input(">> ").strip()

        if pin == "byexe-x":
            time.sleep(1)
            break

        elif pin.lower() == "getpin":
            print("[\033[1;31m!\033[0m]\033[1;33m Open Saluran Whatsapp For Get PIN\033[0m")
            time.sleep(2)
            saluran()
            login_page()

        else:
            print("\033[1;31m[✗] PIN Salah\033[0m")
            time.sleep(2)

def saluran():
    print("[\033[1;31m!\033[0m]\033[1;33m Open Saluran Whatsapp For Get PIN\033[0m")
    time.sleep(2)

    url = "https://whatsapp.com/channel/0029VbBLBZ80lwgrRDEnyV0v"

    if "termux" in os.getenv("PREFIX", "").lower():
        os.system(f"termux-open-url '{url}'")
    elif platform.system() == "Linux":
        os.system(f"xdg-open '{url}'")
    elif platform.system() == "Windows":
        os.system(f"start {url}")
    elif platform.system() == "Darwin":
        os.system(f"open {url}")
    else:
        import webbrowser
        webbrowser.open(url)

def report_bug():
    print("[\033[1;31m!\033[0m]\033[1;33m MENUJU TELEGRAM ARBY-HEX\033[0m")
    time.sleep(2)

    url = "https://t.me/ArbyHex"

    if "termux" in os.getenv("PREFIX", "").lower():
        os.system(f"termux-open-url '{url}'")
    elif platform.system() == "Linux":
        os.system(f"xdg-open '{url}'")
    elif platform.system() == "Windows":
        os.system(f"start {url}")
    elif platform.system() == "Darwin":
        os.system(f"open {url}")
    else:
        import webbrowser
        webbrowser.open(url)

def final_proses():
    print("""\033[1:31m
╭─────────────────────╮
│╔═╗╦ ╦╔═╗╔═╗╔═╗╔═╗╔╦╗│
│╚═╗║ ║║  ║  ║╣ ║╣  ║║│
│╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝═╩╝│\033[0m
│\033[1;32m  Code By Arby-Hex\033[0m   │
╰─────────────────────╯

[\033[1;31m!\033[0m]\033[1;33m JALANKAN COMMAND\033[0m \033[1;32msource ~/.bashrc\033[0m
""")

def hacker_theme():
    print("[\033[1;31m01\033[0m]\033[1;33m HACKER 1\033[0m")
    print("[\033[1;31m02\033[0m]\033[1;33m HACKER 2\033[0m")
    print("[\033[1;31m03\033[0m]\033[1;33m HACKER 3\033[0m")
    print("[\033[1;31m04\033[0m]\033[1;33m HACKER 4\033[0m")
    print("[\033[1;31m05\033[0m]\033[1;33m HACKER 5\033[0m")

def anime_theme():
    print("[\033[1;31m01\033[0m]\033[1;33m GIRL SEXI\033[0m")
    print("[\033[1;31m02\033[0m]\033[1;33m POKEMON\033[0m")
    print("[\033[1;31m03\033[0m]\033[1;33m ANYA\033[0m")
    print("[\033[1;31m04\033[0m]\033[1;33m GOJO\033[0m")
    print("[\033[1;31m05\033[0m]\033[1;33m AMATERASU\033[0m")

def grafiti_theme():
    print("[\033[1;31m01\033[0m]\033[1;33m BLACKHAT\033[0m")
    print("[\033[1;31m02\033[0m]\033[1;33m GHOST\033[0m")
    print("[\033[1;31m03\033[0m]\033[1;33m HACKERS\033[0m")
    print("[\033[1;31m04\033[0m]\033[1;33m RED SKULL\033[0m")
    print("[\033[1;31m05\033[0m]\033[1;33m XCRYPTER\033[0m")
    print("")
    print("[\033[1;31m00\033[0m]\033[1;33m EXIT MENU GRAFITI THEME\033[0m")

def banner():
    clear()
    print("╭─────────────────────────────────────────────╮")
    print("│ \033[1;31m•\033[1;33m•\033[1;32m•\033[0m                                         │")
    print("│    \033[1;31m╔╦╗╔═╗╦═╗╔╦╗╦ ╦═╗ ╦  ╔╦╗╦ ╦╔═╗╔╦╗╔═╗\033[0m     │")
    print("│    \033[1;31m ║ ║╣ ╠╦╝║║║║ ║╔╩╦╝   ║ ╠═╣║╣ ║║║║╣ \033[0m     │")
    print("│    \033[1;31m ╩ ╚═╝╩╚═╩ ╩╚═╝╩ ╚═   ╩ ╩ ╩╚═╝╩ ╩╚═╝\033[0m     │")
    print("│           [\033[1;31m!\033[0m]\033[1;33m Code By Arby-Hex\033[0m              │")
    print("│                                             │")
    print("╰─────────────────────────────────────────────╯")
    print("\033[0m")

def banner_hacking():
    clear()
    print("╭─────────────────────────────────────────────╮")
    print("│ \033[1;31m•\033[1;33m•\033[1;32m•\033[0m                                         │")
    print("│    \033[1;31m╔╦╗╔═╗╦═╗╔╦╗╦ ╦═╗ ╦  ╔╦╗╦ ╦╔═╗╔╦╗╔═╗\033[0m     │")
    print("│    \033[1;31m ║ ║╣ ╠╦╝║║║║ ║╔╩╦╝   ║ ╠═╣║╣ ║║║║╣ \033[0m     │")
    print("│    \033[1;31m ╩ ╚═╝╩╚═╩ ╩╚═╝╩ ╚═   ╩ ╩ ╩╚═╝╩ ╩╚═╝\033[0m     │")
    print("│          [\033[1;31m!\033[0m]\033[1;33m MENU TEMA HACKING\033[0m              │")
    print("│                                             │")
    print("╰─────────────────────────────────────────────╯")
    print("\033[0m")

def banner_anime():
    clear()
    print("╭─────────────────────────────────────────────╮")
    print("│ \033[1;31m•\033[1;33m•\033[1;32m•\033[0m                                         │")
    print("│    \033[1;31m╔╦╗╔═╗╦═╗╔╦╗╦ ╦═╗ ╦  ╔╦╗╦ ╦╔═╗╔╦╗╔═╗\033[0m     │")
    print("│    \033[1;31m ║ ║╣ ╠╦╝║║║║ ║╔╩╦╝   ║ ╠═╣║╣ ║║║║╣ \033[0m     │")
    print("│    \033[1;31m ╩ ╚═╝╩╚═╩ ╩╚═╝╩ ╚═   ╩ ╩ ╩╚═╝╩ ╩╚═╝\033[0m     │")
    print("│          [\033[1;31m!\033[0m]\033[1;33m MENU TEMA ANIME\033[0m              │")
    print("│                                             │")
    print("╰─────────────────────────────────────────────╯")
    print("\033[0m")

def banner_grafiti():
    clear()
    print("╭─────────────────────────────────────────────╮")
    print("│ \033[1;31m•\033[1;33m•\033[1;32m•\033[0m                                         │")
    print("│    \033[1;31m╔╦╗╔═╗╦═╗╔╦╗╦ ╦═╗ ╦  ╔╦╗╦ ╦╔═╗╔╦╗╔═╗\033[0m     │")
    print("│    \033[1;31m ║ ║╣ ╠╦╝║║║║ ║╔╩╦╝   ║ ╠═╣║╣ ║║║║╣ \033[0m     │")
    print("│    \033[1;31m ╩ ╚═╝╩╚═╩ ╩╚═╝╩ ╚═   ╩ ╩ ╩╚═╝╩ ╩╚═╝\033[0m     │")
    print("│          [\033[1;31m!\033[0m]\033[1;33m MENU TEMA GRAFITI\033[0m              │")
    print("│                                             │")
    print("╰─────────────────────────────────────────────╯")
    print("\033[0m")

def run_hacker():
    banner_hacker()
    hacker_theme()

    pilihan = input("\n\033[1;31m>> ")

    if pilihan == "01" or pilihan == "1":
        os.system("bash Data/HACKER/hacker1.sh")
        clear()
        final_proses()
        exit()
    elif pilihan == "02" or pilihan == "2":
        os.system("bash Data/HACKER/hacker2.sh")
        clear()
        final_proses()
        exit()
    elif pilihan == "03" or pilihan == "3":
        os.system("bash Data/HACKER/hacker3.sh")
        clear()
        final_proses()
        exit()
    elif pilihan == "04" or pilihan == "4":
        os.system("bash Data/HACKER/hacker4.sh")
        clear()
        final_proses()
        exit()
    elif pilihan == "05" or pilihan == "5":
        os.system("bash Data/HACKER/hacker5.sh")
        clear()
        final_proses()
        exit()
    elif pilihan == "00":
        print("\n\033[1;31m[!]\033[0m KELUAR...\033[1;31m!\033[0m")
        time.sleep(1)
        return
    else:
        print("PILIH YANG BENER\n\033[1;31m!\033[0m")
        time.sleep(1)

    input("\n\033[1;32mTEKAN ENTER UNTUK KEMBALI KE MENU\033[0m...")
    run_hacker()

def run_grafiti():
    banner_grafiti()
    grafiti_theme()

    pilihan = input("\n\033[1;31m>> ")

    if pilihan == "01" or pilihan == "1":
        os.system("bash Data/GRAFITI/blackhat.sh")
        clear()
        final_proses()
        exit()
    elif pilihan == "02" or pilihan == "2":
        os.system("bash Data/GRAFITI/ghost.sh")
        clear()
        final_proses()
        exit()
    elif pilihan == "03" or pilihan == "3":
        os.system("bash Data/GRAFITI/hacker.sh")
        clear()
        final_proses()
        exit()
    elif pilihan == "04" or pilihan == "4":
        os.system("bash Data/GRAFITI/redskull.sh")
        clear()
        final_proses()
        exit()
    elif pilihan == "05" or pilihan == "5":
        os.system("bash Data/GRAFITI/xcrypter.sh")
        clear()
        final_proses()
        exit()
    elif pilihan == "00":
        print("\n\033[1;31m[!]\033[0m KELUAR...\033[1;31m!\033[0m")
        time.sleep(1)
        return
    else:
        print("PILIH YANG BENER\n\033[1;31m!\033[0m")
        time.sleep(1)

    input("\n\033[1;32mTEKAN ENTER UNTUK KEMBALI KE MENU\033[0m...")
    run_grafiti()

def run():
    banner()
    print("[\033[1;31m01\033[0m]\033[1;33m HACKER THEME\033[0m")
    print("[\033[1;31m02\033[0m]\033[1;33m ANIME THEME\033[0m")
    print("[\033[1;31m03\033[0m]\033[1;33m GRAFITI THEME\033[0m")
    print("[\033[1;31m04\033[0m]\033[1;33m REPORT BUG\033[0m")
    print("[\033[1;31m05\033[0m]\033[1;33m KELUAR\033[0m")

    pilihan = input("\n\033[1;31m>> ")

    if pilihan == "01" or pilihan == "1":
        print("[\033[1;31m!\033[0m]\033[1;33m COMING SOON\033[0m")
        time.sleep(2)
    elif pilihan == "02" or pilihan == "2":
        print("[\033[1;31m!\033[0m]\033[1;33m COMING SOON\033[0m")
        time.sleep(2)
    elif pilihan == "03" or pilihan == "3":
        run_grafiti()
    elif pilihan == "04" or pilihan == "4":
        report_bug()
    elif pilihan == "05" or pilihan == "5":
        print("\n\033[1;31m[!]\033[0m KELUAR...\033[1;31m!\033[0m")
        time.sleep(1)
        exit()
    else:
        print("PILIH YANG BENER\n\033[1;31m!\033[0m")
        time.sleep(1)

    input("\n\033[1;32mTEKAN ENTER UNTUK KEMBALI KE MENU\033[0m...")
    run()

def run_utama():
    login_page()
    banner()
    print("[\033[1;31m01\033[0m]\033[1;33m HACKER THEME\033[0m")
    print("[\033[1;31m02\033[0m]\033[1;33m ANIME THEME\033[0m")
    print("[\033[1;31m03\033[0m]\033[1;33m GRAFITI THEME\033[0m")
    print("[\033[1;31m04\033[0m]\033[1;33m REPORT BUG\033[0m")
    print("[\033[1;31m05\033[0m]\033[1;33m KELUAR\033[0m")

    pilihan = input("\n\033[1;31m>> ")

    if pilihan == "01" or pilihan == "1":
        print("[\033[1;31m!\033[0m]\033[1;33m COMING SOON\033[0m")
        time.sleep(2)
    elif pilihan == "02" or pilihan == "2":
        print("[\033[1;31m!\033[0m]\033[1;33m COMING SOON\033[0m")
        time.sleep(2)
    elif pilihan == "03" or pilihan == "3":
        run_grafiti()
    elif pilihan == "04" or pilihan == "4":
        report_bug()
    elif pilihan == "05" or pilihan == "5":
        print("\n\033[1;31m[!]\033[0m KELUAR...\033[1;31m!\033[0m")
        time.sleep(1)
        exit()
    else:
        print("PILIH YANG BENER\n\033[1;31m!\033[0m")
        time.sleep(1)

    input("\n\033[1;32mTEKAN ENTER UNTUK KEMBALI KE MENU\033[0m...")
    run()

if __name__ == "__main__":
    run_utama()
