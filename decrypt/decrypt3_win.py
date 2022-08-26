# written by : P Daligault-Hardy
import contextlib
import cryptocode
from PIL import Image as Im
import wmi

from os import listdir
def getproco():
    c = wmi.WMI()
    for i in c.Win32_Processor():
        a = i.ProcessorId
    return a

decodage_insane = lambda phrase: cryptocode.decrypt(phrase, getproco())

class Ronde:
    def __init__(self, lis):
        self.liste = [lis[2], lis[0], lis[1]]

    def rotat(self):
        self.liste += [self.liste[0]]
        self.liste.pop(0)
        return self.liste[0]
def separateur(liste):
    a = liste.pop()
    return liste, a
def decryptage_methode_3_win(
    chemin_im_origine: str, chemin_im_stega: str, clé: str
):
    algo, longueur = separateur(decodage_insane(clé).split("i"))
    true_algo = Ronde(algo)
    longueur = int(longueur)
    im_origine = Im.open(chemin_im_origine)
    im_stega = Im.open(chemin_im_stega)
    assert im_origine.size == im_stega.size
    x, y = im_origine.size
    compt = 0
    phrase = []
    t = true_algo.rotat()
    for j in range(y):
        if len(phrase) == longueur:
            break
        for i in range(x):
            if len(phrase) == longueur:
                break
            compt += 1
            if int(t) % 15 == compt % 15:
                t = true_algo.rotat()
                a, b, c = im_origine.getpixel((i, j))
                d, e, f = im_stega.getpixel((i, j))
                if (a, b, c) != (d, e, f):
                    phrase.append((abs((a + b + c) - (d + e + f))) - 1)
    return bin_to_str(phrase)

def bin_to_str(liste_bin: list):
    """
    Convertie une chaine binaire en utf-8 en sa phrase decodée.

    Parameters
    ----------
    liste_bin : list
        Liste contenant la representation binaire d'une chaine de caractère.

    Returns
    -------
    str
        Chaine de caractère representant la phrase encodée.

    """
    chaine = "0b"
    for i in liste_bin:
        chaine += str(i)
    chaine_b10 = int(chaine, 2)
    chaine_bytes = chaine_b10.to_bytes((chaine_b10.bit_length() + 7) // 8, "big")
    return chaine_bytes.decode()
def key(path):
    with open(path) as keyfile:
        line = keyfile.readline()
        line = line.replace('\n','')
    return line
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
    print("What is the key file ? (in pour current repository)")
    all_files = listdir()
    for i, j in enumerate(all_files):
        if ".txt" in j:
            print(i, " . ", j)
    while True:
        with contextlib.suppress(Exception):
            choice3 = all_files[int(input())]
            break
    print(decryptage_methode_3_win(choice2, choice,key(choice3)))
    print("press enter key to continue")
    input()