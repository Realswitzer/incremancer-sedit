#!/usr/bin/env python3
import os

protected_dirs = ['.git']
protected_files = ['.gitignore', 'clean.py', 'dump.py', 'id', 'LICENSE', 'readme.md', 'saveedit.py', 'TODO']
delfiles = []
files = os.walk(os.getcwd(), topdown=True)
for root, dirs, files in files:
    dirs[:] = [d for d in dirs if d not in protected_dirs]
    files[:] = [d for d in files if d not in protected_files]
    #print(root)
    #print(dirs)
    #print(files)
for file in files:
    if (os.path.getsize(file) == 0) or (file == 'temp.tmp'):
        os.remove(file)
        delfiles.append(file)

print("Deleted files:",delfiles)
