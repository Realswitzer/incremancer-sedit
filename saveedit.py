#!/usr/bin/env python3

# pretend that theres a link to the license file. im too lazy.
# you will NOT import the entire python base installation modules
import argparse
import json
import os
import time
import re
# import code

import fuckit  # this is bad practice.
import lzstring
import numpy

# SHIPPING: REMOVE THIS
# import pyperclip

# be able to call LZString.func() rather than lzstring.LZString().func().
LZString = lzstring.LZString()

# create argument parser to screw over people who dont know how to use cmd prompt
parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="save file")
parser.add_argument("-o", "--output", type=str, help="output file")
parser.add_argument("-c", "--overwrite", action='store_true',
                    help="confirm overwrite")
args = parser.parse_args()

# look for temp file and determine input file
if os.path.exists('temp.tmp'):
    howvarname = input(
        "temp.tmp found. Would you like to load this instead? ").lower()
    if howvarname == "y" or howvarname == "yes":
        inputfile = 'temp.tmp'
    else:
        inputfile = args.file
else:
    inputfile = args.file

# determine file format
v = open(inputfile)
troll = v.read()
v.close()
del v
# look for json format
if troll[0] == "{":
    data = troll
    format = "json"
# first character in an encodeduricomponent is N if the first character is {
# because science?
elif troll[0] == "N":
    data = LZString.decompressFromEncodedURIComponent(troll)
    format = "sav"
# otherwise its in some format that i refuse to work with.
else:
    print("hey i think ur file sort of brokey.")
    exit()
del troll

# check if output was specified
if args.output == None:
    outputfile = args.file
else:
    outputfile = args.output

# load the json data
jsondata = json.loads(data)

# print info
print("Input file: " + inputfile + " | Output file: " +
      outputfile + " | Format: " + format)
# manually delete useless variables
del format

# this extracts a list of keys from the json.
# you may be looking at this and ask,
# "but wait, why do you use this? doesnt this hardcode the values in cmdview
# and couldn't you just replace it with list(jsondata) when not specified?
# also doesn't this not even get used when checking if a key exists?"
# well, yes. i should replace it but this is not made to be efficient.
jsonkeys = list(jsondata)

# terminal stuff
# possibly make longer prefixes?
# SHIPPING: Make sure this line is not commented out.
cmdprefix = ["/", '!', '#', ':']
if str(cmdprefix) == '' or cmdprefix == ['']:
    print("cmdprefix variable is screwed up, using emergency prefix '!'")
    cmdprefix = '!'


def cmdexit(shouldsave=True):
    # save and exit, deleting temp.tmp. much more graceful than ctrl+c.
    # uh this doesnt work it literally just saves anyways. sorry.
    if shouldsave:
        # just call the save command real quick
        cmdsave()
    # get rid of the temp file that doesn't have much point.
    os.remove("temp.tmp")
    exit()


def cmdsave():
    # the actual save part
    # now jsondata needs to be accessible in this function
    global jsondata
    # pretty much just open the files to write to
    file = open(outputfile, "w")
    tempfile = open("temp.tmp", "w")
    # SHIPPING: remove pyperclip.
    # pyperclip.copy(json.dumps(jsondata))
    # dump the data in a single line as it matters
    vvv = json.dumps(jsondata, separators=(',', ':'))
    # pyperclip.copy(vvv)
    # write to the files, and close them
    tempfile.write(vvv)
    file.write(LZString.compressToEncodedURIComponent(vvv))
    file.close()
    tempfile.close()


# honestly none of this even does anything.
currmenu = "term"


def cmdmenu(menu="main"):
    # so the current menu needs to be accessible.
    global currmenu
    # some debug code i forgot to delete
    print(menu)
    # should set to menu _after_ i check. but this doesnt work.
    # stop crying about it i guess.
    currmenu = menu
    print("this doesnt really work sorry.")
    # if menu == "main":
    #     print("main menu")
    # elif menu == "term":
    #     print("terminal")
    # elif menu == "stats":
    #     print("stats menu")
    # elif menu == "skeleton":
    #     print("skeleton menu")
    # elif menu == "runesmith":
    #     print("runesmith menu")
    # elif menu == "upgrades":
    #     print("upgrades menu")
    # elif menu == "constructions":
    #     print("constructions menu")
    # else:
    #     print("Menu not found")


def cmdprev():
    # now this would make sense if the above function worked.
    # it doesn't.
    # get the current menu
    global currmenu
    # more debug code.
    print(currmenu)
    # optimization is cringe.
    # given the bug in the cmdmenu which sets before checking, this could make
    # this not work as intended.
    if currmenu == "main":
        cmdmenu('term')
    elif currmenu in ['stats', 'skeleton', 'runesmith', 'upgrades', 'constructions']:
        cmdmenu('main')
    elif currmenu in ['blood_upg', 'brain_upg', 'part_upg', 'bone_upg', 'prestige_upg']:
        cmdmenu('upgrades')
    elif currmenu in ['items_skel', 'talents_skel', 'stats_skel']:
        cmdmenu('skeleton')


def cmdhelp():
    # create incrementing variable
    x = 0
    # get list of prefixes
    print("Valid prefixes: " + str(cmdprefix))
    # now, you may look at this and say
    # "hey", as you look on with uncertainty.
    # "what is even happening."
    # now this does require manual updating, is outdated, and if you get
    # anything in the wrong order then all of the help texts for each cmd
    # is out of order.
    cmds = ["help", "exit", "save", "saveas", "menu", "view", "eval", "exec"]
    cmdshelps = ["Prints list of editor commands", "Exits save editor",
                 "Saves file", "Saves file as new file, changes output", "Opens different menus", "View value of key (@all shows all keys) <key,@all,key.nestkey>", "Arbitrary code execution - evaluate expressions", "Arbitrary code execution - execute code. but with exec()"]
    # now we just increment through everything and print the help message! easy!
    while x < len(cmds):
        print(str(cmdprefix[0]) + cmds[x] + " - " + cmdshelps[x])
        x += 1


def cmdview(x):
    # view key values. this is an actually useful command.
    # print name of every key in base
    if x == "@all":
        print(jsonkeys)
    elif x == '':
        print("invalid syntax")
    else:
        zzzparts = x.split('.')
        # make/clear incrementing variable
        inc = 0
        # assign blank string
        zzy = ""
        # if x = 'skeleton.xpRate';
        # zzzparts = ['skeleton','xpRate'];
        # zzy = "['skeleton']['xpRate']"
        # now just increment through to get a large string.
        while inc < len(zzzparts):
            try:
                # handle editing json list elements.
                zzzpart = int(zzzparts[inc])
            except:
                # if its not an integer, its a string.
                zzzpart = str(zzzparts[inc])
            zzy = zzy + str([zzzpart])
            inc += 1
        # try to edit variable if it exists. just using tryexcept to lazily
        # catch errors and stop the program from exiting unexpectedly
        try:
            # use exec because i dont know any workarounds.
            exec('print(jsondata' + zzy + ')')
        # if anything happens during this,
        except:
            print("something went wrong, probably misinput\nsowwy :3")


# to gatekeep using eval and exec, even though from the user perspective
# they basically do nothing of value, just have them type a long ass phrase
# every time they start the program!
# hell, this is so secure you can't even set variables. debugging this was ass.
# may turn this into a settings file so you dont have to type
# 'ok trust me bro' every single time.
evalagree = False
# evalphrase = "This is a terrible practice and should not be used in the slightest" # SHIPPING: Make sure this line is not commented out.
evalphrase = "ok trust me bro"


@fuckit  # ooh spooky bad practice
# now just throw input in eval command. got it? good.
def cmdeval(x):
    global evalagree
    global evalphrase
    if evalagree == False:
        if input("The eval command is a dangerous command, it is literally just arbitrary code execution. By typing '" + evalphrase + "', you will be able to execute arbitrary code. This is dangerous and not recommended. ") == evalphrase:
            evalagree = True
    if evalagree:
        eval(x, globals(), globals())


# wait this does basically the same thing but with exec.
# now i know if you look at previous versions,
# i had comments saying you couldn't set variables.
# turns out i was wrong. just needed to pass globals.
@fuckit
def cmdexec(x):
    global evalagree
    global evalphrase
    if evalagree == False:
        if input("The exec command is a dangerous command, it is literally just arbitrary code execution. By typing '" + evalphrase + "', you will be able to execute arbitrary code. This is dangerous and not recommended. ") == evalphrase:
            evalagree = True
    if evalagree:
        exec(x, globals(), globals())

# now this was going to just throw people into an interactive shell, like if
# you typed 'python3'. that didn't work.
# @fuckit
# def cmdinteractiveinterpreter():
#     code.InteractiveInterpreter(locals=locals())


def cmddedupe(x):
    zzzparts = x.split('.')
    # make/clear incrementing variable
    inc = 0
    # assign blank string
    zzy = ""
    # if editkey = 'skeleton.xpRate';
    # zzzparts = ['skeleton','xpRate'];
    # zzy = "['skeleton']['xpRate']"
    # now just increment through to get a large string.
    while inc < len(zzzparts):
        try:
            zzzpart = int(zzzparts[inc])
        except:
            zzzpart = str(zzzparts[inc])
        zzy = zzy + str([zzzpart])
        inc += 1
    exec("zz = list(dict.fromkeys(jsondata" + zzy + "))", globals(), globals())
    exec('jsondata' + zzy + ' = zz')
    print("Deduped " + str(zzy))
    cmdview(x)


def cmdCheck(cmdinput):
    # check command input.
    # insert some code that checks the command i guess
    # make this more efficient pls
    # try to split the command if it's not just one word.
    if ' ' in cmdinput:
        cmd = cmdinput.split(' ', 1)[0]
        rest = cmdinput.split(' ', 1)[1]
    else:
        cmd = cmdinput
        rest = ''
    # convert everything to a string. why? no idea.
    cmd = str(cmd)
    # alright now get ready for some yandev level shit, this is intense.
    # exit this bad program
    if cmd == "exit":
        # lol this doesnt work.
        if rest == '':
            cmdexit()
        else:
            cmdexit(rest)
    # return to prev menu
    elif cmd == "prev" or cmd == "back":
        cmdprev()
    # again interactive shell didn't work.
    # elif cmd == "ii":
    #     cmdinteractiveinterpreter()
    # stuff that uses "rest"
    # this command is basically useless.
    elif cmd == "menu":
        if rest == '':
            cmdmenu()
        else:
            cmdmenu(rest)
    # save this important file.
    elif cmd == "save":
        if rest == '':
            cmdsave()
        else:
            cmdsave(rest)
    # eval command
    elif cmd == "eval":
        cmdeval(rest)
    # exec command
    elif cmd == "exec":
        cmdexec(rest)
    # view command
    elif cmd == "view":
        cmdview(rest)
    # aliases
    # stats does nothing.
    elif cmd == "stats":
        cmdmenu("stats")
    # why did i put this under aliases?
    # prints help
    elif cmd == "help" or cmd == "?":
        cmdhelp()
    # deduplicate lists
    elif cmd == "dedupe" or cmd == "deduplicate":
        cmddedupe(rest)
    # other
    elif cmd == ":3":
        # :3
        print('''
                   ██████████▄
          ████     ████████████
          ████              ████
          ████                ██
                          █████▀
                    ▄▄███████
                    ▀▀█████████▄
          ████              ████
          ████               ███
          ████          ▄██████▀
                    █████████▀
                    █████▀
                    ''')
    # and if nothing else catches input,
    else:
        print("Editor command not found.")


# prints different help, may make SETTINGS that will turn this off for people
# used to the weird way of save editing via cli
print(
    "hii use !help (default) to see list of commands.\nto edit values, do '[key] = [value]'\nto edit nested values do '[key.nestkey] = [value]'\nto create a list of all numbers between x and y do [x,...,y]\nfor every fifth one do [x,...,y,5]")


def parseCmd(cmd):
    # parses the input
    # check if it seems to be an editor command
    if cmd[0] in cmdprefix:
        cmdCheck(cmd[1:])
    # if no pretend it's trying to edit.
    else:
        # check if we can split an atom.
        try:
            # split at equal sign
            # editkey - key to be edited
            # editval - value to be assigned
            # should figure out more efficient method to do all of this.
            if ' = ' in cmd:
                editkey = cmd.split(' = ', 1)[0]
                editval = cmd.split(' = ', 1)[1].strip()
                # determine mode
                mode = 'set'
                # stop this from erroring.
                skip = False
            elif ' += ' in cmd:
                editkey = cmd.split(' += ', 1)[0]
                editval = cmd.split(' += ', 1)[1].strip()
                mode = 'add'
                skip = False
            elif ' -= ' in cmd:
                editkey = cmd.split(' -= ', 1)[0]
                editval = cmd.split(' -= ', 1)[1].strip()
                mode = 'sub'
                skip = False
            else:
                # if someone just types a random character then skip processing
                skip = True
        # if we realize splitting atoms is just stupid,
        except:
            print("editval not found")
        # just skip to prevent exiting.
        if skip:
            pass
        else:
            # now we check if its a list
            if re.search(r"\[\d*,...,\d*\]", editval) or re.search(r"\[\d*,...,\d*,\d*\]", editval):
                # just to not deal with the brackets, cut them off.
                chucklenuts = editval[1:-1].split(',')
                if len(chucklenuts) == 3:
                    # [x,...,y]
                    # step is implied
                    rangestep = 1
                    # x = min
                    rangemin = int(chucklenuts[0])
                    # y = max
                    rangemax = int(chucklenuts[2])
                elif len(chucklenuts) == 4:
                    # [x,...,y,z]
                    # z = step
                    rangestep = int(chucklenuts[3])
                    # x = min
                    rangemin = int(chucklenuts[0])
                    # y = max
                    rangemax = int(chucklenuts[2])
                else:
                    # dont know how this would get triggered but if something really bad happens...
                    print("probably did something wrong because it no workey. :3c")
                # not turn everything into a fun list!
                editval = numpy.arange(
                    rangemin, rangemax + rangestep, rangestep).tolist()
            # for accessing nested variables we split it inefficiently
            zzzparts = editkey.split('.')
            # make/clear incrementing variable
            inc = 0
            # assign blank string
            zzy = ""
            # if editkey = 'skeleton.xpRate';
            # zzzparts = ['skeleton','xpRate'];
            # zzy = "['skeleton']['xpRate']"
            # now just increment through to get a large string.
            while inc < len(zzzparts):
                try:
                    zzzpart = int(zzzparts[inc])
                except:
                    zzzpart = str(zzzparts[inc])
                zzy = zzy + str([zzzpart])
                inc += 1
            # try to edit variable if it exists. just using tryexcept to lazily
            # catch errors and stop the program from exiting unexpectedly
            # try:
                # use exec because i dont know any workarounds.
            if mode == 'set':
                pass
            elif mode == 'add':
                try:
                    # halfassed solution.
                    # do not replicate this code
                    # i cant legally enforce this, it's just terrible.
                    try:
                        editval = int(editval)
                    except:
                        pass
                    if isinstance(editval, int):
                        exec('whatdoinamethis = int(jsondata' + zzy + ')',
                             globals(), globals())
                        editval = whatdoinamethis + int(editval)
                    try:
                        editval = list(editval)
                    except:
                        pass
                    if isinstance(editval, list):
                        exec('whatdoinamethis = list(jsondata' +
                             zzy + ')', globals(), globals())
                        editval = whatdoinamethis + list(editval)
                    else:
                        print("sowwy list and numbews onwy 3:")
                except:
                    print("woopsies :3c")
            elif mode == 'sub':
                # again, this is really horrible copy and pasted code.
                try:
                    # halfassed solution.
                    # do not replicate this code
                    # i cant legally enforce this, it's just terrible.
                    try:
                        editval = int(editval)
                    except:
                        pass
                    if isinstance(editval, int):
                        exec('whatdoinamethis = int(jsondata' + zzy + ')',
                             globals(), globals())
                        editval = whatdoinamethis - int(editval)
                    else:
                        print(
                            "sowwy numbews onwy 3:\n lists awe too hawd to wowk with")
                except:
                    print("woopsies :3c")
            exec('jsondata' + zzy + ' = editval')
            # show edited keys, esp. for concatenated commands.
            print("Key edited / (" + zzy + ") -> \"" + str(editval) + "\"")
            # if anything happens during this,
            # except:
            #    print("something went wrong, probably misinput\nsowwy :3")


# create infinite terminal.
while True:
    # always ask for input
    cmd = input(" > ")
    if cmd == '':
        # if someone just hits enter
        pass
    # check for concatenated commands
    elif ';' in cmd:
        print("Running concatenated cmd")
        # treat each side of semicolons as an individual command
        cmds = cmd.split(';')
        # help javascript users not break everything when ending with semicolon
        cmds = list(filter(None, cmds))
        # incrementing variable
        inc = 0
        # parse each command seperately
        while inc < len(cmds):
            parseCmd(cmds[inc].strip())
            inc += 1
    # otherwise bypass this entire mess.
    else:
        parseCmd(cmd)
