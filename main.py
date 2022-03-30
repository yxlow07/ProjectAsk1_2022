from time import sleep
from termcolor import colored
print("Semua ukuran dibuat dalam unit cm")


def pcm(msg, color):  # print colored message
    print(colored(msg, color))


def getInputAndCheck(inputs, message, selection=1):
    returns = []
    for i in range(inputs):
        checked = False
        while not checked:
            try:
                if selection == 1:
                    msg = "Sila masukkan " + message[i] + " tin anda: "
                else:
                    msg = message[i]
                get_inp = float(input(msg))
                checked = True, returns.append(get_inp)
            except ValueError:
                pcm("Terdapat satu kesalahan dalam input anda. Sila cuba satu kali lagi", "yellow")
    return returns


def calc_radius():
    diameter = getInputAndCheck(1, ["diameter"])
    keputusan = diameter[0] / 2
    pcm("Jejari ialah {:0.2f}cm".format(keputusan), "green")


def getInpAndCalc():
    inputs = getInputAndCheck(2, ["ketinggian", "jejari"])
    pi = 3.14159
    keputusan = inputs[0] * inputs[1] * inputs[1] * pi
    pcm("Isi padu tin anda adalah {:0.2f}ml".format(keputusan), "green")


def tutorial():
    instructions = ["1. Membuka tin mimuman dan menuang isinya ke dalam satu bekas silinder", "2. Mengukur ketinggian silinder", "3. Mengukur diameter bahagian bawah yang berbentuk bulat", "4. Memilih pilihan 3 dan mendapatkan jejarinya", "5. Memilih pilihan 2 dan mendapatkan isi padunya"]
    for i in range(len(instructions)):
        pcm(instructions[i], "blue")
        sleep(1)


def checkInput(inp, available_inp):
    try:
        return int(inp) in available_inp
    except:
        return False


def menuInput(get_input):
    if checkInput(get_input, [1, 2, 3, 4]):
        if get_input == 1:
            tutorial()
        elif get_input == 2:
            getInpAndCalc()
        elif get_input == 3:
            calc_radius()
        else:
            pcm("Terima kasih kerana menggunakan servis kami", "green")
            exit()

print("\n=================<== Menu ==>=================\n1 -> Tutorial mendapat pengukuran paling tepat\n2 -> Pengiraan\n3 -> Mengira jejari\n4 -> Keluar\n")
while True:
    getInput = getInputAndCheck(1, ["\nSila pilih salah satu option dari menu: "], 0)
    menuInput(int(getInput[0]))
