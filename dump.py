#!/usr/bin/env python3

import lzstring
import argparse
import os
import json

# so i can do javascript feeling things, avoid "x.compressToEncodedURI('')"
# or "lzstring.LZString().compressToEncodedURI('')"
LZString = lzstring.LZString()

# get args
parser = argparse.ArgumentParser()
parser.add_argument(
    "mode", type=str, help="decode: sav -> json | encode: json -> sav")
parser.add_argument("input", type=str, help="input file location")
parser.add_argument("output", type=str, help="output file name")
parser.add_argument("-b", "--beautify", action='store_true',
                    help="beautify output (if decode)")
parser.add_argument("-c", "--overwrite", action='store_true',
                    help="Confirm overwrite")
args = parser.parse_args()

# parse args
if os.path.exists(args.input):
    file = open(args.input)
    file.close()
else:
    print("file does not exist, cannot proceed.")
    exit()

if '.' in args.output:  # check if output has file extension. if so, roll with it.
    output = args.output
elif args.mode == "decode":  # else automatically add appropriate file extension
    output = args.output + ".json"
elif args.mode == "encode":
    output = args.output + ".sav"

if not args.overwrite:
    if os.path.exists(output):
        if input("Output file already exists. Overwrite? (Yes/No) ").lower() == "yes" or "y":
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
    ok = json.dumps(ok, separators=(',', ':'))
    ok = LZString.compressToEncodedURIComponent(ok)
else:
    print("read the usage. <decode/encode>")
    exit()

file.close()
file2 = open(output, "w")
file2.write(ok)
print("File written")
