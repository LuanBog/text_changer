#Made by TheLittleBro122
#https://github.com/TheLittleBro122/text_changer

import random
import argparse
import json

parser = argparse.ArgumentParser(description="Automate the process of manipulating texts")
parser.add_argument("-t", "--text", type=str, required=True, help="The text that you want to manipulate")

parser.add_argument("-rc", "--randomcapitalization", action="store_true", required=False, help="Randomizes the capitalization")
parser.add_argument("-s", "--separate", type=int, required=False, help="Separates the text by number")
parser.add_argument("-re", "--reverse", action="store_true", required=False, help="Reverses the text")
parser.add_argument("-c", "--capitalize", action="store_true", required=False, help="Capitalizes the text")
parser.add_argument("-dc", "--decapitalize", action="store_true", required=False, help="Decapitalize the text")
parser.add_argument("-dt", "--duplicatetext", type=int, required=False, help="Duplicates the text")
parser.add_argument("-dl", "--duplicateletters", type=int, required=False, help="Duplicates the letters of the text")
parser.add_argument("-de", "--discordemoji", action="store_true", required=False, help="Makes texts as discord emojis")

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

def capitalize(n):
    return n.upper()

def decapitalize(n):
    return n.lower()

def duplicate_text(n, amount):
    return n*amount

def duplicate_letters(n, amount):
    new = ""

    for letter in n:
        if letter != " ":
            new = new + letter*amount
        else:
            new = new + " "

    return new

def separate(n, space):
    new = ""

    for letter in n:
        new = new + letter + " "*space

    return new

def reverse(n):
    return n[::-1]

def discordemoji(n):
    n = n.lower()

    data = None
    new = ""

    with open("discord-emojis.json") as f:
        data = json.load(f)

    for letter in n:
        if letter != " ":
            if letter in data:
                new = new + data[letter] + " "
            else:
                new = new + letter + " "
        else:
            new = new + "     "

    return new

if __name__ == "__main__":
    text = args.text

    if args.discordemoji:
        text = discordemoji(text)
    else:
        if args.randomcapitalization:
            text = randomCapitalization(text)
        if args.separate:
            text = separate(text, args.separate)
        if args.duplicatetext:
            text = duplicate_text(text, args.duplicatetext)
        if args.duplicateletters:
            text = duplicate_letters(text, args.duplicateletters)
        if args.decapitalize:
            text = decapitalize(text)
        if args.capitalize:
            text = capitalize(text)
        if args.reverse:
            text = reverse(text)

    print("\n%s" % (text))
