# Incremancer Save Editor
### i used python btw

# this does not work well
<p>it sorta works. to just decompress the save so you can see inside of it, use dump.py</p>

```
./dump.py decode input.sav output.json -b
notepad output.json
./dump.py encode output.json output.sav
```

# requirements
you need to install lzstring and fuckit.
lzstring -> decompress save file and compress it
fuckit -> try/except didnt work for eval and exec so...yeah.
pyperclip -> not used in final thing but used for debugging. i left the code in because im lazy so until the "final" release is made itll be listed.
```
pip install lzstring
pip install fuckit
```

### idk what to name this section
but anyways this entire thing wouldnt be possible without incremancer existing

[jamesmgittins/incremancer](https://github.com/jamesmgittins/incremancer)
<p style='font-size: 5px'>This does not use any code from incremancer, and also the original project seems to not be licensed. Hopefully this doesnt cause problems.</p>
and also [gkovacs/lz-string-python](https://github.com/gkovacs/lz-string-python) for the lzstring module in python.

# license
<p>licensed under gplv3 ♡</p>
<p style='font-size: 8px'>gplv3 my beloved</p>
