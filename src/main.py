
import os
import sys
import time


# ==========================================
# IDENTITAS MAHASISWA
# ==========================================

NAMA = "Fuad Jabbar Dzakwan"
NIM = "26552011105"
KELAS = "TIF SB 25"

MATA_KULIAH = "Kompleksitas Algoritma"
SKS = "3 SKS"

DOSEN = "Ahsani Takwim, S.Kom., M.Kom"
EMAIL_DOSEN = "ahsanitakwim@sttbandung.ac.id"


# ==========================================
# ANSI COLORS
# ==========================================

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
GRAY = "\033[90m"


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_center(text, width=60):
    print(text.center(width))


def print_line(width=60):
    print(f"{CYAN}{'═' * width}{RESET}")


def typing_effect(text, delay=0.025):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ==========================================
# MAIN GREETING
# ==========================================

def main():
    clear_screen()

    width = 60

    print()
    print_line(width)

    print_center(f"{BOLD}{YELLOW}WELCOME TO MY PROJECT UTS{RESET}", width)
    print_center(f"{BOLD}{WHITE}KOMPLEKSITAS ALGORITMA{RESET}", width)

    print_line(width)

    print()
    print(f"{BOLD}{CYAN}IDENTITAS MAHASISWA{RESET}")
    print(f"{GRAY}{'─' * width}{RESET}")

    print(f"{WHITE}Nama          : {NAMA}{RESET}")
    print(f"{WHITE}NIM           : {NIM}{RESET}")
    print(f"{WHITE}Kelas         : {KELAS}{RESET}")

    print()
    print(f"{BOLD}{CYAN}INFORMASI MATA KULIAH{RESET}")
    print(f"{GRAY}{'─' * width}{RESET}")

    print(f"{WHITE}Mata Kuliah   : {MATA_KULIAH}{RESET}")
    print(f"{WHITE}Bobot         : {SKS}{RESET}")

    print()
    print(f"{BOLD}{CYAN}DOSEN PENGAMPU{RESET}")
    print(f"{GRAY}{'─' * width}{RESET}")

    print(f"{WHITE}Nama          : {DOSEN}{RESET}")
    print(f"{WHITE}Email         : {EMAIL_DOSEN}{RESET}")

    print()
    print_line(width)

    print()
    typing_effect(
        f"{GREEN}{BOLD}Hello, welcome to my algorithm project!{RESET}"
    )

    typing_effect(
        f"{WHITE}This project demonstrates algorithm "
        f"analysis and implementation.{RESET}"
    )

    print()
    print_center(f"{YELLOW}Have a great learning experience!{RESET}", width)

    print()
    print_line(width)
    print()


if __name__ == "__main__":
    main()
