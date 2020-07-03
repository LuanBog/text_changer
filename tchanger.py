#Made by TheLittleBro122

import random
import sys
import argparse

parser = argparse.ArgumentParser(description="Automate the process of manipulating texts")
parser.add_argument("-t", "--text", type=str, required=True, help="The text that you want to manipulate")

parser.add_argument("-rc", "--randomCapitalization", action="store_true", required=False, help="Randomizes the capitalization")
parser.add_argument("-s", "--separate", type=int, required=False, help="Separates the text by number")
parser.add_argument("-re", "--reverse", action="store_true", required=False, help="Reverses the text")

args = parser.parse_args()

def randomCapitalization(n):
    new = ""

    for letter in n:
        change = random.choice([True, False]);

        if change:
            new = new + letter.upper()
        else:
            new = new + letter.lower()

    return new

def separate(n, space):
    new = ""

    for letter in n:
        new = new + letter + " "*space

    return new

def reverse(n):
    return n[::-1]

if __name__ == "__main__":
    text = args.text

    if args.randomCapitalization:
        text = randomCapitalization(text)
    if args.separate:
        text = separate(text, args.separate)
    if args.reverse:
        text = reverse(text)

    print("\n%s" % (text))
