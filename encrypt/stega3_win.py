# written by : P Daligault-Hardy
from PIL import Image as Im
from random import randint
import cryptocode
from os import listdir
import wmi


class rotation:
    def __init__(self, lis):
        self.lists = [lis[2], lis[0], lis[1]]

    def rotat(self):
        self.lists += [self.lists[0]]
        self.lists.pop(0)
        return self.lists[0]


def getproco():
    c = wmi.WMI()
    for i in c.Win32_Processor():
        a = i.ProcessorId
    return a


encodage_genial = lambda text: cryptocode.encrypt(text, getproco())


def str_to_bin(charac_chain: str):
    """Convert str chain to binary chain

    Args:
        charac_chain (str): str to convert

    Returns:
        _bin_: binary result
    """
    byte_array = charac_chain.encode()
    binary_int = int.from_bytes(byte_array, "big")
    binary_string = bin(binary_int)
    return [j for i, j in enumerate(binary_string) if i not in [0, 1]]


def crea_key(lists, long):
    return "".join(f"{str(i)}i" for i in lists) + str(long)


def keyenr(key):
    with open("key.txt", "w") as fichier:
        fichier.write(key)


def crea_algo():
    return [randint(100, 999) for _ in range(3)]


def steganographie_methode_3_win(path: str, text: str, rng: int):
    text = str_to_bin(text)
    longueur = len(text)
    algo = crea_algo()
    true_algo = rotation(algo)
    keyenr(encodage_genial(crea_key(algo, longueur)))
    image = Im.open(path)
    image2 = Im.open(path)
    x, y = image.size
    for j in range(y):
        for i in range(x):
            if randint(0, 3) == 0:
                r, g, b = image.getpixel((i, j))
                al = randint(1, 3)
                if al == 1:
                    if r > 1:
                        image2.putpixel((i, j), (r - randint(1, 2), g, b))
                    else:
                        image2.putpixel((i, j), (r + randint(1, 2), g, b))
                elif al == 2:
                    if g > 1:
                        image2.putpixel((i, j), (r, g - randint(1, 2), b))
                    else:
                        image2.putpixel((i, j), (r, g + randint(1, 2), b))
                elif al == 3:
                    if b > 1:
                        image2.putpixel((i, j), (r, g, b - randint(1, 2)))
                    else:
                        image2.putpixel((i, j), (r, g, b + randint(1, 2)))
    a = true_algo.rotat()
    compt = 0
    for j in range(y):
        if len(text) == 0:
            break
        for i in range(x):
            compt += 1
            if len(text) == 0:
                break
            if a % 15 == compt % 15:
                r, g, b = image.getpixel((i, j))
                al = randint(1, 3)
                if randint(0, rng) == 0:
                    if al == 1:
                        if r > 1:
                            image2.putpixel((i, j), (r - (int(text[0]) + 1), g, b))
                        else:
                            image2.putpixel((i, j), (r + (int(text[0]) + 1), g, b))
                    elif al == 2:
                        if g > 1:
                            image2.putpixel((i, j), (r, g - (int(text[0]) + 1), b))
                        else:
                            image2.putpixel((i, j), (r, g + (int(text[0]) + 1), b))
                    elif al == 3:
                        if b > 1:
                            image2.putpixel((i, j), (r, g, b - (int(text[0]) + 1)))
                        else:
                            image2.putpixel((i, j), (r, g, b + (int(text[0]) + 1)))
                    text.reverse()
                    text.pop()
                    text.reverse()
                else:
                    image2.putpixel((i, j), (r, g, b))
                a = true_algo.rotat()
    image2.save("image_stega.png")


import contextlib
def stega():
    print("What image do you want to use ? (in pour current repository)")
    all_files = listdir()
    for i, j in enumerate(all_files):
        if ".jpg" in j:
            print(i, " . ", j)
    while True:
        with contextlib.suppress(Exception):
            choice = all_files[int(input())]
            break
    print("Type the text you want to hide :")
    while True:
        with contextlib.suppress(Exception):
            choice2 = input()
            break
    print("what degree of random do you want ?")
    while True:
        with contextlib.suppress(Exception):
            choice3 = int(input())
            break
    steganographie_methode_3_win(choice, choice2, choice3)
    print("Done !")
