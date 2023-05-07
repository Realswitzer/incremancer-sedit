#!/usr/bin/env python3

# pretend that theres a link to the license file. im too lazy.
# you will NOT import the entire python base installation modules
import argparse
import json
import os
import re
import operator

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
parser.add_argument(
    "-c", "--overwrite", action="store_true", help="confirm overwrite"
)  # not used, need to implement.
args = parser.parse_args()

# look for temp file and determine input file
if os.path.exists("temp.tmp"):
    howvarname = input("temp.tmp found. Would you like to load this instead? ").lower()
    if howvarname == "y" or howvarname == "yes":
        inputfile = "temp.tmp"
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
print(
    "Input file: "
    + inputfile
    + " | Output file: "
    + outputfile
    + " | Format: "
    + format
)
# manually delete useless variables
del format

# sort by id, should figure out better way of doing this.
jsondata["upgrades"].sort(key=operator.itemgetter("id"))
jsondata["constructions"].sort(key=operator.itemgetter("id"))

# terminal stuff
# possibly make longer prefixes?
# SHIPPING: Make sure this line is not commented out.
cmdprefix = ["/", "!", "#", ":"]
if str(cmdprefix) == "" or cmdprefix == [""]:
    print("cmdprefix variable is screwed up, using emergency prefix '!'")
    cmdprefix = "!"


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
    vvv = json.dumps(jsondata, separators=(",", ":"))
    # pyperclip.copy(vvv)
    # write to the files, and close them
    tempfile.write(vvv)
    file.write(LZString.compressToEncodedURIComponent(vvv))
    file.close()
    tempfile.close()


# for upg/const: set min and max boundaries to make it better. or something.
def check(x, min, max):
    x = int(x)
    if x < min:
        return min
    elif x > max:
        return max
    else:
        return x


def cmdupgrades(x):
    x = list(x.rpartition(" "))
    skip = False
    # finally use switch statements.
    # need to fix x[2] = 1 in case user is trying to lock it
    # should determine if 1 or greater, x[2]=1 else x[2]=0 and convert to function
    match re.compile("[^a-zA-Z ]").sub("", x[0].lower()):
        case "bloodthirst":
            listelement = 0
        case "like leather":
            listelement = 1
        case "cold storage":
            listelement = 2
        case "recycling is cool":
            listelement = 3
        case "your soul is mine":
            listelement = 4
        case "infected bite":
            listelement = 5
        case "detonate":
            listelement = 6
            # this can only be on or off, no point in having level 1000
            x[2] = check(x[2], 0, 1)
        case "gigazombies":
            listelement = 7
            x[2] = check(x[2], 0, 1)
        case "sharpened teeth":
            listelement = 8
        case "thick skull":
            listelement = 9
        case "razor claws":
            listelement = 10
        case "battle hardened":
            listelement = 11
        case "blazing speed":
            listelement = 12
        case "spit it out":
            listelement = 13
        case "runic syphon":
            listelement = 14
        case "killer instinct":
            listelement = 15
        case "tough as nails":
            listelement = 16
        case "faster harpies":
            listelement = 17
        case "energy rush":
            listelement = 18
            x[2] = check(x[2], 0, 1)
        case "master summoner":
            listelement = 19
        case "primal reflexes":
            listelement = 20
        case "blood harvest":
            listelement = 21
        case "unholy construction":
            listelement = 22
            x[2] = check(x[2], 0, 1)
        case "infected corpse":
            listelement = 23
        case "energy charge":
            listelement = 24
            x[2] = check(x[2], 0, 1)
        case "what doesnt kill you":
            listelement = 25
        case "one is never enough":
            listelement = 26
        case "tank buster":
            listelement = 27
            x[2] = check(x[2], 0, 1)
        case "improved spikes":
            listelement = 28
        case "bone throne":
            listelement = 29
        case "crown of bones":
            listelement = 30
        case "bonebarrows":
            listelement = 31
        case "bone reinforced tanks":
            listelement = 32
        case "brain cage":
            listelement = 33
        case "earth freeze":
            listelement = 34
            x[2] = check(x[2], 0, 1)
        case "plague armor":
            listelement = 35
        case "bulletproof":
            listelement = 36
        case "bombs away":
            listelement = 37
        case "extra limbs":
            listelement = 38
        case "big boned":
            listelement = 39
        case "blood storage":
            listelement = 40
        case "blood rate":
            listelement = 41
        case "brain storage":
            listelement = 42
        case "brain rate":
            listelement = 43
        case "bone rate":
            listelement = 44
        case "a small investment":
            listelement = 45
        case "time warp":
            listelement = 46
            x[2] = check(x[2], 0, 1)
        case "master of death":
            listelement = 47
        case "parts rate":
            listelement = 48
        case "auto construction":
            listelement = 49
            x[2] = check(x[2], 0, 1)
        case "graveyard health":
            listelement = 50
        case "auto shop":
            listelement = 51
            x[2] = check(x[2], 0, 1)
        case "talent point":
            listelement = 52
            x[2] = check(x[2], 0, 120)
        case _:
            skip = True
    if not skip == True:
        listelement = "[" + str(listelement) + "]"
        exec(
            'jsondata["upgrades"]' + listelement + '["rank"] = x[2]',
            globals(),
            locals(),
        )
        # show edited keys, esp. for concatenated commands.
        print(
            'Key edited / (["upgrades"]'
            + str(listelement)
            + '["rank"]) -> "'
            + str(x[2])
            + '"'
        )
    else:
        print("skipped")


def cmdconstructions(x):
    x = x.rsplit(" ", 2)
    listelement = -1
    match re.compile("[^a-zA-Z0-9 ]").sub("", x[0].lower()):
        case ("cursed graveyard" | "graveyard"):
            # how the hell do i do anything with check()?
            # maybe make new function to shorten this massively
            listelement = 0
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("perimeter fence" | "fence"):
            listelement = 1
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("bigger fence" | "fencesize"):
            listelement = 2
            x[1] = check(x[1], 0, 1)
        case ("plague workshop" | "plagueworkshop" | "workshop"):
            listelement = 3
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("crypt"):
            listelement = 4
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("bone fort" | "fort"):
            listelement = 5
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("bone fortress" | "fortress"):
            listelement = 6
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("plague spikes" | "plaguespikes" | "spikes"):
            listelement = 7
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("spell tower" | "spelltower"):
            listelement = 8
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("runesmith"):
            listelement = 9
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("bone citadel" | "citadel"):
            listelement = 10
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("accursed aviary" | "aviary"):
            listelement = 11
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("zombie cage" | "zombiecage" | "cage1" | "zombie cage 1" | "zombiecage1"):
            listelement = 12
            x[1] = check(x[1], 0, 1)
        case ("second zombie cage" | "zombiecage2" | "cage2" | "zombie cage 2"):
            listelement = 13
            x[1] = check(x[1], 0, 1)
        case ("third zombie cage" | "zombiecage3" | "cage3" | "zombie cage 3"):
            listelement = 14
            x[1] = check(x[1], 0, 1)
        case ("fourth zombie cage" | "zombiecage4" | "cage4" | "zombie cage 4"):
            listelement = 15
            x[1] = check(x[1], 0, 1)
        case ("fifth zombie cage" | "zombiecage5" | "cage5" | "zombie cage 5"):
            listelement = 16
            x[1] = check(x[1], 0, 1)
        case ("plague laboratory" | "plaguelaboratory" | "laboratory"):
            listelement = 17
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("part factory" | "partfactory"):
            listelement = 18
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("creature factory" | "creaturefactory"):
            listelement = 19
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
        case ("bottomless pit" | "pit"):
            listelement = 20
            x[1] = check(x[1], 0, 10)
            x[2] = check(x[2], 0, 1)
        case ("harpy outfitter" | "harpy" | "outfitter"):
            listelement = 21
            x[1] = check(x[1], 0, 1)
            x[2] = check(x[2], 0, 1)
    if not listelement == -1:
        listelement = "[" + str(listelement) + "]"
        exec(
            'jsondata["constructions"]' + listelement + '["rank"] = x[1]',
            globals(),
            locals(),
        )
        exec(
            'jsondata["constructions"]' + listelement + '["effect"] = x[2]',
            globals(),
            locals(),
        )
        # show edited keys, esp. for concatenated commands.
        print(
            'Key edited / (["constructions"]'
            + str(listelement)
            + '["rank"]) -> "'
            + str(x[1])
            + '"'
        )
        print(
            'Key edited / (["constructions"]'
            + str(listelement)
            + '["effect"]) -> "'
            + str(x[2])
            + '"'
        )
    else:
        print("skipped")


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
    cmds = [
        "help",
        "exit",
        "save",
        "saveas",
        "view",
        "dedupe",
        "upgrades",
        "constructions",
        "clear",
        "eval",
        "exec",
    ]
    cmdshelps = [
        "Prints list of editor commands",
        "Exits save editor",
        "Saves file",
        "Saves file as new file, changes output",
        "View value of key (@all shows all keys) <key,@all,key.nestkey>",
        "Deduplicate lists",
        "Edit upgrade values by name",
        "Edit constructions by name",
        "Clears screen",
        "Arbitrary code execution - evaluate expressions",
        "Arbitrary code execution - execute code. but with exec()",
    ]
    # now we just increment through everything and print the help message! easy!
    while x < len(cmds):
        print(str(cmdprefix[0]) + cmds[x] + " - " + cmdshelps[x])
        x += 1


def cmdview(x):
    # view key values. this is an actually useful command.
    # print name of every key in base
    if x == "@all":
        print(list(jsondata))
    elif x == "":
        print("invalid syntax")
    else:
        zzzparts = x.split(".")
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
            exec("print(jsondata" + zzy + ")")
        # if anything happens during this,
        except:
            print("something went wrong, probably misinput\nsowwy :3")


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
        if (
            input(
                "The eval command is a dangerous command, it is literally just arbitrary code execution. By typing '"
                + evalphrase
                + "', you will be able to execute arbitrary code. This is dangerous and not recommended. "
            )
            == evalphrase
        ):
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
        if (
            input(
                "The exec command is a dangerous command, it is literally just arbitrary code execution. By typing '"
                + evalphrase
                + "', you will be able to execute arbitrary code. This is dangerous and not recommended. "
            )
            == evalphrase
        ):
            evalagree = True
    if evalagree:
        exec(x, globals(), globals())


def cmddedupe(x):
    zzzparts = x.split(".")
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
    exec("jsondata" + zzy + " = zz")
    print("Deduped " + str(zzy))
    cmdview(x)


def cmdCheck(cmdinput):
    # remake as switch statement?
    # check command input.
    # insert some code that checks the command i guess
    # make this more efficient pls
    # try to split the command if it's not just one word.
    if " " in cmdinput:
        cmd = cmdinput.split(" ", 1)[0]
        rest = cmdinput.split(" ", 1)[1]
    else:
        cmd = cmdinput
        rest = ""
    # convert everything to a string. why? no idea.
    cmd = str(cmd)
    # alright now get ready for some yandev level shit, this is intense.
    # exit this bad program
    if cmd == "exit":
        # lol this doesnt work.
        if rest == "":
            cmdexit()
        else:
            cmdexit(rest)
    # stuff that uses "rest"
    # save this important file.
    elif cmd == "save":
        if rest == "":
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
    # prints help
    elif cmd == "help" or cmd == "?":
        cmdhelp()
    # deduplicate lists
    elif cmd == "dedupe" or cmd == "deduplicate":
        cmddedupe(rest)
    # upgrades thing
    elif cmd == "upgrades" or cmd == "upgrade" or cmd == "upg":
        cmdupgrades(rest)
    # edit constructions
    elif (
        cmd == "constructions"
        or cmd == "construction"
        or cmd == "construct"
        or cmd == "const"
    ):
        cmdconstructions(rest)
    # other
    elif cmd == "cls" or cmd == "clear":
        os.system("cls" if os.name == "nt" else "clear")
    elif cmd == ":3":
        # :3
        print(
            """
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
                    """
        )
    # and if nothing else catches input,
    else:
        print("Editor command not found.")


# prints different help, may make SETTINGS that will turn this off for people
# used to the weird way of save editing via cli
print(
    "hii use !help (default) to see list of commands.\nto edit values, do '[key] = [value]'\nto edit nested values do '[key.nestkey] = [value]'\nto create a list of all numbers between x and y do [x,...,y]\nfor every fifth one do [x,...,y,5]"
)


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
            if " = " in cmd:
                editkey = cmd.split(" = ", 1)[0]
                editval = cmd.split(" = ", 1)[1].strip()
                # determine mode
                mode = "set"
                # stop this from erroring.
                skip = False
            elif " += " in cmd:
                editkey = cmd.split(" += ", 1)[0]
                editval = cmd.split(" += ", 1)[1].strip()
                mode = "add"
                skip = False
            elif " -= " in cmd:
                editkey = cmd.split(" -= ", 1)[0]
                editval = cmd.split(" -= ", 1)[1].strip()
                mode = "sub"
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
            if re.search(r"\[\d*,...,\d*\]", editval) or re.search(
                r"\[\d*,...,\d*,\d*\]", editval
            ):
                # just to not deal with the brackets, cut them off.
                chucklenuts = editval[1:-1].split(",")
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
                    rangemin, rangemax + rangestep, rangestep
                ).tolist()
            # for accessing nested variables we split it inefficiently
            zzzparts = editkey.split(".")
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
            if mode == "set":
                pass
            elif mode == "add":
                try:
                    # halfassed solution.
                    # do not replicate this code
                    # i cant legally enforce this, it's just terrible.
                    try:
                        editval = int(editval)
                    except:
                        pass
                    whatdoinamethis = int
                    if isinstance(editval, int):
                        exec(
                            "whatdoinamethis = int(jsondata" + zzy + ")",
                            globals(),
                            globals(),
                        )
                        editval = whatdoinamethis + int(editval)
                    try:
                        editval = list(editval)
                    except:
                        pass
                    if isinstance(editval, list):
                        exec(
                            "whatdoinamethis = list(jsondata" + zzy + ")",
                            globals(),
                            globals(),
                        )
                        editval = whatdoinamethis + list(editval)
                    else:
                        print("sowwy list and numbews onwy 3:")
                except:
                    print("woopsies :3c")
            elif mode == "sub":
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
                        exec(
                            "whatdoinamethis = int(jsondata" + zzy + ")",
                            globals(),
                            globals(),
                        )
                        editval = whatdoinamethis - int(editval)
                    else:
                        print("sowwy numbews onwy 3:\n lists awe too hawd to wowk with")
                except:
                    print("woopsies :3c")
            exec("jsondata" + zzy + " = editval")
            # show edited keys, esp. for concatenated commands.
            print("Key edited / (" + zzy + ') -> "' + str(editval) + '"')
            # if anything happens during this,
            # except:
            #    print("something went wrong, probably misinput\nsowwy :3")


# create infinite terminal.
while True:
    # always ask for input
    cmd = input(" > ")
    if cmd == "":
        # if someone just hits enter
        pass
    # check for concatenated commands
    elif ";" in cmd:
        print("Running concatenated cmd")
        # treat each side of semicolons as an individual command
        cmds = cmd.split(";")
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
