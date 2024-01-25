# Easy datamoshing with Python!

This is a command line interface to make datamoshing easy and accesible to everyone!

This repo is built off of tiberiuiancu/datamoshing and itsKaspar/tomato, so thanks for the awesome code!

![Command Line Interface](https://i.imgur.com/d14DQcY.png)

## Quick start!

Make sure you have downloaded all the requirements!

Run `pip install -r requirements.txt`

`mosh.py` requires `ffmpeg` to be installed.

`vector_motion.py` and `style_transfer.py` depend on `ffedit` and `ffgac`, which can be downloaded from [ffglitch.org](https://ffglitch.org/)

**Don't forget to add those 3 files to your path!**

**If you are using vscode and the file won't play, try playing it outside of vscode!**

# Effects you can achieve

## i-frame removal
This type of glitch creates the transition effect. Example:

| Original | Moshed |
|:--------:|:------:|
| ![original_hand](https://user-images.githubusercontent.com/31802439/112060042-f3e42780-8b5c-11eb-8019-df4d06dd0d31.gif) | ![moshed_hand](https://user-images.githubusercontent.com/31802439/112060033-f181cd80-8b5c-11eb-9025-65064bbc6200.gif) |

## p-frame duplication
Repeats a series of p-frames (aka delta frames), which can give a 'melting' effect

| Original | Moshed |
|:--------:|:------:|
| ![original_dog](https://user-images.githubusercontent.com/31802439/112059335-0316a580-8b5c-11eb-98c8-3493969dd472.gif) | ![moshed_dog](https://user-images.githubusercontent.com/31802439/112060106-065e6100-8b5d-11eb-9670-4ad3bd9522cd.gif) |

## Vector motion
While the previous effects copy and delete whole frames, this one changes the actual frame data. As explained in
[this article on ffglitch.org](https://ffglitch.org/2020/07/mv.html), you need to write a custom JavaScript file
that can change the frame data. `vector_motion.py` is just a wrapper for `ffedit` and `ffgac` and makes moshing
possible through only one command.
Example:

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

extracts vector data from `clouds.mp4`, transfers it to `trees.mp4`.

| Extract style from | Transfer style to | Result |
|:------------------:|:-----------------:|:------:|
| ![clouds](https://user-images.githubusercontent.com/31802439/112489124-70a21c00-8d7e-11eb-8640-6817a46602ca.gif) | ![trees](https://user-images.githubusercontent.com/31802439/112489146-74ce3980-8d7e-11eb-9091-999fbb98552c.gif) | ![ct](https://user-images.githubusercontent.com/31802439/112489221-86afdc80-8d7e-11eb-9a51-14d91ec7cdfa.gif) |
