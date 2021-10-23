import keyboard
from random import randint
from time import sleep
from pynput.keyboard import Key, Listener

class Cracking:
    
    codes = open('codes.txt', 'r').readlines()
    count = 0

    def crack(self, key):
            
        if hasattr(key, "char"):
            if key.char == 'b':
                code = list(self.codes[self.count][:-1])

                for number in code:
                    sleep(randint(25,176)/1000)
                    keyboard.press_and_release(number)

                message = "Try#" + str(self.count + 1) + " Code=" + str(self.codes[self.count])

                print(message)
                f = open("Log.txt", "a")
                f.write(message)
                self.count += 1


            
    def __init__(self):
        with Listener(on_press = self.crack) as listener:
            listener.join()
    
Cracking()