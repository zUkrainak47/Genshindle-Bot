# This is not the file you're looking for

import pyautogui
from pyautogui import *
import time
import keyboard
import win32api
import win32con
import json

visions = ["pyro", "hydro", "cryo", "anemo", "geo", "electro", "dendro"]
regions = ["mondstadt", "liyue", "inazuma", "sumeru", "fontaine", "snezhnaya", "none"]
weapons = ["sword", "claymore", "polearm", "catalyst", "bow"]
versions = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
            2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8,
            3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7,
            4.0, 4.1, 4.2, 4.3, 4.4]
arrow_folder = 'arrows 100% scale'
arrows = ["2 up arrow", "1 up arrow", "1 down arrow", "2 down arrow", "1 down arrow_again"]
arrows_wrio = ["2 down arrow_for_wriothesley", "2 down arrow_for_wrio_again", "2 up arrow", "2 down arrow",
               "1 up arrow", "1 down arrow", "1 down arrow_again"]
arrow_map = {"2": " way", "1": "", "up": "later", "down": "earlier"}
location = (472, 516, 976, 116)
arrow_location = (472, 468, 976, 170)
click_y = 334


# ChatGPT code:
def read_settings():
    with open(r'.\settings.txt', 'r') as file:
        lines = file.readlines()
        # Parse each line of the file
        for line in lines:
            # Split each line into key and value pairs
            try:
                key, value = line.strip().split('=')
                key = key.strip()
                value = value.strip()

                # Convert value to integer if applicable
                if value.isdigit():
                    value = int(value)

                # Assign value to corresponding variable
                if key == 'daily_mode':
                    daily_mode = value
                elif key == 'even_faster':
                    even_faster = value
            except ValueError:
                pass
        return daily_mode, even_faster


# ChatGPT code:
def create_settings():
    with open(r'.\settings.txt', 'w') as file:
        file.write('daily_mode = 0\n'
                   'set to 1 to use in Normal (daily) Mode.\n'
                   'set to 0 to use in Endless Mode.\n\n'

                   'even_faster = 0\n'
                   'set to 1 to make the script run around 33% faster. that affects win screen time & console and '
                   'image logs.\n'
                   'set to 0 to be able to see which character was the solution & see more console logs and image logs.'
                   '\n\n'
                   'delete this file (settings.txt) to restore defaults'
                   )


def read_log():
    try:
        with open('.\\logs\\log.txt', 'r') as file:
            pass
    except FileNotFoundError:
        with open('.\\logs\\log.txt', 'w') as file:
            file.write('{}')
    with open('.\\logs\\log.txt') as file:
        data = file.read()
    return data


def v(a):  # since im storing version screenshots in the "x x yes" format i need to covert 4.4 to "4 4"
    return str(a).replace(".", " ")


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def screenshot(loc):
    img = pyautogui.screenshot(region=loc)
    return img


# def locate(image, condition="yes"):
#     condition = ' ' + condition
#     return pyautogui.locateOnScreen(f'{image}{condition}.png',
#                                     region=location, confidence=0.95) is not None


def waiting():
    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    sleep(1)
    print("Ok, looking now")
    return


grey = (33, 37, 41)
black = (13, 15, 15)
gray = (26, 26, 26)
colors = (grey, black, gray)


def f11():
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
        return True
    return False


def stop(q):
    if keyboard.is_pressed('ctrl'):
        if not q:
            print("You quit")
        return True
    return False


def win(scale125, r, g, b):
    if (scale125 and (g > 90) and (20 < r < 35) and (50 < b < 85)) or (not scale125 and (g > 80) and (r < 40)):
        return True
    return False


def write_logs(writing, daily, log, characters, even_faster):
    print(f"We win - {writing.upper()}")
    # time.sleep(1)
    if not daily:
        if writing in log:
            log[writing] += 1
            if len(log) != len(characters):
                progress = f" ({len(log)}/{len(characters)} characters found)"
            else:
                progress = ' You found every character!'
            if not even_faster:
                print(f"You found {writing} {log[writing]} times!{progress}")
        else:
            log[writing] = 1
            if len(log) != len(characters):
                progress = f" ({len(log)}/{len(characters)} characters found)"
            else:
                progress = ' You found every character!'
            if not even_faster:
                print(f"You discovered {writing}!{progress}")
        with open(r'.\logs\log.txt', 'w') as file:
            file.write(json.dumps(log))
        print("\n--------------------------\n")


def check_for_125_scale(r, g, b, location, arrows_wrio, arrow_folder, arrow_location, click_y):
    if (r, g, b) == black:
        scale125 = True
        location = (472, 570, 976, 119)
        arrows_wrio = ["2 down arrow", "2 up arrow", "1 up arrow", "1 down arrow", "1 down arrow_again"]
        arrow_folder = 'arrows 125% scale'
        arrow_location = (472, 505, 976, 190)
        click_y = 355
    else:
        scale125 = False
    return scale125, location, arrows_wrio, arrow_folder, arrow_location, click_y


def update_pool(pool, eligible_regions, eligible_visions, eligible_weapons, eligible_versions, writing):
    return [character for character in pool if
     ((character.region.lower() in eligible_regions) and
      (character.vision.lower() in eligible_visions) and
      (character.weapon.lower() in eligible_weapons) and
      (character.version in eligible_versions) and
      (character.name is not writing))]


def identify_region(character, t, el_reg, even_faster):
    r, g, b = t.getpixel((555, 20))
    if (g, b) == (25, 25):
        if not even_faster:
            print(f"The character is not from {character.region}!")
        return False, [r for r in el_reg if r != character.region.lower()]
    if not even_faster:
        print(f"The character is from {character.region}!")
    return True, [character.region.lower()]


def identify_vision(character, t, el_vis, even_faster):
    r, g, b = t.getpixel((667, 20))
    if (g, b) == (25, 25):
        if not even_faster:
            print(f"The character is not {character.vision}!")
        return False, [vis for vis in el_vis if vis != character.vision.lower()]
    if not even_faster:
        print(f"The character is {character.vision}!")
    return True, [character.vision.lower()]


def identify_weapon(character, t, el_weap, even_faster):
    r, g, b = t.getpixel((777, 20))
    if (g, b) == (25, 25):
        if not even_faster:
            print(f"The character does not use a {character.weapon}!")
        return False, [w for w in el_weap if w != character.weapon.lower()]
    if not even_faster:
        print(f"The character uses a {character.weapon}!")
    return True, [character.weapon.lower()]


def identify_arrow_type(character, arrow, even_faster, el_ver, arrow_location):
    arrow_list = arrow.split()[:-1]
    if not even_faster:
        img = pyautogui.screenshot(region=arrow_location)
        img.save(r'.\logs\last arrow seen.png')
        print(f"They released{arrow_map[arrow_list[0]]} {arrow_map[arrow_list[1]]}")
    if arrow_list[0] == '1':
        if arrow_list[1] == 'up':
            return [ver for ver in el_ver if ((ver > character.version) and (ver - character.version <= 1))]
        return [ver for ver in el_ver if ((ver < character.version) and (character.version - ver <= 1))]
    elif arrow_list[1] == 'up':
        return [ver for ver in el_ver if ((ver > character.version) and (ver - character.version > 1))]
    return [ver for ver in el_ver if ((ver < character.version) and (character.version - ver > 1))]


def didnt_find_any_arrows(character):
    try:
        with open(r'.\logs\arrow.txt', 'a') as file:
            file.write(f'\n{character.name}')
    except FileNotFoundError:
        with open(r'.\logs\arrow.txt', 'w') as file:
            file.write(f'{character.name}')


def log_incorrect_version(character, location):
    print(f"The character did not release in {character.version}!")
    img = pyautogui.screenshot(region=location)
    img.save(r'.\logs\last incorrect version seen.png')


def print_mode(daily_mode, even_faster):
    if daily_mode:
        print("Solving normal mode", end=" ")
    else:
        print("Solving endless mode", end=" ")
    if even_faster:
        print("at supersonic speed")
    else:
        print("at moderate speed")
    print()