import time
from pathlib import Path
from res.genshindle_help_file import *

daily_mode = 0
even_faster = 0

try:
    daily_mode, even_faster = read_settings()
except FileNotFoundError:
    create_settings()

print_mode(daily_mode, even_faster)

Path(".\\logs").mkdir(parents=True, exist_ok=True)

log = json.loads(read_log())


class Character:
    def __init__(self, name, region, vision, weapon, version):
        self.name = name
        self.region = region
        self.vision = vision
        self.weapon = weapon
        self.version = version


characters = {Character("Amber", "mondstadt", "Pyro", "Bow", 1.0),
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
              Character("Xingqiu", "liyue", "Hydro", "Sword", 1.0),
              Character("Diona", "mondstadt", "Cryo", "Bow", 1.1),
              Character("Tartaglia", "snezhnaya", "Hydro", "Bow", 1.1),
              Character("Xinyan", "liyue", "Pyro", "Claymore", 1.1),
              Character("Zhongli", "liyue", "Geo", "Polearm", 1.1),
              Character("Albedo", "mondstadt", "Geo", "Sword", 1.2),
              Character("Ganyu", "liyue", "Cryo", "Bow", 1.2),
              Character("Hu Tao", "liyue", "Pyro", "Polearm", 1.3),
              Character("Xiao", "liyue", "Anemo", "Polearm", 1.3),
              Character("Rosaria", "mondstadt", "Cryo", "Polearm", 1.4),
              Character("Eula", "mondstadt", "Cryo", "Claymore", 1.5),
              Character("Yanfei", "liyue", "Pyro", "Catalyst", 1.5),
              Character("Kazuha", "inazuma", "Anemo", "Sword", 1.6),
              Character("Ayaka", "inazuma", "Cryo", "Sword", 2.0),
              Character("Sayu", "inazuma", "Anemo", "Claymore", 2.0),
              Character("Yoimiya", "inazuma", "Pyro", "Bow", 2.0),
              Character("Aloy", "none", "Cryo", "Bow", 2.1),
              Character("Kujou Sara", "inazuma", "Electro", "Bow", 2.1),
              Character("Raiden Shogun", "inazuma", "Electro", "Polearm", 2.1),
              Character("Kokomi", "inazuma", "Hydro", "Catalyst", 2.1),
              Character("Thoma", "inazuma", "Pyro", "Polearm", 2.2),
              Character("Itto", "inazuma", "Geo", "Claymore", 2.3),
              Character("Gorou", "inazuma", "Geo", "Bow", 2.3),
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
              Character("Nilou", "sumeru", "Hydro", "Sword", 3.1),
              Character("Layla", "sumeru", "Cryo", "Sword", 3.2),
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
              Character("Xianyun", "liyue", "Anemo", "Catalyst", 4.4)}

# Character("Chiori", "liyue", "Geo", "Sword", 4.5)

pool = set()
eligible_regions = []
eligible_visions = []
eligible_weapons = []
eligible_versions = set()


def find_character(el_reg, el_vis, el_weap, el_ver, know_vision, know_region, know_weapon, know_version, character):
    t = screenshot(location)
    error1 = False
    error2 = False
    error3 = False
    if not know_region:
        know_region, el_reg, error1 = identify_region(character, t, el_reg, even_faster, elapsed_count)

    if not know_vision:
        know_vision, el_vis, error2 = identify_vision(character, t, el_vis, even_faster, elapsed_count)

    if not know_weapon:
        know_weapon, el_weap, error3 = identify_weapon(character, t, el_weap, even_faster, elapsed_count)

    if error1 or error2 or error3:
        return el_reg, el_vis, el_weap, el_ver, know_vision, know_region, know_weapon, know_version, True

    flag2 = False
    if not know_version:
        r, g, b = t.getpixel((915, 15))  # correct version
        for x in range(50):
            if flag2:
                break
            if (r, g, b) == (29, 145, 40):
                el_ver = {character.version}
                know_version = True
                break
            elif (r, g, b) == (126, 25, 25):
                if not even_faster:
                    log_incorrect_version(character, location)
                el_ver.remove(character.version)
                if character.name == "Wriothesley":
                    arrows_to_go_through = arrows_wrio
                else:
                    arrows_to_go_through = arrows
                for arrow in arrows_to_go_through:
                    try:
                        if (pyautogui.locateOnScreen(f".\\res\\{arrow_folder}\\{arrow}.png", region=arrow_location,
                                                     confidence=0.95) is not None):
                            el_ver = identify_arrow_type(character, arrow, even_faster, el_ver, arrow_location)
                            if len(el_ver) == 1:
                                know_version = True
                            flag2 = True
                            break
                    except ImageNotFoundException:
                        if not even_faster:
                            print(f"Couldn't locate {arrow}...")
                else:
                    print("THIS IS NOT GOOD. COULDN'T FIND ANY ARROWS")
                    didnt_find_any_arrows(character)
                    # this should NOT occur and if it does, the program will not work optimally.
                    # if you notice this, try replacing the arrows I provided with screenshots of your own arrows
                    # (take them at 100% window size, in fullscreen and the respective display scale)
                    # if that doesn't help recognize the arrows, I haven't found a fix yet unfortunately
                    break
            elif (r, g, b) == (9, 52, 76):
                return el_reg, el_vis, el_weap, el_ver, know_vision, know_region, know_weapon, know_version, True
            else:
                if not even_faster:
                    print("Too fast to identify version, waiting 0.005 seconds to try again")
                sleep(0.005)
                t = screenshot(location)
                t.save(f'.\\logs\\version_{elapsed_count % 10}.png')
                r, g, b = t.getpixel((915, 15))
        else:
            print(f"Version identification failed: ({r}, {g}, {b})")

    # print(el_reg, el_vis, el_weap, el_ver)
    if not even_faster:
        print("Possible versions:", el_ver)
    return el_reg, el_vis, el_weap, el_ver, know_vision, know_region, know_weapon, know_version, False


keyboard.press_and_release('alt+tab')
sleep(0.5)
keyboard.press_and_release('ctrl+0')
keyboard.press_and_release('up_arrow')

sleep(0.1)

if f11():
    keyboard.press_and_release('f11')

sleep(0.1)

pic = pyautogui.screenshot(region=(1100, 1, 2, 2))
r, g, b = pic.getpixel((1, 1))
scale125, location, arrows_wrio, arrow_folder, arrow_location, click_y = \
    check_for_125_scale(r, g, b, location, arrows_wrio, arrow_folder, arrow_location, click_y)

lost = False
quit = False
daily = False

elapsed_sum = 0.0
elapsed_count = 0
# for x in range(1000):
while not lost and not quit and not daily:
    start = time.perf_counter()
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

        if flag:
            try:
                writing, most_common_count, char = choose_character(pool)
            except ValueError:
                print("We fail", eligible_regions, eligible_visions, eligible_weapons, eligible_versions)
                quit = True
                break
        else:
            flag = True
            pool = characters.copy()
            eligible_regions = regions.copy()
            eligible_visions = visions.copy()
            eligible_weapons = weapons.copy()
            eligible_versions = versions.copy()
            writing, most_common_count, char = \
                "Qiqi", (20, 15, 17, 21), Character("Qiqi", "liyue", "Cryo", "Sword", 1.0)
        click(1000, click_y)
        click(1000, click_y)
        time.sleep(0.02)

        keyboard.write(writing)
        keyboard.press_and_release('enter')
        time.sleep(0.05)
        if daily:
            quit = stop(quit)
            if quit:
                break
        pic = pyautogui.screenshot(region=(550, 350, 2, 2))
        r, g, b = pic.getpixel((1, 1))
        if writing == "Qiqi" and win(scale125, r, g, b):
            sleep(0.01)
            pic = pyautogui.screenshot(region=(550, 350, 2, 2))
            r, g, b = pic.getpixel((1, 1))
        # print(r, g, b)
        if win(scale125, r, g, b):
            elapsed = write_logs(writing, daily, log, characters, even_faster, start)
            elapsed_sum += elapsed
            elapsed_count += 1
            break
        elif r >= 50:
            print(f"We lose. Pool: {[character.name for character in pool]}")
            lost = True
            break
        else:
            print(f"Guessing {writing}...", end='')
            print() if even_faster else print(f" {most_common_count}")
        time.sleep(0.1)
        quit = stop(quit)
        if quit:
            break
        time.sleep(0.33)

        quit = stop(quit)
        if quit:
            break

        if daily:
            print("Waiting for the cards to flip...")
            time.sleep(0.4)
            waiting()

        # print('Now!')

        eligible_regions, eligible_visions, eligible_weapons, eligible_versions, know_vision, know_region, know_weapon, know_version, that_error = \
            find_character(eligible_regions, eligible_visions, eligible_weapons, eligible_versions, know_vision,
                           know_region, know_weapon, know_version, char)
        # time.sleep(0.2)
        # print(eligible_visions)
        if that_error:
            pic = pyautogui.screenshot(region=(550, 350, 2, 2))
            r, g, b = pic.getpixel((1, 1))
            if win(scale125, r, g, b):
                elapsed = write_logs(writing, daily, log, characters, even_faster, start)
                elapsed_sum += elapsed
                elapsed_count += 1
                break
        else:
            pool = update_pool(pool, eligible_regions, eligible_visions, eligible_weapons, eligible_versions, writing)
            if not even_faster:
                print(f"{len(pool)} left in the pool\n")
            quit = stop(quit)
            if quit:
                break
    else:
        print(f"We do not win. Pool: {[character.name for character in pool]}")
        break
    if quit:
        break
    quit = stop(quit)
    if quit:
        break
    if not even_faster:
        sleep(1)
    quit = stop(quit)
    if quit:
        break
if not daily_mode and elapsed_count:
    print(f'\n--------------------------\n\n'
          f'Average time: {elapsed_sum / elapsed_count + bool(not even_faster):.6f} seconds')
    print(f'Characters guessed correctly: {elapsed_count}')
    print(f'Total characters guessed: {sum(log.values())}')
