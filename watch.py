import random

service = ["HBO Max", "Netflix", "Hulu", "Peacock", "Tubi", "Amazon Prime", "Disney Plus"]
letter = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
numSelect = random.randrange(0, 20)

def pickWatch():
    serv = random.randrange(0, len(service))
    print("Go to " + service[serv])
    lett = random.randrange(0, len(letter))
    print("Search the letter: " + letter[lett].upper())
    print("Select title number: " + str(numSelect))
    
pickWatch()