#!/usr/bin/env python3
# incremancer-sedit: A save editor for Incremancer
# Copyright (C) 2023  Realswitzer/Switz

# This file is part of incremancer-sedit.
#
# incremancer-sedit is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# incremancer-sedit is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Foobar. If not, see <https://www.gnu.org/licenses/>. 
import os

print("Hi, I feel under GPLv3 licensing, I should put this here.\nThis program does not have any warranty, no implied warranty, and I am legally not held responsible for any damages.")
protected_dirs = [".git", ".venv", ".vscode", "presets", "chalice"]
protected_files = [
    ".gitignore",
    "clean.py",
    "dump.py",
    "id",
    "LICENSE",
    "readme.md",
    "saveedit.py",
    "TODO",
    "sedit.cfg"
]
x = input("1. empty files and temp.tmp\n2. all sav/json files\n3. both\n4. exit\n")
try:
    x = int(x)
except:
    print("not int, exiting")
    exit()
if x == 4:
    exit()
elif x not in [1, 2, 3]:
    print("invalid int")
    exit()

delfiles = []


def delfile(file):
    os.remove(file)
    delfiles.append(file)


files = os.walk(os.getcwd(), topdown=True)
for root, dirs, files in files:
    dirs[:] = [d for d in dirs if d not in protected_dirs]
    files[:] = [d for d in files if d not in protected_files]
    # print(root)
    # print(dirs)
    # print(files)
for file in files:
    if x == 1:
        if (os.path.getsize(file) == 0) or (file == "temp.tmp"):
            delfile(file)
    if x == 2:
        if (file.endswith(".sav")) or (file.endswith(".json")):
            delfile(file)
    if x == 3:
        # not the most optimized though
        if (
            (os.path.getsize(file) == 0)
            or (file == "temp.tmp")
            or (file.endswith(".sav"))
            or (file.endswith(".json"))
        ):
            delfile(file)

print("Deleted files:", delfiles)
