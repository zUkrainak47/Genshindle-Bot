# import pytesseract as pyt
# from pytesseract import Output
# from PIL import Image
# import cv2

import random
from pyautogui import *
import json
import pyautogui
import time
import keyboard
from random import choice
from collections import Counter
import win32api
import win32con


daily_mode = False  # set this to True to use in Normal (daily) mode and False to use in Endless mode!


# try:
#     with open('pyt.txt', 'r') as file:
#         pyt_folder = file.read()
#         if pyt_folder.split('\\')[-1] == 'tesseract.exe':
#             pyt.pytesseract.tesseract_cmd = pyt_folder
#         else:
#             print("The path must be to the tesseract.exe file")
# except FileNotFoundError:
#     with open('pyt.txt', 'w') as file:
#         file.write('Put your tesseract.exe path here')


visions = ["pyro", "hydro", "cryo", "anemo", "geo", "electro", "dendro"]
regions = ["mondstadt", "liyue", "inazuma", "sumeru", "fontaine", "snezhnaya", "none"]
weapons = ["sword", "claymore", "polearm", "catalyst", "bow"]
versions = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
            2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8,
            3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7,
            4.0, 4.1, 4.2, 4.3, 4.4]
arrows = ["2 down arrow_for_wriothesley", "2 down arrow_for_wrio_again", "2 down arrow", "2 up arrow", "1 up arrow", "1 down arrow", "1 down arrow_again"]
arrow_map = {"2": " way", "1": "", "up": "later", "down": "earlier"}
location = (472, 516, 976, 116)

from pathlib import Path
Path(".\logs").mkdir(parents=True, exist_ok=True)

try:
    with open('.\logs\log.txt', 'r') as file:
        pass
except FileNotFoundError:
    with open('.\logs\log.txt', 'w') as file:
        file.write('{}')

with open('.\logs\log.txt') as file:
    data = file.read()
log = json.loads(data)


class Character:
    def __init__(self, name, region, vision, weapon, version):
        self.name = name
        self.region = region
        self.vision = vision
        self.weapon = weapon
        self.version = version


characters = [Character("Amber", "mondstadt", "Pyro", "Bow", 1.0),
              Character("Barbara", "mondstadt", "Hydro", "Catalyst", 1.0),
              Character("Beidou", "liyue", "Electro", "Claymore", 1.0),
              Character("Bennett", "mondstadt", "Pyro", "Sword", 1.0),
              Character("Chongyun", "liyue", "Cryo", "Claymore", 1.0),
              Character("Diluc", "mondstadt", "Pyro", "Claymore", 1.0),
              Character("Fischl", "mondstadt", "Electro", "Bow", 1.0),
              Character("Jean", "mondstadt", "Anemo", "Sword", 1.0),
              Character("Kaeya", "mondstadt", "Cryo", "Sword", 1.0),
              Character("Keqing", "liyue", "Electro", "Sword", 1.0),
              Character("Klee", "mondstadt", "Pyro", "Catalyst", 1.0),
              Character("Lisa", "mondstadt", "Electro", "Catalyst", 1.0),
              Character("Mona", "mondstadt", "Hydro", "Catalyst", 1.0),
              Character("Ningguang", "liyue", "Geo", "Catalyst", 1.0),
              Character("Noelle", "mondstadt", "Geo", "Claymore", 1.0),
              Character("Qiqi", "liyue", "Cryo", "Sword", 1.0),
              Character("Razor", "mondstadt", "Electro", "Claymore", 1.0),
              Character("Sucrose", "mondstadt", "Anemo", "Catalyst", 1.0),
              Character("Venti", "mondstadt", "Anemo", "Bow", 1.0),
              Character("Xiangling", "liyue", "Pyro", "Polearm", 1.0),
              Character("Xingqiu", "liyue", "Hydro", "Sword", 1.0), Character("Diona", "mondstadt", "Cryo", "Bow", 1.1),
              Character("Tartaglia", "snezhnaya", "Hydro", "Bow", 1.1),
              Character("Xinyan", "liyue", "Pyro", "Claymore", 1.1),
              Character("Zhongli", "liyue", "Geo", "Polearm", 1.1),
              Character("Albedo", "mondstadt", "Geo", "Sword", 1.2), Character("Ganyu", "liyue", "Cryo", "Bow", 1.2),
              Character("Hu Tao", "liyue", "Pyro", "Polearm", 1.3), Character("Xiao", "liyue", "Anemo", "Polearm", 1.3),
              Character("Rosaria", "mondstadt", "Cryo", "Polearm", 1.4),
              Character("Eula", "mondstadt", "Cryo", "Claymore", 1.5),
              Character("Yanfei", "liyue", "Pyro", "Catalyst", 1.5),
              Character("Kazuha", "inazuma", "Anemo", "Sword", 1.6),
              Character("Ayaka", "inazuma", "Cryo", "Sword", 2.0),
              Character("Sayu", "inazuma", "Anemo", "Claymore", 2.0),
              Character("Yoimiya", "inazuma", "Pyro", "Bow", 2.0), Character("Aloy", "none", "Cryo", "Bow", 2.1),
              Character("Kujou Sara", "inazuma", "Electro", "Bow", 2.1),
              Character("Raiden Shogun", "inazuma", "Electro", "Polearm", 2.1),
              Character("Kokomi", "inazuma", "Hydro", "Catalyst", 2.1),
              Character("Thoma", "inazuma", "Pyro", "Polearm", 2.2),
              Character("Itto", "inazuma", "Geo", "Claymore", 2.3), Character("Gorou", "inazuma", "Geo", "Bow", 2.3),
              Character("Shenhe", "liyue", "Cryo", "Polearm", 2.4),
              Character("Yun Jin", "liyue", "Geo", "Polearm", 2.4),
              Character("Yae Miko", "inazuma", "Electro", "Catalyst", 2.5),
              Character("Ayato", "inazuma", "Hydro", "Sword", 2.6),
              Character("Kuki Shinobu", "inazuma", "Electro", "Sword", 2.7),
              Character("Yelan", "liyue", "Hydro", "Bow", 2.7),
              Character("Heizou", "inazuma", "Anemo", "Catalyst", 2.8),
              Character("Collei", "sumeru", "Dendro", "Bow", 3.0),
              Character("Dori", "sumeru", "Electro", "Claymore", 3.0),
              Character("Tighnari", "sumeru", "Dendro", "Bow", 3.0),
              Character("Candace", "sumeru", "Hydro", "Polearm", 3.1),
              Character("Cyno", "sumeru", "Electro", "Polearm", 3.1),
              Character("Nilou", "sumeru", "Hydro", "Sword", 3.1), Character("Layla", "sumeru", "Cryo", "Sword", 3.2),
              Character("Nahida", "sumeru", "Dendro", "Catalyst", 3.2),
              Character("Faruzan", "sumeru", "Anemo", "Bow", 3.3),
              Character("Wanderer", "sumeru", "Anemo", "Catalyst", 3.3),
              Character("Alhaitham", "sumeru", "Dendro", "Sword", 3.4),
              Character("Yaoyao", "liyue", "Dendro", "Polearm", 3.4),
              Character("Dehya", "sumeru", "Pyro", "Claymore", 3.5),
              Character("Mika", "mondstadt", "Cryo", "Polearm", 3.5),
              Character("Baizhu", "liyue", "Dendro", "Catalyst", 3.6),
              Character("Kaveh", "sumeru", "Dendro", "Claymore", 3.6),
              Character("Kirara", "inazuma", "Dendro", "Sword", 3.7),
              Character("Freminet", "fontaine", "Cryo", "Claymore", 4.0),
              Character("Lynette", "fontaine", "Anemo", "Sword", 4.0),
              Character("Lyney", "fontaine", "Pyro", "Bow", 4.0),
              Character("Neuvillette", "fontaine", "Hydro", "Catalyst", 4.1),
              Character("Wriothesley", "fontaine", "Cryo", "Catalyst", 4.1),
              Character("Charlotte", "fontaine", "Cryo", "Catalyst", 4.2),
              Character("Furina", "fontaine", "Hydro", "Sword", 4.2),
              Character("Chevreuse", "fontaine", "Pyro", "Polearm", 4.3),
              Character("Navia", "fontaine", "Geo", "Claymore", 4.3),
              Character("Gaming", "liyue", "Pyro", "Claymore", 4.4),
              Character("Xianyun", "liyue", "Anemo", "Catalyst", 4.4)]

# characters.append(Character("Chiori", "liyue", "Geo", "Sword", 4.5))

pool = []
eligible_regions = []
eligible_visions = []
eligible_weapons = []
eligible_versions = []


def v(a):  # since im storing version screenshots in the "x x yes" format i need to covert 4.4 to "4 4"
    return str(a).replace(".", " ")


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def screenshot():
    img = pyautogui.screenshot(region=location)
    return img


# def locate(image, condition="yes"):
#     condition = ' ' + condition
#     return pyautogui.locateOnScreen(f'{image}{condition}.png',
#                                     region=location, confidence=0.95) is not None


def stop(q):
    if keyboard.is_pressed('ctrl'):
        if not q:
            print("You quit")
        return True
    return False

def waiting():
    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    sleep(1)
    print("Ok, looking now")
    return


def find_character(el_reg, el_vis, el_weap, el_ver, know_vision, know_region, know_weapon, know_version, character):
    t = screenshot()

    if not know_region:
        r, g, b = t.getpixel((555, 25))
        if (g, b) == (25, 25):
            el_reg = [r for r in el_reg if r != character.region.lower()]
            print(f"The character is not from {character.region}!")
        else:
            el_reg = [character.region.lower()]
            print(f"The character is from {character.region}!")
            know_region = True

    if not know_vision:
        r, g, b = t.getpixel((667, 33))
        if (g, b) == (25, 25):
            el_vis = [vis for vis in el_vis if vis != character.vision.lower()]
            print(f"The character is not {character.vision}!")
        else:
            el_vis = [character.vision.lower()]
            print(f"The character is {character.vision}!")
            know_vision = True

    if not know_weapon:
        r, g, b = t.getpixel((777, 25))
        if (g, b) == (25, 25):
            el_weap = [w for w in el_weap if w != character.weapon.lower()]
            print(f"The character does not use a {character.weapon}!")
        else:
            el_weap = [character.weapon.lower()]
            print(f"The character uses a {character.weapon}!")
            know_weapon = True

    if not know_version:
        r, g, b = t.getpixel((888, 25))  # correct version
        if (g, b) != (25, 25):
            el_ver = [character.version]
            know_version = True
        else:
            print(f"The character did not release in {character.version}!")
            el_ver = [ver for ver in el_ver if ver != character.version]
            img = pyautogui.screenshot(region=location)
            img.save(r'.\logs\last incorrect version seen.png')
            for arrow in arrows:
                try:
                    sleep(0.2)
                    if (pyautogui.locateOnScreen(f".\Arrows\{arrow}.png", region=(472, 468, 976, 170), confidence=0.95) is not None):
                        img = pyautogui.screenshot(region=(472, 468, 976, 170))
                        img.save(r'.\logs\last arrow seen.png')
                        # try:
                        #     image = cv2.imread('last arrow seen.png')
                        #     text = pyt.image_to_string(image)
                        #     print(f"text: {text} text end here")
                        # except FileNotFoundError:
                        #     print('Go to line 220 in the code')
                        #     '''
                        #         Tesseract not installed.
                        #         Follow the tutorial at https://youtu.be/HHHkh9IOqhI or do the following:
                        #         Go to https://github.com/UB-Mannheim/tesseract/wiki and download the installer.
                        #         Save the destination folder you choose while using the installer!!!
                        #     '''
                        # except:
                        #     print("Verify that pyt.txt leads to your tesseract.exe location")
                        arrow_list = arrow.split()[:-1]
                        print(f"They released{arrow_map[arrow_list[0]]} {arrow_map[arrow_list[1]]}")
                        if arrow_list[0] == '1':
                            if arrow_list[1] == 'up':
                                el_ver = [ver for ver in el_ver if ((ver > character.version) and (ver - character.version <= 1))]
                            else:
                                el_ver = [ver for ver in el_ver if ((ver < character.version) and (character.version - ver <= 1))]
                        elif arrow_list[1] == 'up':
                            el_ver = [ver for ver in el_ver if ((ver > character.version) and (ver - character.version > 1))]
                        else:
                            el_ver = [ver for ver in el_ver if ((ver < character.version) and (character.version - ver > 1))]
                        break
                except ImageNotFoundException:
                    print(f"Couldn't locate {arrow}...")
            else:
                print("THIS IS NOT GOOD. COULDN'T FIND ANY ARROWS")
                try:
                    with open('arrow.txt', 'a') as file:
                        file.write(f'\n{character.name}')
                except FileNotFoundError:
                    with open('arrow.txt', 'w') as file:
                        file.write(f'{character.name}')

                # this should NOT occur and if it does, the program will not work optimally.
                # if you notice this, try replacing the arrows i provided with screenshots of your own arrows
                # (take them at 100% window size, in fullscreen and 100% system scale)
                # if that doesn't help recognize the arrows, i haven't found a fix yet unfortunately

    # print(el_reg, el_vis, el_weap, el_ver)
    print("Possible versions:", el_ver)
    return el_reg, el_vis, el_weap, el_ver, know_vision, know_region, know_weapon, know_version


keyboard.press_and_release('alt+tab')
sleep(0.2)
keyboard.press_and_release('ctrl+0')

sleep(0.05)

grey = (33, 37, 41)
black = (13, 15, 15)
gray = (26, 26, 26)
colors = (grey, black, gray)


temp1 = pyautogui.screenshot(region=(1, 1, 2, 2))
r1, g1, b1 = temp1.getpixel((1, 1))
test1 = (r1, g1, b1) in colors

temp2 = pyautogui.screenshot(region=(1, 1, 360, 10))
r2, g2, b2 = temp2.getpixel((358, 8))
test2 = (r2, g2, b2) in colors

temp3 = pyautogui.screenshot(region=(1, 1, 1920, 50))
r3, g3, b3 = temp3.getpixel((1900, 17))
test3 = (r3, g3, b3) in colors

master_test = test1 and test2 and test3
if not master_test:
    keyboard.press_and_release('f11')


lost = False
quit = False
daily = False

while not lost and not quit and not daily:

    if daily_mode:
        daily = True

    know_vision, know_region, know_weapon, know_version = False, False, False, False
    flag = False
    for i in range(5):
        # quit = stop(quit)
        # if quit:
        #     break
        # time.sleep(3)
        quit = stop(quit)
        if quit:
            break
        if not flag:
            flag = True
            pool = characters.copy()
            eligible_regions = regions.copy()
            eligible_visions = visions.copy()
            eligible_weapons = weapons.copy()
            eligible_versions = versions.copy()
        click(1000, 334)
        click(1000, 334)
        time.sleep(0.1)

        # Count the occurrences of each property
        region_counts = Counter(character.region for character in pool)
        vision_counts = Counter(character.vision for character in pool)
        weapon_counts = Counter(character.weapon for character in pool)
        version_counts = Counter(character.version for character in pool)

        # Find the character with the most common properties
        char = max(pool, key=lambda character: (
            region_counts[character.region],
            vision_counts[character.vision],
            weapon_counts[character.weapon],
            version_counts[character.version]
        ))
        writing = char.name
        most_common_count = max(
            region_counts[char.region],
            vision_counts[char.vision],
            weapon_counts[char.weapon],
            version_counts[char.version]
        )

        keyboard.write(writing)
        keyboard.press_and_release('enter')
        time.sleep(0.3)
        if daily:
            quit = stop(quit)
            if quit:
                break
        pic = pyautogui.screenshot(region=(550, 350, 2, 2))
        r, g, b = pic.getpixel((1, 1))
        if (g > 80) and (r < 40):
            print(f"We win - {writing.upper()}")
            # time.sleep(1)
            if not daily:
                if writing in log:
                    log[writing] += 1
                    if len(log) != len(characters):
                        progress = f" ({len(log)}/{len(characters)} characters found)"
                    else:
                        progress = ' You found every character!'
                    print(f"You found {writing} {log[writing]} times!{progress}")
                else:
                    log[writing] = 1
                    if len(log) != len(characters):
                        progress = f" ({len(log)}/{len(characters)} characters found)"
                    else:
                        progress = ' You found every character!'
                    print(f"You discovered {writing}!{progress}")
                with open('.\logs\log.txt', 'w') as file:
                    file.write(json.dumps(log))
                print("\n--------------------------\n")
            break
        elif r >= 50:
            print(f"We lose. Pool: {[character.name for character in pool]}")
            lost = True
            break
        else:
            print(f"Guessing {writing}... ({most_common_count})")
        quit = stop(quit)
        if quit:
            break
        time.sleep(0.7)

        quit = stop(quit)
        if quit:
            break

        if daily:
            waiting()

        eligible_regions, eligible_visions, eligible_weapons, eligible_versions, know_vision, know_region, know_weapon, know_version = \
            find_character(eligible_regions, eligible_visions, eligible_weapons, eligible_versions, know_vision, know_region, know_weapon, know_version, char)
        time.sleep(0.2)
        # print(eligible_visions)
        pool = [character for character in pool if
                ((character.region.lower() in eligible_regions) and
                 (character.vision.lower() in eligible_visions) and
                 (character.weapon.lower() in eligible_weapons) and
                 (character.version in eligible_versions) and
                 (character.name is not writing))]
        print(f"{len(pool)} left in the pool\n")
        quit = stop(quit)
        if quit:
            break
    else:
        print(f"We do not win. Pool: {[character.name for character in pool]}")
        break
    quit = stop(quit)
    if quit:
        break
    sleep(1)
    quit = stop(quit)
    if quit:
        break
