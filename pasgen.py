import random as ra
import string as s
import os
import time

while True:
    def cls():
        os.system("CLS")


    def decorator():
        print("----------------------------------------------")


    def decorator2():
        print("===========================")


    social_choosen = str

    smarks = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '[', ']', '/', '+']

    social_media = {
        1: 'fb',
        2: 'gogl',
        3: 'insta',
        4: 'st',
    }
    social_media_2 = {
        1: 'Facebook:',
        2: 'Google:',
        3: 'Instagram:',
        4: 'Steam:',
    }
    extra = str()

    cls()

    decorator()
    print("Welcome to random password generator!\nproject by: Maciej Wiatr")
    decorator()
    print('\n\nAlways remember to save your progress before re-using program!')
    cls()
    decorator2()

    dl = int(input("How long do you want the password to be? \nSuggested lengh is more than 5 :  "))
    decorator2()
    yn = str(input("Do you want to have letters in it? (y/n) "))
    decorator2()
    yn_2 = str(input("Do you want to have special marks in it? (y/n) "))
    decorator2()
    yn_3 = str(input("Do you want to save your password to .txt file? (y/n) "))
    decorator2()
    yn_4 = str(input("Do you want extra features that will help you remember your password?\n"))
    print("Warning! It might extend password lengh! (y/n) ")
    decorator2()
    yn_5 = str(input("Do you want it to contain some extra word? (e.g. Your dogs name) (y/n) "))
    if (yn_5 == 'y'):
        extra = str(input("Type it here: "))

    password = str()

    cls()


    def randwithlet():
        global password, yn_2, smarks
        if (yn_2 == "n"):
            for i in range(dl):
                password = password + ra.choice(s.ascii_letters.upper()) + str(ra.randrange(10)) + ra.choice(
                    s.ascii_letters) + ra.choice(s.ascii_letters.upper())
        elif (yn_2 == "y"):
            for i in range(dl):
                password = password + ra.choice(s.ascii_letters.upper()) + ra.choice(
                    s.ascii_letters.lower()) + ra.choice(smarks) + str(ra.randrange(10)) + ra.choice(
                    s.ascii_letters) + ra.choice(smarks)


    def randwithoutlet():
        global password, yn_2, smarks
        if (yn_2 == 'n'):
            for i in range(dl):
                password = password + str(ra.randrange(10))
        elif (yn_2 == "y"):
            for i in range(dl):
                password = password + str(ra.randrange(10)) + ra.choice(smarks)


    if (yn == "y"):
        randwithlet()
    elif (yn == "n"):
        randwithoutlet()
    fil = open("LastPassword.txt", "w+")
    print("\n")
    print("============== This is your password =============\n")
    finalresult = password[:dl]
    if (yn_5 == 'y'):
        finalresult = finalresult + extra
    print(finalresult + "\n")
    print("==================================================")
    print("\n\n")
    if (yn_4 == "y"):
        print("============== Your Password for social media accounts =============\n")
        for wd in social_media.keys():
            print(social_media_2[wd] + "\n")
            print(finalresult + "_" + social_media[wd] + "\n")
        print("====================================================================")

    if (yn_3 == "y"):
        fil = open("LastPassword.txt", "w+")
        fil.write("Main Password: \n" + finalresult + "\n")
        for y in social_media_2.keys():
            fil.write(social_media_2[y] + "\n")
            fil.write(finalresult + "_" + social_media[y] + "\n")
        fil.close()
        print("\nYour password has been saved!\n")

    rest = input("Restart? (y/n) ")
    if (rest == "y"):
        continue
    elif (rest == "n"):
        print("Goodbye!")
        time.sleep(1)
        break
    else:
        print("Invalid output!")
        for x in 'time':
            time.sleep(0.2) 
            print(".")
    continue
