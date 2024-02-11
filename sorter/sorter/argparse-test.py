"""
----------------------------------------
----------------------------------------
                sorter
               argparse
----------------------------------------
----------------------------------------
"""

import argparse
import os
import shutil

home = os.path.dirname(os.path.dirname(__file__))

src = home + "/src/"
dest = home + "/dest/"
formats = home + "/sorter/formats/"

audio_text = open(formats + "audio.txt", "r")
audio_formats = audio_text.readlines()
audio_text.close()

document_text = open(formats + "document.txt", "r")
document_formats = document_text.readlines()
document_text.close()

video_text = open(formats + "video.txt", "r")
video_formats = video_text.readlines()
video_text.close()

image_text = open(formats + "image.txt", "r")
image_formats = image_text.readlines()
image_text.close()

def audio_run():
    if not os.path.exists(dest + "audios/"):
        os.mkdir(dest + "audios/")

    for home, subDirs, files in os.walk(src):
        for f in files:
            print("Checking", f, "...\n")
            tmp = False
            for d in audio_formats:
                d = d.strip("\n")
                print("Checking", d, "...\n")
                if d in f:
                    shutil.move(src + f, dest + "audios/" + f)
                    tmp = True
                    break
            if tmp:
                print(f, "is successfully moved in 'audios'.\n")
            else:
                print(f, "couldn't be moved in 'audios'.\n")

def document_run():
    if not os.path.exists(dest + "documents/"):
        os.mkdir(dest + "documents/")

    for home, subDirs, files in os.walk(src):
        for f in files:
            print("Checking", f, "...\n")
            tmp = False
            for d in document_formats:
                d = d.strip("\n")
                print("Checking", d, "...\n")
                if d in f:
                    shutil.move(src + f, dest + "documents/" + f)
                    tmp = True
                    break
            if tmp:
                print(f, "is successfully moved in 'documents'.\n")
            else:
                print(f, "couldn't be moved in 'documents'.\n")

def image_run():
    if not os.path.exists(dest + "images/"):
        os.mkdir(dest + "images/")

    for home, subDirs, files in os.walk(src):
        for f in files:
            print("Checking", f, "...\n")
            tmp = False
            for d in image_formats:
                d = d.strip("\n")
                print("Checking", d, "...\n")
                if d in f:
                    shutil.move(src + f, dest + "images/" + f)
                    tmp = True
                    break
            if tmp:
                print(f, "is successfully moved in 'images'.\n")
            else:
                print(f, "couldn't be moved in 'images'.\n")

def video_run():
    if not os.path.exists(dest + "videos/"):
        os.mkdir(dest + "videos/")

    for home, subDirs, files in os.walk(src):
        for f in files:
            print("Checking", f, "...\n")
            tmp = False
            for d in video_formats:
                d = d.strip("\n")
                print("Checking", d, "...\n")
                if d in f:
                    shutil.move(src + f, dest + "videos/" + f)
                    tmp = True
                    break
            if tmp:
                print(f, "is successfully moved in 'videos'.\n")
            else:
                print(f, "couldn't be moved in 'videos'.\n")

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

subparsers = parser.add_subparsers(
    dest = "command",
    help = "list of operations"
)
subparsers.required = True

for function in(
    audio_run,
    document_run,
    video_run,
    image_run
):
    parser_func = subparsers.add_parser(
        function.__name__,
        help=function.__doc__)
    parser_func.set_defaults(func=function)

if __name__ == '__main__':
    args = parser.parse_args()
    res = args.func()
    print(res)
