import keyboard
from random import randint
from time import sleep
from pynput.keyboard import Key, Listener
import os

class Cracking:

    number_of_tries = 1
    
    codes = open('codes.txt', 'r').readlines()

    people = int(input("How many people: "))
    person_number = int(input("You are person number: "))
    count = int(input("Enter the starting count: ")) + person_number - 1

    clear = lambda: os.system('cls')
    clear()

    print("Press b to try a code!")

    
    def crack(self, key):
            
        if hasattr(key, "char"):
            if key.char == 'b':
                code = list(self.codes[self.count][:-1])

                for number in code:
                    sleep(randint(25,176)/1000)
                    keyboard.press_and_release(number)

                message = "Try#" + str(self.number_of_tries) + " Code=" + str(self.codes[self.count])
                print(message)

                f = open("Log.txt", "a")
                f.write(message)

                self.number_of_tries += 1
                self.count += self.people

    def __init__(self):
        with Listener(on_press = self.crack) as listener:
            listener.join()
    
Cracking()