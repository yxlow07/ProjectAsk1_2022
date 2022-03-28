from time import sleep
print("Semua ukuran dibuat dalam unit cm")


def calc_radius():
    checked = False
    diameter = 0
    while not checked:
        try:
            diameter = float(input("Apakah diameter tin anda: "))
            checked = True
        except ValueError:
            print("Terdapat satu kesalahan dalam input anda. Sila cuba satu kali lagi")

    keputusan = diameter / 2
    print("Jejari ialah {:0.2f}cm".format(keputusan))

def getInpAndCalc():
    checked = False
    ketinggian = 0.00
    jejari = 0
    pi = 3.14159
    while not checked:
        try:
            _ketinggian = float(input("Apakah ketinggian tin anda: "))
            _jejari = float(input("Apakah jejari tin anda: "))
            checked = True
        except ValueError:
            checked = False
            print("Terdapat satu kesalahan dalam input anda. Sila cuba satu kali lagi")

    keputusan = _ketinggian * _jejari * _jejari * pi
    print("Isi padu tin anda adalah {:0.2f}ml".format(keputusan))


def tutorial():
    instructions = ["1. Membuka tin mimuman dan menuang isinya ke dalam satu bekas silinder", "2. Mengukur ketinggian silinder", "3. Mengukur diameter bahagian bawah yang berbentuk bulat", "4. Memilih pilihan 3 dan mendapatkan jejarinya", "5. Memilih pilihan 2 dan mendapatkan isi padunya"]
    for i in range(len(instructions)):
        print(instructions[i])
        sleep(1)


def checkInput(inp, available_inp):
    try:
        return int(inp) in available_inp
    except:
        return False

check_menu = False

print(
    """
=================<== Menu ==>=================
1 -> Tutorial mendapat pengukuran paling tepat
2 -> Pengiraan
3 -> Mengira jejari
4 -> Keluar\n
""")
while not check_menu:
    getInput = input("\nSila pilih salah satu option dari menu: ")
    print()
    if checkInput(getInput, [1, 2, 3, 4]):
        getInput = int(getInput)
        if getInput == 1:
            tutorial()
        elif getInput == 2:
            getInpAndCalc()
        elif getInput == 3:
            calc_radius()
        else:
            print("Terima kasih kerana menggunakan servis kami")
            check_menu = True
    else:
        print("Sila pilih satu option yang sah!")
