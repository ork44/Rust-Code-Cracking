import keyboard
from random import randint
from time import sleep
from pynput.keyboard import Key, Listener
import os
import pyautogui
import time

class Cracking:

    #Global variables
    number_of_tries = 1
    
    #Put the users input into a variable
    people = int(input("How many people: "))
    person_number = int(input("You are person number: "))
    count = int(input("Enter the starting count: ")) + (person_number - 1)
    trigger_key = str(input("Enter the trigger key: "))[0]
    width, height= pyautogui.size()

    #Input validation
    if people > 10000 : people = 10000
    if person_number > people : person_number = people

    #Read the codes line by line and put them into an array
    codes = open('codes.txt', 'r').readlines()

    #Clear the screen
    clear = lambda: os.system('cls')
    clear()

    print("Press " + trigger_key + " to try a code!")
    

    def click_lock(self):
        timer = 0
        while timer < 0.7:
            time.sleep(0.1)
            timer += 0.1
            keyboard.press('e')
        sleep(randint(10,20)/1000)
        pyautogui.moveTo((randint(75,85)/100) * self.width, (randint(80,95)/100) * self.height)
        sleep(randint(10,20)/1000)
        pyautogui.click(0.8 * self.width, 0.9 * self.height)
        keyboard.release('e')
        sleep(randint(10,20)/1000)


    #Crack function
    def crack(self, key):
        #Check if key has an attribute char  
        if hasattr(key, "char"):
            if key.char == self.trigger_key:
                Cracking.click_lock(self)
                #Put the current code in a list
                code = list(self.codes[self.count][:-1])
                #Loop through list
                for number in code:
                    #Wait random amount
                    sleep(randint(25,176)/1000)
                    #Press the number
                    keyboard.press_and_release(number)
                #Create message
                message = "Try#" + str(self.number_of_tries) + " Code=" + str(self.codes[self.count])
                print(message)
                #Save the message in a log file
                f = open("Log.txt", "a")
                f.write(message)

                self.number_of_tries += 1
                self.count += self.people

    def __init__(self):
        with Listener(on_press = self.crack) as listener:
            listener.join()
    
Cracking()