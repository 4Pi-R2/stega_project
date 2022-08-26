# written by : P Daligault-Hardy

from PIL import Image as Im
from os import listdir


def bin_to_str(liste_bin: list):
    chaine = "0b"
    for i in liste_bin:
        chaine += str(i)
    chaine_b10 = int(chaine, 2)
    chaine_bytes = chaine_b10.to_bytes((chaine_b10.bit_length() + 7) // 8, "big")
    return chaine_bytes.decode()


def decriptage_methode_1_2(chemin_im_origine: str, chemin_im_stega: str):
    im_origine = Im.open(chemin_im_origine)
    im_stega = Im.open(chemin_im_stega)
    assert im_origine.size == im_stega.size
    x, y = im_origine.size
    chaine = []
    for j in range(y):
        for i in range(x):
            a, b, c = im_origine.getpixel((i, j))
            d, e, f = im_stega.getpixel((i, j))
            if (a, b, c) != (d, e, f):
                chaine.append((abs((a + b + c) - (d + e + f))) - 1)
    return bin_to_str(chaine)


import contextlib
def stega():
    print("What image do you want to decrypt ? (in pour current repository)")
    all_files = listdir()
    for i, j in enumerate(all_files):
        if ".png" in j:
            print(i, " . ", j)
    while True:
        with contextlib.suppress(Exception):
            choice = all_files[int(input())]
            break
    print("What is the original image ? (in pour current repository)")
    all_files = listdir()
    for i, j in enumerate(all_files):
        if ".jpg" in j:
            print(i, " . ", j)
    while True:
        with contextlib.suppress(Exception):
            choice2 = all_files[int(input())]
            break
    print(decriptage_methode_1_2(choice2, choice))
    print("press enter key to continue")
    input()
