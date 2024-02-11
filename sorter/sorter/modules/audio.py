import os, shutil

curDir = os.path.dirname(__file__)
home = os.path.dirname(os.path.dirname(curDir))

src = home + "/src/"
dest = home + "/dest/"
formats = home + "/sorter/formats/"

tmp_file = open(formats + "audio.txt", "r")
audio_formats = tmp_file.readlines()
tmp_file.close()

def run():
    if not os.path.exists(dest + "audios/"):
        os.mkdir(dest + "audios/")

    for home, subDirs, files in os.walk(src):
        for f in files:
            print("checking", f, "...\n")
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
