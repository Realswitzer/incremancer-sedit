#!/usr/bin/env python3
import os

protected_dirs = ['.git','.venv','.vscode']
protected_files = ['.gitignore', 'clean.py', 'dump.py', 'id', 'LICENSE', 'readme.md', 'saveedit.py', 'TODO']
x = input("1. empty files and temp.tmp\n2. all sav/json files\n3. both\n4. exit\n")
try:
    x = int(x)
except:
    print("not int, exiting")
    exit()
if x == 4:
    exit()
elif x not in [1,2,3]:
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
    #print(root)
    #print(dirs)
    #print(files)
for file in files:
    if x == 1:
        if (os.path.getsize(file) == 0) or (file == 'temp.tmp'):
            delfile(file)
    if x == 2:
        if (file.endswith('.sav')) or (file.endswith('.json')):
            delfile(file)
    if x == 3:
        # not the most optimized though
        if (os.path.getsize(file) == 0) or (file == 'temp.tmp') or (file.endswith('.sav')) or (file.endswith('.json')):
            delfile(file)

print("Deleted files:",delfiles)
