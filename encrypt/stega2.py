# written by : P Daligault-Hardy
from PIL import Image as Im
from random import randint
from os import listdir


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


def steganographie_methode_2(rng: int, path: str, text: str):
    """hide a text into a jpg image

    Args:
        rng (int): Degree of randomness you want
        path (str): path to the image
        text (str): text to hide
    """
    image = Im.open(path)
    text = str_to_bin(text)
    x, y = image.size
    for j in range(y):
        if len(text) == 0:
            break
        for i in range(x):
            if len(text) == 0:
                break
            if randint(0, rng + 1) == 0:
                r, g, b = image.getpixel((i, j))
                al = randint(1, 3)
                if al == 1:
                    if r > 1:
                        image.putpixel((i, j), (r - (int(text[0]) + 1), g, b))
                    else:
                        image.putpixel((i, j), (r + (int(text[0]) + 1), g, b))
                elif al == 2:
                    if g > 1:
                        image.putpixel((i, j), (r, g - (int(text[0]) + 1), b))
                    else:
                        image.putpixel((i, j), (r, g + (int(text[0]) + 1), b))
                elif al == 3:
                    if b > 1:
                        image.putpixel((i, j), (r, g, b - (int(text[0]) + 1)))
                    else:
                        image.putpixel((i, j), (r, g, b + (int(text[0]) + 1)))
                text.reverse()
                text.pop()
                text.reverse()
    image.save("image_stega.png")


import contextlib
def stega():
    print("What image do you want to use ? (in pour current repository)")
    all_files = listdir()
    for i, j in enumerate(all_files):
        if ".jpg" in j:
            print(i, " - ", j)
    while True:
        with contextlib.suppress(Exception):
            choice2 = all_files[int(input())]
            break
    print("Type the text you want to hide :")
    while True:
        with contextlib.suppress(Exception):
            choice3 = input()
            break
    print("what degree of random do you want ?")
    while True:
        with contextlib.suppress(Exception):
            choice = int(input())
            break
    steganographie_methode_2(choice, choice2, choice3)
    print("Done !")
