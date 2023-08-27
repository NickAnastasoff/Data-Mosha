#!/usr/bin/env python3

import subprocess

# wicked sick start up screen
print(" ____  ____  ____  ____  ____  ____  ____  ____  ____ ")
print("                                                      ")
print(" ____   __  ____  __     _  _   __   ____  _  _   __  ")
print("(    \ / _\(_  _)/ _\   ( \/ ) /  \ / ___)/ )( \ / _\ ")
print(") D (/    \ )( /    \  / \/ \(  O )\___ \) __ (/    \ ")
print("(____/\_/\_/(__)\_/\_/  \_)(_/ \__/ (____/\_)(_/\_/\_/")
print("Thanks to tiberiuiancu and itsKaspar for awesome code!")
print(" ____  ____  ____  ____  ____  ____  ____  ____  ____ ")

print("\ntiberiuiancu/datamoshing")

print("\tA - TRANSFER MOTION VECTORS")
# python3 style_transfer.py -e {input_video} -t {input_video2} {output_video}

print("\tB - AVERAGE MOTION VECTORS")
# python3 vector_motion.py {input_video} -s average_motion_example.py -o {output_video}

print("\tC - DELETE VERTICAL MOTION VECTORS")
# python3 vector_motion.py {input_video} -s horizontal_motion_example.py -o {output_video}

print("\tD - DELETE I-FRAMES")
# python3 mosh.py {input_video} -s {start frame} -e {end frame} -o {output_video}

print("\tE - DUPLICATE P-FRAMES")
# python3 mosh.py {input_video} -d {delta_frames} -s {start} -o {output_video}

print("\tF - GET VECTORS AS JSON")
# python3 style_transfer.py -e {input_video} {output json}

print("\nitsKaspar/tomato")

print("\tG - KILL remove frames with data higher than min")
# python3 tomato.py -i {input_video} -m void -k {kill}

print("\tH - RANDOM randomizes frame order")
# python3 tomato.py -i {input_video} -m random -k {kill}

print("\tI - REVERSE reverse frame order")
# python3 tomato.py -i {input_video} -m reverse -k {kill}

print("\tJ - INVERT switches each consecutive frame witch each other")
# python3 tomato.py -i {input_video} -m invert -k {kill}

print("\tK - BLOOM duplicates c times p-frame number n")
# python3 tomato.py -i {input_video} -m bloom -c {number_duplicates} -n {number_frame} -k {kill}

print("\tL - PULSE duplicates groups of c p-frames every n frames")
# python3 tomato.py -i {input_video} -m pulse -c {number_duplicates} -n {number_frame} -k {kill}

print("\tM - OVERLAP copy group of c frames taken from every nth position")
# python3 tomato.py -i {input_video} -m overlap -c {number_duplicates} -n {number_frame} -k {kill}

print("\tN - JIGGLE take frame from around current position. n parameter is spread size [broken]")
# python3 tomato.py -i {input_video} -m jiggle -n {number_frame} -k {kill}
print(" ____  ____  ____  ____  ____  ____  ____  ____  ____ ")
operation = input("Please enter a letter: ").upper()

if operation == "A":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    input_video2 = input("Please enter input video 2 (default - input2.mp4): ")
    if input_video2 == "":
        input_video2 = "input2.mp4"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(f'python3 style_transfer.py -e {input_video} -t {input_video2} {output_video}', shell=True)
    print(f'python3 style_transfer.py -e {input_video} -t {input_video2} {output_video}')

if operation == "B":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(f'python3 vector_motion.py {input_video} -s average_motion_example.py -o {output_video}', shell=True)
    print(f'python3 vector_motion.py {input_video} -s average_motion_example.py -o {output_video}')

if operation == "C":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(f'python3 vector_motion.py {input_video} -s horizontal_motion_example.py -o {output_video}', shell=True)
    print(f'python3 vector_motion.py {input_video} -s horizontal_motion_example.py -o {output_video}')

if operation == "D":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    start_frame = input("Please enter start frame (default - 0): ")
    if start_frame == "":
        start_frame = "0"
    end_frame = input("Please enter end frame (default - 0): ")
    if end_frame == "":
        end_frame = "0"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(f'python3 mosh.py {input_video} -s {start_frame} -e {end_frame} -o {output_video}', shell=True)
    print(f'python3 mosh.py {input_video} -s {start_frame} -e {end_frame} -o {output_video}')

if operation == "E":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    delta_frames = input("Please enter delta frames (default - 0): ")
    if delta_frames == "":
        delta_frames = "0"
    start_frame = input("Please enter start frame (default - 0): ")
    if start_frame == "":
        start_frame = "0"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(f'python3 mosh.py {input_video} -d {delta_frames} -s {start_frame} -o {output_video}', shell=True)
    print(f'python3 mosh.py {input_video} -d {delta_frames} -s {start_frame} -o {output_video}')

if operation == "F":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    output_json = input("Please enter output json (default - output.json): ")
    if output_json == "":
        output_json = "output.json"
    subprocess.call(f'python3 style_transfer.py -e {input_video} {output_json}', shell=True)
    print(f'python3 style_transfer.py -e {input_video} {output_json}')

if operation == "G":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    kill_min = input("Please enter kill min (default - .5): ")
    if kill_min == "":
        kill_min = ".5"
    subprocess.call(f'python3 tomato.py -i {input_video} -o {output_video} -m void -k {kill_min}', shell=True)
    print(f'python3 tomato.py -i {input_video} -o {output_video} -m void -k {kill_min}')

if operation == "H":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(f'python3 tomato.py -i {input_video} -o {output_video} -m random ', shell=True)
    print(f'python3 tomato.py -i {input_video} -o {output_video} -m random')

if operation == "I":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(f'python3 tomato.py -i {input_video} -o {output_video} -m reverse', shell=True)
    print(f'python3 tomato.py -i {input_video} -o {output_video} -m reverse')

if operation == "J":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(f'python3 tomato.py -i {input_video} -o {output_video} -m invert', shell=True)
    print(f'python3 tomato.py -i {input_video} -o {output_video} -m invert')

if operation == "K":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    number_duplicates = input("Please enter number of duplicates (default - 1): ")
    if number_duplicates == "":
        number_duplicates = "1"
    number_frame = input("Please enter number of frame (default - 1): ")
    if number_frame == "":
        number_frame = "1"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(
        f'python3 tomato.py -i {input_video} -o {output_video} -m bloom -c {number_duplicates} -n {number_frame} -o {output_video}',
        shell=True)
    print(f'python3 tomato.py -i {input_video} -o {output_video} -m bloom -c {number_duplicates} -n {number_frame} -o {output_video}')
    
if operation == "L":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    number_duplicates = input("Please enter number of duplicates (default - 1): ")
    if number_duplicates == "":
        number_duplicates = "1"
    number_frame = input("Please enter number of frame (default - 1): ")
    if number_frame == "":
        number_frame = "1"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(
        f'python3 tomato.py -i {input_video} -o {output_video} -m pulse -c {number_duplicates} -n {number_frame} -o {output_video}',
        shell=True)
    print(f'python3 tomato.py -i {input_video} -o {output_video} -m pulse -c {number_duplicates} -n {number_frame} -o {output_video}')
    
if operation == "M":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    number_duplicates = input("Please enter number of duplicates (default - 1): ")
    if number_duplicates == "":
        number_duplicates = "1"
    number_frame = input("Please enter number of frame (default - 1): ")
    if number_frame == "":
        number_frame = "1"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(
        f'python3 tomato.py -i {input_video} -o {output_video} -m overlap -c {number_duplicates} -n {number_frame} -o {output_video}',
        shell=True)
    print(f'python3 tomato.py -i {input_video} -o {output_video} -m overlap -c {number_duplicates} -n {number_frame} -o {output_video}')
    
if operation == "N":
    input_video = input("Please enter input video (default - input.mp4): ")
    if input_video == "":
        input_video = "input.mp4"
    number_frame = input("Please enter number of frame (default - 1): ")
    if number_frame == "":
        number_frame = "1"
    output_video = input("Please enter output video (default - output.mp4): ")
    if output_video == "":
        output_video = "output.mp4"
    subprocess.call(
        f'python3 tomato.py -i {input_video} -o {output_video} -m jiggle -n {number_frame} -o {output_video}',
        shell=True)
    print(f'python3 tomato.py -i {input_video} -o {output_video} -m jiggle -n {number_frame} -o {output_video}')
    