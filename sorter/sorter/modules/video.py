import os, shutil

curDir = os.path.dirname(__file__)
home = os.path.dirname(os.path.dirname(curDir))

src = home + "/src/"
dest = home + "/dest/"
formats = home + "/sorter/formats/"

tmp_file = open(formats + "video.txt", "r")
video_formats = tmp_file.readlines()
tmp_file.close()

def run():
    if not os.path.exists(dest + "videos/"):
        os.mkdir(dest + "videos/")

    for home, subDirs, files in os.walk(src):
        for f in files:
            print("checking", f, "...\n")
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
