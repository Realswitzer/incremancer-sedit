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

import lzstring
import argparse
import os
import json

print("Hi, I feel under GPLv3 licensing, I should put this here.\nThis program does not have any warranty, no implied warranty, and I am legally not held responsible for any damages.")

# so i can do javascript feeling things, avoid "x.compressToEncodedURI('')"
# or "lzstring.LZString().compressToEncodedURI('')"
LZString = lzstring.LZString()

# get args
parser = argparse.ArgumentParser()
parser.add_argument("mode", type=str, help="decode: sav -> json | encode: json -> sav")
parser.add_argument("input", type=str, help="input file location")
parser.add_argument("output", type=str, help="output file name")
parser.add_argument(
    "-b", "--beautify", action="store_true", help="beautify output (if decode)"
)
parser.add_argument("-c", "--overwrite", action="store_true", help="Confirm overwrite")
args = parser.parse_args()

# parse args
if os.path.exists(args.input):
    file = open(args.input)
    file.close()
else:
    print("file does not exist, cannot proceed.")
    exit()

if "." in args.output:  # check if output has file extension. if so, roll with it.
    output = args.output
elif args.mode == "decode":  # else automatically add appropriate file extension
    output = args.output + ".json"
elif args.mode == "encode":
    output = args.output + ".sav"

if not args.overwrite:
    if os.path.exists(output):
        if (
            input("Output file already exists. Overwrite? (Yes/No) ").lower() == "yes"
            or "y"
        ):
            os.remove(output)
        else:
            print("Exiting.")
            exit()

file = open(args.input)
if args.mode == "decode":
    print("Decoding file")
    try:
        ok = LZString.decompressFromEncodedURIComponent(file.read())
        if args.beautify:
            ok = json.loads(ok)
            ok = json.dumps(ok, indent=2)
    except:
        print("invalid file, please make sure you used a save file and not a json file")
        exit()
elif args.mode == "encode":
    print("Encoding file")
    ok = file.read()
    ok = json.loads(ok)
    ok = json.dumps(ok, separators=(",", ":"))
    ok = LZString.compressToEncodedURIComponent(ok)
else:
    print("read the usage. <decode/encode>")
    exit()

file.close()
file2 = open(output, "w")
file2.write(ok)
print("File written")
