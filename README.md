# Easy datamoshing with Python!

This is a command line interface to make datamoshing easy and accesible to everyone!

**If you are using vscode and the file won't play, try playing it outside of vscode!**

This repo is built off of tiberiuiancu/datamosher and itsKaspar/tomato, so thanks for the awesome code!

## Quick start!

Make sure you have downloaded all the requirements!

Run `pip install -r requirements.txt`

`mosh.py` requires `ffmpeg` to be installed.

`vector_motion.py` and `style_transfer.py` depend on `ffedit` and `ffgac`, which can be downloaded from [ffglitch.org](https://ffglitch.org/)

**Don't forget to add those 3 files to your path!**

Then all thats left is to run main.py!

# Effects you can achieve

## i-frame removal
This type of glitch creates the transition effect. Example:

| Original | Moshed |
|:--------:|:------:|
| ![original_hand](https://user-images.githubusercontent.com/31802439/112060042-f3e42780-8b5c-11eb-8019-df4d06dd0d31.gif) | ![moshed_hand](https://user-images.githubusercontent.com/31802439/112060033-f181cd80-8b5c-11eb-9025-65064bbc6200.gif) |

    $ python mosh.py input.mp4 -s 40 -e 90 -o output.mp4
removes all the i-frames from the input video starting at frame 40 and ending at frame 90, and outputs the final result
to `output.mp4`

## p-frame duplication
Repeats a series of p-frames (aka delta frames), which can give a 'melting' effect. This type of glitch is triggered by the `-d` flag. Example:

| Original | Moshed |
|:--------:|:------:|
| ![original_dog](https://user-images.githubusercontent.com/31802439/112059335-0316a580-8b5c-11eb-98c8-3493969dd472.gif) | ![moshed_dog](https://user-images.githubusercontent.com/31802439/112060106-065e6100-8b5d-11eb-9670-4ad3bd9522cd.gif) |

    $ python mosh.py dog.mp4 -d 5 -s 165 -o moshed_dog.mp4

copies 5 frames starting at frame 165, then replaces all subsequent groups of 5 frames with the copied data (in this case until the video ends, as no `-e` flag was specified).

## Vector motion
While the previous effects copy and delete whole frames, this one changes the actual frame data. As explained in
[this article on ffglitch.org](https://ffglitch.org/2020/07/mv.html), you need to write a custom JavaScript file
that can change the frame data. `vector_motion.py` is just a wrapper for `ffedit` and `ffgac` and makes moshing
possible through only one command.
Example:

    $ python vector_motion.py input.mp4 -s your_script.js -o output.mp4

**WARNING** No matter what name the output file has, it will always be of type mpg (and because we glitched it, video players
will probably have trouble reading its length). To convert it to mp4, you can use `ffmpeg`:

    $ ffmpeg -i input.mpg output.mp4

It will complain about corrupt p-frame data, but the result should look the same as in the mpg.

## Vector motion with Python

If you prefer to use python to glitch the frames, you can specify a python script for the `-s` argument (see previous section for usage).
The script must contain a function called `mosh_frames` that takes as argument an array of frames (warning: some of the frames
might be empty), where each non-empty frame represents a 3D array of shape (height, width, 2). The function should
return an array of the same shape, representing the modified vectors. For reference, I have included two examples:

`horizontal_motion_example.py` contains the equivalent python code of the js script from this 
[ffglitch tutorial](https://ffglitch.org/2020/07/mv.html).

`average_motion_example.py` is the equivalent of [ffglitch average motion tutorial](https://ffglitch.org/2020/07/mv_avg.html)
using numpy. Neat!


## Style transfer

This means combining the motion vectors of two videos, by simply adding them together (see example below). Note that if the videos do not have the same resolution (and framerate), the results might not look as desired.

Examples:

    $ python style_transfer.py -e clouds.mp4 -t trees.mp4 output.mp4

extracts vector data from `clouds.mp4`, transfers it to `trees.mp4` and outputs the video to `output.mp4`.

| Extract style from | Transfer style to | Result |
|:------------------:|:-----------------:|:------:|
| ![clouds](https://user-images.githubusercontent.com/31802439/112489124-70a21c00-8d7e-11eb-8640-6817a46602ca.gif) | ![trees](https://user-images.githubusercontent.com/31802439/112489146-74ce3980-8d7e-11eb-9091-999fbb98552c.gif) | ![ct](https://user-images.githubusercontent.com/31802439/112489221-86afdc80-8d7e-11eb-9a51-14d91ec7cdfa.gif) |


## Applying vector data manually

You can also apply already extracted vector motion data, similar to ffglitch:

    $ python style_transfer.py -e clouds.mp4 vectors.json

extracts the vector data from `clouds.mp4` and outputs it to `vectors.json`.

    $ python style_transfer.py -v vectors.json -t trees.mp4 output.mp4

loads vector data from `vectors.json`, transfers it to `trees.mp4` and outputs the video to `output.mp4`.

# tomato

**tomato** is a python script to glitch AVI files 
- utilities inspired by [Way Spurr-Chen](https://github.com/wayspurrchen)'s [moshy](https://github.com/wayspurrchen/moshy). 
- functionality based off of [Tomasz Sulej](https://github.com/tsulej)'s research on AVI file structure.

It was designed to operate video frame ordering, substraction and duplication.

Modes called through -mode [mode]

- `void` - does nothing
- `random` - randomizes frame order
- `reverse` - reverse frame order
- `invert` - switches each consecutive frame witch each other
- `bloom` - duplicates `c` times p-frame number `n`
- `pulse` - duplicates groups of `c` p-frames every `n` frames
- `overlap` - copy group of `c` frames taken from every `n`th position
- `jiggle` - take frame from around current position. `n` parameter is spread size [broken]

Other parameters :

- `-c and -n` - reserved for the modes
- `-ff [0 or 1]` - ignore first frame (default 1)
- `-a [0 or 1]` - activate audio (default 0)
- `-k [0 to 1]` - kill frames with too much data (default 0.7)

## Examples of usage

Takes out iframes:
>python tomato.py -i input.avi

Duplicate 50 times the 100th frame:
>python tomato.py -i input.avi -m bloom -c 50 -n 100 

Duplicates 5 times a frame every 10 frame:
>python tomato.py -i input.avi -m pulse -c 5 -n 10

Shuffles all of the frames in the video:
>python tomato.py -i input.avi -m random

Copy 4 frames taken starting from every 2nd frame. [1 2 3 4 3 4 5 6 5 6 7 8 7 8...]:
>python tomato.py -i input.avi -m overlap -c 4 -n 2


## Why tomato ?

I made tomato because I wanted to be able to glitch avi files regardless of the contained codec, the resolution and the file size while still being super duper fast and not needing to encode anything.

## How does it work ?

It reorders the frames inside the movi tag of your AVI file.

## How should you use it

Libraries used : numpy, argparse, os, re, random, struct, itertools

I recommend preparing your AVI files with ffmpeg and the codec library of your choice. To read your glitched files I recommend VLC or Xine if you're under Linux. Both are great for visualizing content (especially xine for the random mode) but keep in mind you should always be experimenting and using different visualizers or tools to bake your files.

If you have any questions or ideas feel free to send me an email at kaspar.ravel@gmail.com

For more info on development : https://www.kaspar.wtf/blog/tomato-v2-0-avi-breaker
