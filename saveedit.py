#!/usr/bin/env python3

import lzstring
import os
import time
import argparse
import json

LZString = lzstring.LZString()

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="save file")
parser.add_argument("-o", "--output", type=str, help="output file")
parser.add_argument("-c", "--overwrite", action='store_true',
                    help="confirm overwrite")
args = parser.parse_args()


if os.path.exists('temp.tmp'):
    if input("temp.tmp found. Would you like to load this instead? ").lower() == "y" or "yes":
        inputfile = 'temp.tmp'
else:
    inputfile = args.file

# determine file format
v = open(inputfile)
troll = v.read()
v.close()
del v
if troll[0] == "{":
    data = troll
    format = "json"
elif troll[0] == "N":
    data = LZString.decompressFromEncodedURIComponent(troll)
    format = "sav"
else:
    print("hey i think ur file sort of brokey.")
    exit()
del troll

if args.output == None:
    outputfile = args.file
else:
    outputfile = args.output

jsondata = json.loads(data)
print(jsondata)
print(type(jsondata))

print("Input file: " + inputfile + " | Output file: " +
      outputfile + " | Format: " + format)
# manually delete useless variables
del format

# terminal stuff
# possibly make longer prefixes? or lists of valid prefixes?
# cmdprefix = ["/", '!', '#', ':']
cmdprefix = ['']
if str(cmdprefix) == '' or cmdprefix == ['']:
    print("cmdprefix variable is screwed up, using emergency prefix '!'")
    cmdprefix = '!'


def cmdexit(shouldsave=True):
    if shouldsave:
        cmdsave()
    os.remove("temp.tmp")
    exit()


def cmdsave():
    file = open(outputfile, "w")
    tempfile = open("temp.tmp", "w")

    # tempfile.write(json.dumps(data, separators=(',', ':')))
    tempfile.write(json.dumps(json.loads(data), separators=(',', ':')))
    file.write(LZString.compressToEncodedURIComponent(
        json.dumps(json.loads(data), separators=(',', ':'))))
    file.close()
    tempfile.close()
    pass


currmenu = "term"


def cmdmenu(menu="main"):
    global currmenu
    print(menu)
    currmenu = menu
    if menu == "main":
        print("main menu")
    elif menu == "term":
        print("terminal")
    elif menu == "stats":
        print("stats menu")
    elif menu == "skeleton":
        print("skeleton menu")
    elif menu == "runesmith":
        print("runesmith menu")
    elif menu == "upgrades":
        print("upgrades menu")
    elif menu == "constructions":
        print("constructions menu")
    else:
        print("Menu not found")


def cmdprev():
    global currmenu
    print(currmenu)
    # optimization is cringe.
    if currmenu == "main":
        cmdmenu('term')
    elif currmenu in ['stats', 'skeleton', 'runesmith', 'upgrades', 'constructions']:
        cmdmenu('main')
    elif currmenu in ['blood_upg', 'brain_upg', 'part_upg', 'bone_upg', 'prestige_upg']:
        cmdmenu('upgrades')
    elif currmenu in ['items_skel', 'talents_skel', 'stats_skel']:
        cmdmenu('skeleton')


def cmdhelp():
    x = 0
    print("Valid prefixes: " + str(cmdprefix))
    cmds = ["help", "exit", "save", "saveas", "menu", "eval", "exec"]
    cmdshelps = ["Prints list of editor commands", "Exits save editor",
                 "Saves file", "Saves file as new file, changes output", "Opens different menus", "Arbitrary code execution - evaluate expressions", "Arbitrary code execution - execute code. but with exec()"]
    while x < len(cmds):
        print(str(cmdprefix[0]) + cmds[x] + " - " + cmdshelps[x])
        x += 1


evalagree = False
evalphrase = "This is a terrible practice and should not be used in the slightest"
# evalphrase = "ok trust me bro"


def cmdeval(x):
    global evalagree
    global evalphrase
    if evalagree == False:
        if input("The eval command is a dangerous command, it is literally just arbitrary code execution. By typing '" + evalphrase + "', you will be able to execute arbitrary code. This is dangerous and not recommended. ") == evalphrase:
            evalagree = True
    if evalagree:
        eval(x)


def cmdexec(x):
    global evalagree
    global evalphrase
    if evalagree == False:
        if input("The exec command is a dangerous command, it is literally just arbitrary code execution. By typing '" + evalphrase + "', you will be able to execute arbitrary code. This is dangerous and not recommended. ") == evalphrase:
            evalagree = True
    if evalagree:
        exec(x)


def cmdCheck(cmdinput):
    # insert some code that checks the command i guess
    # make this more efficient pls
    if ' ' in cmdinput:
        cmd = cmdinput.split(' ', 1)[0]
        rest = cmdinput.split(' ', 1)[1]
    else:
        cmd = cmdinput
        rest = ''
    cmd = str(cmd)
    if cmd == "exit":
        cmdexit()
    elif cmd == "prev" or cmd == "back":
        # return to prev menu
        cmdprev()
        pass
    # stuff that uses "rest"
    elif cmd == "menu":
        if rest == '':
            cmdmenu()
        else:
            cmdmenu(rest)
    elif cmd == "save":
        if rest == '':
            cmdsave()
        else:
            cmdsave(rest)
    elif cmd == "eval":
        cmdeval(rest)
    elif cmd == "exec":
        cmdexec(rest)
    # aliases
    elif cmd == "stats":
        cmdmenu("stats")
    elif cmd == "help" or cmd == "?":
        cmdhelp()
    else:
        print("Editor command not found.")


while True:
    cmd = input(" > ")
    if cmd[0] in cmdprefix:
        cmdCheck(cmd[1:])
    else:
        # edit save/interact with menu
        pass
