# Incremancer Save Editor

### i used python btw

<p>oh yeah i also made one of the worst code samples. feel free to use as an example of flat out terrible code.</p>

# this does not work well

<p>it sorta works. to just decompress the save so you can see inside of it, use dump.py</p>

```
./dump.py decode input.sav output.json -b
notepad output.json
./dump.py encode output.json output.sav
```

# heres a demo

https://user-images.githubusercontent.com/39711351/235377516-6963cf74-934e-4e8e-870a-0db6eeea0d47.mp4

# requirements

you need to install lzstring and fuckit.
<p>lzstring -> decompress save file and compress it</p>

<p>fuckit -> try/except didnt work for eval and exec so...yeah.</p>

<p>numpy -> idk handle [x,...,y]</p>

<p>pyperclip -> not used in final thing but used for debugging. i left the code in because im lazy so until the "final" release is made itll be listed.</p>

```
pip install lzstring
pip install fuckit
pip install numpy
```

### idk what to name this section
but anyways this entire thing wouldnt be possible without incremancer existing

[jamesmgittins/incremancer](https://github.com/jamesmgittins/incremancer)

<p style='font-size: 5px'>This does not use any code from incremancer, and also the original project seems to not be licensed. Hopefully this doesnt cause problems.</p>

and also [gkovacs/lz-string-python](https://github.com/gkovacs/lz-string-python) for the lzstring module in python.

# license

<p>licensed under gplv3 ♡</p>

<p style='font-size: 8px'>gplv3 my beloved</p>
